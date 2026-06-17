r"""
LEO Institutional Approval Human Review Package Tests

Canonical save path:
D:\BBS-09-01-2026\leo\runtime\demos\institutional_approval_review\tests\test_institutional_approval_human_review_package.py

Purpose:
Validate the local human review export package layer for the Institutional
Approval Review demo slice.

Boundary:
- No production mutation.
- No canonical registry mutation.
- No autonomous approval or rejection.
- No enforcement actions.
- No source evidence report mutation.
"""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import pytest

from institutional_approval_human_review_package import (
    ACTIONS_REQUIRING_REVIEWER_NOTE,
    ALLOWED_REVIEW_ACTIONS,
    PACKAGE_TYPE,
    PACKAGE_VERSION,
    SOURCE_SLICE,
    HumanReviewPackageError,
    assert_no_prohibited_package_keys,
    build_human_review_package,
    build_source_report_summary,
    create_review_record,
    generate_human_review_package_file,
    load_json_file,
    validate_review_record,
    validate_review_records,
)


@pytest.fixture()
def sample_source_report() -> dict:
    return {
        "report_id": "INST-REPORT-001",
        "generated_at": "2026-05-15T12:00:00+00:00",
        "findings": [
            {
                "finding_id": "FINDING-001",
                "severity": "HIGH",
                "signal_family": "missing_board_approval",
            },
            {
                "finding_id": "FINDING-002",
                "severity": "MEDIUM",
                "signal_family": "approval_sequence_gap",
            },
            {
                "finding_id": "FINDING-003",
                "severity": "LOW",
                "signal_family": "documentation_review",
            },
        ],
        "evidence_objects": [
            {"evidence_id": "EV-001"},
            {"evidence_id": "EV-002"},
        ],
    }


@pytest.fixture()
def sample_review_record() -> dict:
    return create_review_record(
        finding_id="FINDING-001",
        review_action="ESCALATE_FOR_REVIEW",
        reviewer_note="Board approval chain requires governance review.",
        reviewer_id="reviewer_local_01",
        source_evidence_ids=["EV-001"],
    )


@pytest.fixture()
def multiple_review_records() -> list[dict]:
    return [
        create_review_record(
            finding_id="FINDING-001",
            review_action="ESCALATE_FOR_REVIEW",
            reviewer_note="Escalated for institutional governance review.",
            reviewer_id="reviewer_local_01",
            source_evidence_ids=["EV-001"],
        ),
        create_review_record(
            finding_id="FINDING-002",
            review_action="REQUEST_MORE_EVIDENCE",
            reviewer_note="Missing supporting approval memo.",
            reviewer_id="reviewer_local_02",
            source_evidence_ids=["EV-002"],
            follow_up_required=True,
            follow_up_reason="Awaiting institutional clarification.",
        ),
    ]


class TestReviewRecordValidation:
    def test_allowed_review_actions_are_present(self) -> None:
        expected = {
            "ESCALATE_FOR_REVIEW",
            "ACCEPT_AS_JUSTIFIED",
            "MARK_FALSE_POSITIVE",
            "REQUEST_MORE_EVIDENCE",
            "DEFER_REVIEW",
        }
        assert ALLOWED_REVIEW_ACTIONS == expected

    def test_actions_requiring_note_are_subset(self) -> None:
        assert ACTIONS_REQUIRING_REVIEWER_NOTE.issubset(ALLOWED_REVIEW_ACTIONS)

    def test_create_review_record_succeeds(self) -> None:
        record = create_review_record(
            finding_id="FINDING-100",
            review_action="ACCEPT_AS_JUSTIFIED",
            reviewer_note="Explanation accepted after review.",
        )

        assert record["finding_id"] == "FINDING-100"
        assert record["review_action"] == "ACCEPT_AS_JUSTIFIED"
        assert record["zero_autonomy_acknowledged"] is True

    def test_unknown_review_action_fails(self) -> None:
        with pytest.raises(HumanReviewPackageError, match="Unknown review_action"):
            create_review_record(
                finding_id="FINDING-101",
                review_action="AUTO_APPROVE",
                reviewer_note="Invalid action.",
            )

    @pytest.mark.parametrize(
        "review_action",
        [
            "ESCALATE_FOR_REVIEW",
            "MARK_FALSE_POSITIVE",
            "REQUEST_MORE_EVIDENCE",
            "DEFER_REVIEW",
        ],
    )
    def test_required_note_enforced(self, review_action: str) -> None:
        with pytest.raises(HumanReviewPackageError, match="reviewer_note"):
            create_review_record(
                finding_id="FINDING-102",
                review_action=review_action,
                reviewer_note="   ",
            )

    def test_follow_up_reason_required_when_follow_up_enabled(self) -> None:
        with pytest.raises(HumanReviewPackageError, match="follow_up_reason"):
            create_review_record(
                finding_id="FINDING-103",
                review_action="REQUEST_MORE_EVIDENCE",
                reviewer_note="Need more documentation.",
                follow_up_required=True,
            )

    def test_reviewer_id_must_be_non_empty(self) -> None:
        with pytest.raises(HumanReviewPackageError, match="reviewer_id"):
            create_review_record(
                finding_id="FINDING-104",
                review_action="ACCEPT_AS_JUSTIFIED",
                reviewer_note="Accepted.",
                reviewer_id="",
            )

    def test_source_evidence_ids_must_be_strings(self) -> None:
        with pytest.raises(HumanReviewPackageError, match="source_evidence_ids"):
            create_review_record(
                finding_id="FINDING-105",
                review_action="ESCALATE_FOR_REVIEW",
                reviewer_note="Escalated.",
                source_evidence_ids=[123],
            )

    def test_validate_review_records_returns_copy(self, sample_review_record: dict) -> None:
        records = [sample_review_record]
        validated = validate_review_records(records)

        assert validated == records
        assert validated is not records
        assert validated[0] is not records[0]


class TestSourceReportSummary:
    def test_build_source_report_summary(self, sample_source_report: dict) -> None:
        summary = build_source_report_summary(sample_source_report)

        assert summary["source_report_id"] == "INST-REPORT-001"
        assert summary["findings_count"] == 3
        assert summary["evidence_objects_count"] == 2
        assert summary["findings_by_severity"]["HIGH"] == 1
        assert summary["findings_by_signal_family"]["missing_board_approval"] == 1


class TestHumanReviewPackage:
    def test_build_package_succeeds(
        self,
        sample_source_report: dict,
        multiple_review_records: list[dict],
    ) -> None:
        package = build_human_review_package(
            source_report=sample_source_report,
            review_records=multiple_review_records,
        )

        assert package["package_type"] == PACKAGE_TYPE
        assert package["package_version"] == PACKAGE_VERSION
        assert package["source_slice"] == SOURCE_SLICE
        assert package["reviewed_findings_count"] == 2
        assert len(package["review_records"]) == 2

    def test_zero_autonomy_boundary_present(
        self,
        sample_source_report: dict,
    ) -> None:
        package = build_human_review_package(
            source_report=sample_source_report,
            review_records=[],
        )

        boundary = package["zero_autonomy_boundary"]

        assert boundary["autonomous_approval"] is False
        assert boundary["autonomous_rejection"] is False
        assert boundary["autonomous_enforcement"] is False
        assert boundary["production_mutation"] is False
        assert boundary["canonical_registry_mutation"] is False
        assert boundary["legal_verdict"] is False

    def test_package_contains_integrity_notes(
        self,
        sample_source_report: dict,
    ) -> None:
        package = build_human_review_package(
            source_report=sample_source_report,
            review_records=[],
        )

        notes = package["export_integrity_notes"]
        assert isinstance(notes, list)
        assert len(notes) >= 1

    def test_empty_review_record_list_allowed(
        self,
        sample_source_report: dict,
    ) -> None:
        package = build_human_review_package(
            source_report=sample_source_report,
            review_records=[],
        )

        assert package["reviewed_findings_count"] == 0
        assert package["review_records"] == []

    def test_source_report_not_modified(
        self,
        sample_source_report: dict,
        sample_review_record: dict,
    ) -> None:
        original = deepcopy(sample_source_report)

        build_human_review_package(
            source_report=sample_source_report,
            review_records=[sample_review_record],
        )

        assert sample_source_report == original

    def test_review_records_preserve_finding_ids(
        self,
        sample_source_report: dict,
        sample_review_record: dict,
    ) -> None:
        package = build_human_review_package(
            source_report=sample_source_report,
            review_records=[sample_review_record],
        )

        assert package["review_records"][0]["finding_id"] == "FINDING-001"

    def test_review_records_preserve_evidence_ids(
        self,
        sample_source_report: dict,
        sample_review_record: dict,
    ) -> None:
        package = build_human_review_package(
            source_report=sample_source_report,
            review_records=[sample_review_record],
        )

        assert package["review_records"][0]["source_evidence_ids"] == ["EV-001"]

    def test_source_report_id_propagated(
        self,
        sample_source_report: dict,
        sample_review_record: dict,
    ) -> None:
        package = build_human_review_package(
            source_report=sample_source_report,
            review_records=[sample_review_record],
        )

        assert package["source_report_id"] == "INST-REPORT-001"
        assert (
            package["review_records"][0]["source_report_id"]
            == "INST-REPORT-001"
        )

    def test_prohibited_package_keys_fail(self) -> None:
        with pytest.raises(HumanReviewPackageError, match="prohibited"):
            assert_no_prohibited_package_keys(
                {
                    "package_type": PACKAGE_TYPE,
                    "fraud_verdict": True,
                }
            )

    def test_invalid_source_report_fails(self) -> None:
        with pytest.raises(HumanReviewPackageError, match="source_report"):
            build_human_review_package(
                source_report="invalid",
                review_records=[],
            )


class TestPackageFileGeneration:
    def test_generate_package_file(
        self,
        tmp_path: Path,
        sample_source_report: dict,
        sample_review_record: dict,
    ) -> None:
        source_report_path = tmp_path / "institutional_approval_evidence_report.json"
        output_package_path = tmp_path / "institutional_approval_human_review_package.json"

        source_report_path.write_text(
            json.dumps(sample_source_report, indent=2),
            encoding="utf-8",
        )

        package = generate_human_review_package_file(
            source_report_path=source_report_path,
            output_package_path=output_package_path,
            review_records=[sample_review_record],
        )

        assert output_package_path.exists()
        assert package["package_type"] == PACKAGE_TYPE

        reloaded = json.loads(output_package_path.read_text(encoding="utf-8"))
        assert reloaded["package_version"] == PACKAGE_VERSION

    def test_source_report_file_not_modified(
        self,
        tmp_path: Path,
        sample_source_report: dict,
        sample_review_record: dict,
    ) -> None:
        source_report_path = tmp_path / "institutional_approval_evidence_report.json"
        output_package_path = tmp_path / "institutional_approval_human_review_package.json"

        original_text = json.dumps(sample_source_report, indent=2)
        source_report_path.write_text(original_text, encoding="utf-8")

        generate_human_review_package_file(
            source_report_path=source_report_path,
            output_package_path=output_package_path,
            review_records=[sample_review_record],
        )

        current_text = source_report_path.read_text(encoding="utf-8")
        assert current_text == original_text

    def test_missing_source_report_fails(self, tmp_path: Path) -> None:
        missing_path = tmp_path / "missing.json"
        output_path = tmp_path / "output.json"

        with pytest.raises(HumanReviewPackageError, match="Source report not found"):
            generate_human_review_package_file(
                source_report_path=missing_path,
                output_package_path=output_path,
            )

    def test_invalid_json_source_report_fails(self, tmp_path: Path) -> None:
        invalid_path = tmp_path / "invalid.json"
        invalid_path.write_text("not valid json", encoding="utf-8")

        with pytest.raises(HumanReviewPackageError, match="Invalid JSON"):
            load_json_file(invalid_path)

    def test_output_path_must_differ_from_source_path(
        self,
        tmp_path: Path,
        sample_source_report: dict,
    ) -> None:
        same_path = tmp_path / "same.json"
        same_path.write_text(
            json.dumps(sample_source_report, indent=2),
            encoding="utf-8",
        )

        with pytest.raises(HumanReviewPackageError, match="must differ"):
            generate_human_review_package_file(
                source_report_path=same_path,
                output_package_path=same_path,
            )

    def test_generated_json_can_be_reloaded(
        self,
        tmp_path: Path,
        sample_source_report: dict,
    ) -> None:
        source_report_path = tmp_path / "source.json"
        output_package_path = tmp_path / "package.json"

        source_report_path.write_text(
            json.dumps(sample_source_report, indent=2),
            encoding="utf-8",
        )

        generate_human_review_package_file(
            source_report_path=source_report_path,
            output_package_path=output_package_path,
            review_records=[],
        )

        loaded = json.loads(output_package_path.read_text(encoding="utf-8"))

        assert loaded["package_type"] == PACKAGE_TYPE
        assert loaded["source_slice"] == SOURCE_SLICE
        assert loaded["zero_autonomy_boundary"]["autonomous_enforcement"] is False
