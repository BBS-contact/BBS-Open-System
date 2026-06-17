r"""
Tests for LEO Institutional Approval Evidence Report Validator v0.1

Canonical Path:
D:\BBS-09-01-2026\leo\runtime\demos\institutional_approval_review\tests\test_institutional_approval_evidence_report_validator.py

Purpose:
Validate the Institutional Approval Review evidence report validator without
performing production mutation, workflow execution, legal interpretation,
payment action, staff action, canonical registry mutation, signing, key access,
ERP/HR integration, or external execution.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

CURRENT_DIR = Path(__file__).resolve().parent
DEMO_DIR = CURRENT_DIR.parent

if str(DEMO_DIR) not in sys.path:
    sys.path.insert(0, str(DEMO_DIR))

from institutional_approval_evidence_report_validator import (
    EXPECTED_EVIDENCE_OBJECTS_COUNT,
    EXPECTED_FINDINGS_COUNT,
    EXPECTED_HIGH_OR_CRITICAL_COUNT,
    InstitutionalApprovalEvidenceReportValidator,
    ValidationIssue,
    build_validator_zero_autonomy_boundary,
    validate_institutional_approval_evidence_report,
)
from institutional_approval_review_pipeline import (
    generate_institutional_approval_evidence_report,
)


@pytest.fixture()
def valid_report_payload() -> dict:
    """Return a compact valid report fixture for validator unit tests."""

    finding = {
        "id": "IAR-001",
        "request_id": "REQ-001",
        "title": "Missing required approval",
        "severity": "HIGH",
        "signal_family": "missing_required_approval",
        "detected_signal": "Required approval role is missing.",
        "why_it_matters": "Approval continuity is incomplete.",
        "reviewer_question": "Which approval is missing?",
        "next_action": "Request missing approval evidence.",
        "responsible_review_layer": ["management_board"],
        "rule_trace": {
            "source_rule_id": "APR-RULE-003",
            "source_rule_name": "High-value procurement requires review.",
            "source_rule_file": "approval_policy_rules.csv",
            "protocol_reference": "MISSING_REQUIRED_APPROVAL_PROTOCOL_v0.1.md",
            "human_readable_rule": "High-value procurement requires finance, legal, and management review.",
            "verdict_boundary": "This rule creates a human review requirement only.",
        },
        "evidence_ids": ["IAE-001"],
        "verdict_boundary": "This finding is a human-review signal only. It does not approve, reject, block, punish, sign, mutate, or execute any institutional action.",
        "zero_autonomy_boundary": build_validator_zero_autonomy_boundary(),
    }

    evidence = {
        "evidence_id": "IAE-001",
        "finding_id": "IAR-001",
        "request_id": "REQ-001",
        "source_records": ["approval_requests:REQ-001"],
        "signal_family": "missing_required_approval",
        "evidence_summary": "Required approval role is missing.",
        "data_points": {"missing_roles": ["management_board"]},
        "created_at": "2026-05-15T00:00:00Z",
        "boundary_statement": "Evidence object preserves local review context only and does not mutate source records or execute institutional action.",
    }

    return {
        "report_id": "LOCAL_INSTITUTIONAL_APPROVAL_EVIDENCE_REPORT",
        "report_version": "v0.1",
        "generated_at": "2026-05-15T00:00:00Z",
        "source_input_quality_report": "output/institutional_approval_input_quality_report.json",
        "input_quality_status": "READY",
        "input_quality_ready_for_analysis": True,
        "summary": {
            "findings_count": 1,
            "evidence_objects_count": 1,
            "high_or_critical_findings_count": 1,
            "signal_families": {"missing_required_approval": 1},
            "autonomous_actions": 0,
        },
        "findings": [finding],
        "evidence_objects": [evidence],
        "zero_autonomy_boundary": build_validator_zero_autonomy_boundary(),
    }


def write_json(path: Path, payload: dict | list | str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def test_validation_issue_to_dict() -> None:
    issue = ValidationIssue(
        severity="ERROR",
        code="TEST_ERROR",
        message="Test message",
        item_id="IAR-001",
    )

    assert issue.to_dict() == {
        "severity": "ERROR",
        "code": "TEST_ERROR",
        "message": "Test message",
        "item_id": "IAR-001",
    }


def test_validator_accepts_current_real_evidence_report() -> None:
    validator = InstitutionalApprovalEvidenceReportValidator(
        report_path=DEMO_DIR / "output" / "institutional_approval_evidence_report.json"
    )

    result = validator.validate()
    payload = result.to_dict()

    assert result.status == "VALID"
    assert result.is_valid is True
    assert result.summary["error_count"] == 0
    assert result.summary["warning_count"] == 0
    assert result.summary["findings_count"] == EXPECTED_FINDINGS_COUNT
    assert result.summary["evidence_objects_count"] == EXPECTED_EVIDENCE_OBJECTS_COUNT
    assert result.summary["high_or_critical_findings_count"] == EXPECTED_HIGH_OR_CRITICAL_COUNT
    assert result.summary["autonomous_actions"] == 0
    assert payload["issues"] == []


def test_validator_reports_missing_file(tmp_path: Path) -> None:
    validator = InstitutionalApprovalEvidenceReportValidator(
        report_path=tmp_path / "missing.json"
    )

    result = validator.validate()

    assert result.status == "INVALID"
    assert result.is_valid is False
    assert result.summary["error_count"] == 1
    assert result.issues[0].code == "REPORT_FILE_MISSING"


def test_validator_reports_invalid_json(tmp_path: Path) -> None:
    path = tmp_path / "invalid.json"
    path.write_text("{invalid-json", encoding="utf-8")
    validator = InstitutionalApprovalEvidenceReportValidator(report_path=path)

    result = validator.validate()

    assert result.status == "INVALID"
    assert result.is_valid is False
    assert result.issues[0].code == "INVALID_JSON"


def test_validator_reports_invalid_json_root(tmp_path: Path) -> None:
    path = tmp_path / "list.json"
    write_json(path, [])
    validator = InstitutionalApprovalEvidenceReportValidator(report_path=path)

    result = validator.validate()

    assert result.status == "INVALID"
    assert result.issues[0].code == "INVALID_JSON_ROOT"


def test_validator_detects_missing_top_level_field(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload.pop("findings")
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "MISSING_TOP_LEVEL_FIELD" for issue in result.issues)


def test_validator_detects_unexpected_report_identity(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload["report_id"] = "WRONG"
    payload["report_version"] = "v9"
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "UNEXPECTED_REPORT_ID" for issue in result.issues)
    assert any(issue.code == "UNEXPECTED_REPORT_VERSION" for issue in result.issues)


def test_validator_detects_input_quality_not_ready(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload["input_quality_ready_for_analysis"] = False
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "INPUT_QUALITY_NOT_READY" for issue in result.issues)


def test_validator_detects_summary_count_mismatch(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload["summary"]["findings_count"] = 2
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "FINDINGS_COUNT_MISMATCH" for issue in result.issues)


def test_validator_detects_autonomous_actions_violation(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload["summary"]["autonomous_actions"] = 1
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "UNEXPECTED_SUMMARY_VALUE" for issue in result.issues)


def test_validator_detects_missing_finding_field(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload["findings"][0].pop("rule_trace")
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "MISSING_FINDING_FIELD" for issue in result.issues)
    assert any(issue.code == "INVALID_RULE_TRACE" for issue in result.issues)


def test_validator_detects_invalid_finding_values(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload["findings"][0]["severity"] = "SEVERE"
    payload["findings"][0]["signal_family"] = "unknown_signal"
    payload["findings"][0]["responsible_review_layer"] = []
    payload["findings"][0]["evidence_ids"] = []
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "INVALID_SEVERITY" for issue in result.issues)
    assert any(issue.code == "INVALID_SIGNAL_FAMILY" for issue in result.issues)
    assert any(issue.code == "EMPTY_RESPONSIBLE_REVIEW_LAYER" for issue in result.issues)
    assert any(issue.code == "EMPTY_EVIDENCE_IDS" for issue in result.issues)


def test_validator_detects_missing_rule_trace_fields(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload["findings"][0]["rule_trace"] = {
        "source_rule_id": "APR-RULE-003",
    }
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "MISSING_RULE_TRACE_FIELD" for issue in result.issues)


def test_validator_warns_on_unexpected_rule_source(tmp_path: Path) -> None:
    source_report = DEMO_DIR / "output" / "institutional_approval_evidence_report.json"
    payload = json.loads(source_report.read_text(encoding="utf-8"))

    payload["findings"][0]["rule_trace"]["source_rule_file"] = "other.csv"
    payload["findings"][0]["rule_trace"]["protocol_reference"] = "protocol.txt"

    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "VALID_WITH_WARNINGS"
    assert result.is_valid is True
    assert result.summary["error_count"] == 0
    assert result.summary["warning_count"] == 2
    assert any(issue.code == "UNEXPECTED_RULE_SOURCE" for issue in result.issues)
    assert any(issue.code == "PROTOCOL_REFERENCE_NOT_MARKDOWN" for issue in result.issues)


def test_validator_detects_missing_evidence_field(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload["evidence_objects"][0].pop("source_records")
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "MISSING_EVIDENCE_FIELD" for issue in result.issues)
    assert any(issue.code == "EMPTY_SOURCE_RECORDS" for issue in result.issues)


def test_validator_detects_duplicate_ids(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload["findings"].append(json.loads(json.dumps(payload["findings"][0])))
    payload["evidence_objects"].append(json.loads(json.dumps(payload["evidence_objects"][0])))
    payload["summary"]["findings_count"] = 2
    payload["summary"]["evidence_objects_count"] = 2
    payload["summary"]["high_or_critical_findings_count"] = 2
    payload["summary"]["signal_families"] = {"missing_required_approval": 2}
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "DUPLICATE_FINDING_ID" for issue in result.issues)
    assert any(issue.code == "DUPLICATE_EVIDENCE_ID" for issue in result.issues)


def test_validator_detects_missing_linked_evidence(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload["findings"][0]["evidence_ids"] = ["IAE-999"]
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "MISSING_LINKED_EVIDENCE" for issue in result.issues)


def test_validator_detects_orphan_evidence_object(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload["evidence_objects"][0]["finding_id"] = "IAR-999"
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "EVIDENCE_FINDING_LINK_MISMATCH" for issue in result.issues)
    assert any(issue.code == "ORPHAN_EVIDENCE_OBJECT" for issue in result.issues)


def test_validator_detects_signal_family_summary_mismatch(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload["summary"]["signal_families"] = {"missing_decision_owner": 1}
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "SIGNAL_FAMILY_SUMMARY_MISMATCH" for issue in result.issues)


def test_validator_detects_zero_autonomy_violation(
    tmp_path: Path,
    valid_report_payload: dict,
) -> None:
    payload = json.loads(json.dumps(valid_report_payload))
    payload["zero_autonomy_boundary"]["no_external_execution"] = False
    payload["findings"][0]["zero_autonomy_boundary"]["no_payment_blocking"] = False
    path = tmp_path / "report.json"
    write_json(path, payload)

    result = InstitutionalApprovalEvidenceReportValidator(path).validate()

    assert result.status == "INVALID"
    assert any(issue.code == "ZERO_AUTONOMY_BOUNDARY_VIOLATION" for issue in result.issues)


def test_validate_institutional_approval_evidence_report_writes_output(tmp_path: Path) -> None:
    report_file = DEMO_DIR / "output" / "institutional_approval_evidence_report.json"
    output_file = tmp_path / "validation.json"

    result = validate_institutional_approval_evidence_report(
        report_path=report_file,
        output_file=output_file,
    )

    assert result.status == "VALID"
    assert result.is_valid is True
    assert output_file.exists()
    payload = json.loads(output_file.read_text(encoding="utf-8"))
    assert payload["status"] == "VALID"
    assert payload["summary"]["findings_count"] == EXPECTED_FINDINGS_COUNT


def test_validator_zero_autonomy_boundary_contains_required_fields() -> None:
    boundary = build_validator_zero_autonomy_boundary()

    assert boundary["no_autonomous_approval"] is True
    assert boundary["no_autonomous_rejection"] is True
    assert boundary["no_payment_blocking"] is True
    assert boundary["no_staff_punishment"] is True
    assert boundary["no_legal_conclusion"] is True
    assert boundary["no_donor_compliance_conclusion"] is True
    assert boundary["no_board_decision"] is True
    assert boundary["no_production_mutation"] is True
    assert boundary["no_canonical_registry_mutation"] is True
    assert boundary["no_signing_or_key_access"] is True
    assert boundary["no_external_execution"] is True
    assert "does not approve" in boundary["statement"]
