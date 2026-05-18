r"""
Tests for LEO Institutional Approval Review Input Quality Report v0.1

Canonical Path:
D:\BBS-09-01-2026\leo\runtime\demos\institutional_approval_review\tests\test_institutional_approval_input_quality_report.py

Purpose:
Validate the Institutional Approval Review input quality module without performing
production mutation, workflow execution, legal interpretation, payment action,
staff action, canonical registry mutation, signing, key access, or external execution.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import pytest

CURRENT_DIR = Path(__file__).resolve().parent
DEMO_DIR = CURRENT_DIR.parent

if str(DEMO_DIR) not in sys.path:
    sys.path.insert(0, str(DEMO_DIR))

from institutional_approval_input_quality_report import (
    InstitutionalApprovalInputQualityAnalyzer,
    InputQualityIssue,
    build_zero_autonomy_boundary,
    generate_input_quality_report,
)


REQUEST_COLUMNS = [
    "request_id",
    "request_type",
    "request_title",
    "request_date",
    "requested_by",
    "department",
    "amount_pln",
    "risk_level",
    "execution_status",
    "handoff_status",
    "current_owner",
    "final_decision_state",
    "requires_legal_review",
    "requires_finance_review",
    "requires_management_review",
    "emergency_override_used",
    "override_reason_present",
    "linked_contract_reference",
    "linked_budget_reference",
    "notes",
]

STEP_COLUMNS = [
    "step_id",
    "request_id",
    "step_order",
    "role",
    "reviewer_name",
    "review_status",
    "review_date",
    "review_note",
    "is_required",
    "approval_scope",
    "override_reference",
    "review_layer",
    "decision_owner_confirmed",
]

RULE_COLUMNS = [
    "rule_id",
    "request_type",
    "risk_level",
    "amount_threshold_pln",
    "required_roles",
    "required_order",
    "exception_allowed",
    "exception_requires_reason",
    "exception_requires_documentation",
    "human_readable_rule",
    "verdict_boundary",
]

ROLE_COLUMNS = [
    "role",
    "allowed_request_types",
    "approval_limit_pln",
    "can_override",
    "requires_note",
    "requires_secondary_review",
    "review_scope",
    "max_risk_level",
    "active_role",
    "human_readable_role_description",
]

EXCEPTION_COLUMNS = [
    "exception_id",
    "request_id",
    "exception_type",
    "approved_by",
    "approved_role",
    "exception_date",
    "reason_provided",
    "reason_text",
    "documentation_reference",
    "documentation_present",
    "post_event_review_required",
    "post_event_review_status",
    "human_review_required",
    "notes",
]


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    """Write a CSV fixture."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def create_valid_input_files(input_dir: Path) -> None:
    """Create a minimal valid institutional approval dataset."""

    write_csv(
        input_dir / "approval_requests.csv",
        REQUEST_COLUMNS,
        [
            {
                "request_id": "REQ-001",
                "request_type": "PROCUREMENT",
                "request_title": "Medical Equipment Procurement",
                "request_date": "2026-03-01",
                "requested_by": "Anna Kowalska",
                "department": "Operations",
                "amount_pln": "185000",
                "risk_level": "HIGH",
                "execution_status": "PENDING",
                "handoff_status": "NOT_READY",
                "current_owner": "finance_review",
                "final_decision_state": "UNDER_REVIEW",
                "requires_legal_review": "TRUE",
                "requires_finance_review": "TRUE",
                "requires_management_review": "TRUE",
                "emergency_override_used": "FALSE",
                "override_reason_present": "FALSE",
                "linked_contract_reference": "CTR-001",
                "linked_budget_reference": "BL-001",
                "notes": "Valid request fixture",
            }
        ],
    )

    write_csv(
        input_dir / "approval_steps.csv",
        STEP_COLUMNS,
        [
            {
                "step_id": "STEP-001",
                "request_id": "REQ-001",
                "step_order": "1",
                "role": "finance_review",
                "reviewer_name": "Anna Kurek",
                "review_status": "APPROVED",
                "review_date": "2026-03-02",
                "review_note": "Budget confirmed",
                "is_required": "TRUE",
                "approval_scope": "budget_validation",
                "override_reference": "",
                "review_layer": "finance",
                "decision_owner_confirmed": "TRUE",
            }
        ],
    )

    write_csv(
        input_dir / "approval_policy_rules.csv",
        RULE_COLUMNS,
        [
            {
                "rule_id": "APR-RULE-001",
                "request_type": "PROCUREMENT",
                "risk_level": "HIGH",
                "amount_threshold_pln": "100000",
                "required_roles": "finance_review|legal_review|management_board",
                "required_order": "finance_review>legal_review>management_board",
                "exception_allowed": "TRUE",
                "exception_requires_reason": "TRUE",
                "exception_requires_documentation": "TRUE",
                "human_readable_rule": "High-value procurement requires human review.",
                "verdict_boundary": "This rule creates a human review requirement only.",
            }
        ],
    )

    write_csv(
        input_dir / "approval_role_matrix.csv",
        ROLE_COLUMNS,
        [
            {
                "role": "finance_review",
                "allowed_request_types": "PROCUREMENT|GRANT_EXPENSE",
                "approval_limit_pln": "250000",
                "can_override": "FALSE",
                "requires_note": "TRUE",
                "requires_secondary_review": "FALSE",
                "review_scope": "budget_validation",
                "max_risk_level": "CRITICAL",
                "active_role": "TRUE",
                "human_readable_role_description": "Finance validates budget continuity.",
            }
        ],
    )

    write_csv(
        input_dir / "approval_exception_register.csv",
        EXCEPTION_COLUMNS,
        [
            {
                "exception_id": "OVR-001",
                "request_id": "REQ-001",
                "exception_type": "EMERGENCY_OVERRIDE",
                "approved_by": "Jan Kowalczyk",
                "approved_role": "executive_override",
                "exception_date": "2026-03-05",
                "reason_provided": "TRUE",
                "reason_text": "Emergency operational reason provided.",
                "documentation_reference": "documents/overrides/OVR-001.md",
                "documentation_present": "TRUE",
                "post_event_review_required": "TRUE",
                "post_event_review_status": "PENDING",
                "human_review_required": "TRUE",
                "notes": "Valid exception fixture",
            }
        ],
    )


def test_input_quality_issue_to_dict() -> None:
    issue = InputQualityIssue(
        severity="ERROR",
        source="approval_requests",
        code="MISSING_REQUIRED_FILE",
        message="Missing file",
        row_id="REQ-001",
    )

    assert issue.to_dict() == {
        "severity": "ERROR",
        "source": "approval_requests",
        "code": "MISSING_REQUIRED_FILE",
        "message": "Missing file",
        "row_id": "REQ-001",
    }


def test_analyzer_accepts_valid_minimal_dataset(tmp_path: Path) -> None:
    create_valid_input_files(tmp_path)
    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=tmp_path)

    report = analyzer.analyze()

    assert report.status == "READY"
    assert report.ready_for_analysis is True
    assert report.summary["files_loaded"] == 5
    assert report.summary["files_expected"] == 5
    assert report.summary["approval_requests_count"] == 1
    assert report.summary["approval_steps_count"] == 1
    assert report.summary["approval_policy_rules_count"] == 1
    assert report.summary["approval_role_matrix_count"] == 1
    assert report.summary["approval_exception_register_count"] == 1
    assert report.summary["error_count"] == 0
    assert report.summary["warning_count"] == 0
    assert report.issues == []


def test_analyzer_reports_missing_required_files(tmp_path: Path) -> None:
    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=tmp_path)

    report = analyzer.analyze()

    assert report.status == "BLOCKED_BY_INPUT_ERRORS"
    assert report.ready_for_analysis is False
    assert report.summary["files_loaded"] == 0
    assert report.summary["error_count"] == 5
    assert all(issue.code == "MISSING_REQUIRED_FILE" for issue in report.issues)


def test_analyzer_detects_missing_required_column(tmp_path: Path) -> None:
    create_valid_input_files(tmp_path)
    bad_columns = [column for column in REQUEST_COLUMNS if column != "request_id"]
    write_csv(
        tmp_path / "approval_requests.csv",
        bad_columns,
        [
            {
                column: "TRUE" if column.startswith("requires_") else "fixture"
                for column in bad_columns
            }
        ],
    )

    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=tmp_path)
    report = analyzer.analyze()

    assert report.status == "BLOCKED_BY_INPUT_ERRORS"
    assert any(issue.code == "MISSING_REQUIRED_COLUMN" for issue in report.issues)
    assert any("request_id" in issue.message for issue in report.issues)


def test_analyzer_detects_duplicate_ids(tmp_path: Path) -> None:
    create_valid_input_files(tmp_path)
    duplicate_row = {
        "request_id": "REQ-001",
        "request_type": "PROCUREMENT",
        "request_title": "Duplicate Request",
        "request_date": "2026-03-02",
        "requested_by": "Piotr Zielinski",
        "department": "Operations",
        "amount_pln": "1000",
        "risk_level": "LOW",
        "execution_status": "PENDING",
        "handoff_status": "NOT_READY",
        "current_owner": "finance_review",
        "final_decision_state": "UNDER_REVIEW",
        "requires_legal_review": "FALSE",
        "requires_finance_review": "TRUE",
        "requires_management_review": "FALSE",
        "emergency_override_used": "FALSE",
        "override_reason_present": "FALSE",
        "linked_contract_reference": "",
        "linked_budget_reference": "BL-002",
        "notes": "Duplicate ID",
    }
    write_csv(
        tmp_path / "approval_requests.csv",
        REQUEST_COLUMNS,
        [
            {
                "request_id": "REQ-001",
                "request_type": "PROCUREMENT",
                "request_title": "Original Request",
                "request_date": "2026-03-01",
                "requested_by": "Anna Kowalska",
                "department": "Operations",
                "amount_pln": "185000",
                "risk_level": "HIGH",
                "execution_status": "PENDING",
                "handoff_status": "NOT_READY",
                "current_owner": "finance_review",
                "final_decision_state": "UNDER_REVIEW",
                "requires_legal_review": "TRUE",
                "requires_finance_review": "TRUE",
                "requires_management_review": "TRUE",
                "emergency_override_used": "FALSE",
                "override_reason_present": "FALSE",
                "linked_contract_reference": "CTR-001",
                "linked_budget_reference": "BL-001",
                "notes": "Original ID",
            },
            duplicate_row,
        ],
    )

    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=tmp_path)
    report = analyzer.analyze()

    assert report.status == "BLOCKED_BY_INPUT_ERRORS"
    assert any(issue.code == "DUPLICATE_ID" for issue in report.issues)
    assert any(issue.row_id == "REQ-001" for issue in report.issues)


def test_analyzer_detects_unknown_request_reference(tmp_path: Path) -> None:
    create_valid_input_files(tmp_path)
    write_csv(
        tmp_path / "approval_steps.csv",
        STEP_COLUMNS,
        [
            {
                "step_id": "STEP-999",
                "request_id": "REQ-999",
                "step_order": "1",
                "role": "finance_review",
                "reviewer_name": "Anna Kurek",
                "review_status": "APPROVED",
                "review_date": "2026-03-02",
                "review_note": "Unknown request",
                "is_required": "TRUE",
                "approval_scope": "budget_validation",
                "override_reference": "",
                "review_layer": "finance",
                "decision_owner_confirmed": "TRUE",
            }
        ],
    )

    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=tmp_path)
    report = analyzer.analyze()

    assert report.status == "BLOCKED_BY_INPUT_ERRORS"
    assert any(issue.code == "UNKNOWN_REQUEST_REFERENCE" for issue in report.issues)
    assert any("REQ-999" in issue.message for issue in report.issues)


def test_analyzer_detects_invalid_date(tmp_path: Path) -> None:
    create_valid_input_files(tmp_path)
    rows = list(csv.DictReader((tmp_path / "approval_requests.csv").open("r", encoding="utf-8")))
    rows[0]["request_date"] = "15-03-2026"
    write_csv(tmp_path / "approval_requests.csv", REQUEST_COLUMNS, rows)

    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=tmp_path)
    report = analyzer.analyze()

    assert report.status == "BLOCKED_BY_INPUT_ERRORS"
    assert any(issue.code == "INVALID_DATE" for issue in report.issues)


def test_analyzer_allows_pending_step_without_review_date(tmp_path: Path) -> None:
    create_valid_input_files(tmp_path)
    rows = list(csv.DictReader((tmp_path / "approval_steps.csv").open("r", encoding="utf-8")))
    rows[0]["review_status"] = "PENDING"
    rows[0]["review_date"] = ""
    write_csv(tmp_path / "approval_steps.csv", STEP_COLUMNS, rows)

    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=tmp_path)
    report = analyzer.analyze()

    assert report.status == "READY"
    assert not any(issue.code == "MISSING_DATE" for issue in report.issues)


def test_analyzer_detects_invalid_boolean(tmp_path: Path) -> None:
    create_valid_input_files(tmp_path)
    rows = list(csv.DictReader((tmp_path / "approval_requests.csv").open("r", encoding="utf-8")))
    rows[0]["requires_legal_review"] = "YES"
    write_csv(tmp_path / "approval_requests.csv", REQUEST_COLUMNS, rows)

    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=tmp_path)
    report = analyzer.analyze()

    assert report.status == "BLOCKED_BY_INPUT_ERRORS"
    assert any(issue.code == "INVALID_BOOLEAN" for issue in report.issues)


def test_analyzer_detects_invalid_numeric_value(tmp_path: Path) -> None:
    create_valid_input_files(tmp_path)
    rows = list(csv.DictReader((tmp_path / "approval_requests.csv").open("r", encoding="utf-8")))
    rows[0]["amount_pln"] = "not-a-number"
    write_csv(tmp_path / "approval_requests.csv", REQUEST_COLUMNS, rows)

    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=tmp_path)
    report = analyzer.analyze()

    assert report.status == "BLOCKED_BY_INPUT_ERRORS"
    assert any(issue.code == "INVALID_NUMERIC" for issue in report.issues)


def test_analyzer_detects_invalid_risk_level(tmp_path: Path) -> None:
    create_valid_input_files(tmp_path)
    rows = list(csv.DictReader((tmp_path / "approval_requests.csv").open("r", encoding="utf-8")))
    rows[0]["risk_level"] = "EXTREME"
    write_csv(tmp_path / "approval_requests.csv", REQUEST_COLUMNS, rows)

    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=tmp_path)
    report = analyzer.analyze()

    assert report.status == "BLOCKED_BY_INPUT_ERRORS"
    assert any(issue.code == "INVALID_RISK_LEVEL" for issue in report.issues)


def test_analyzer_warns_on_unrecognized_review_status(tmp_path: Path) -> None:
    create_valid_input_files(tmp_path)
    rows = list(csv.DictReader((tmp_path / "approval_steps.csv").open("r", encoding="utf-8")))
    rows[0]["review_status"] = "WAITING_FOR_MANAGER"
    write_csv(tmp_path / "approval_steps.csv", STEP_COLUMNS, rows)

    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=tmp_path)
    report = analyzer.analyze()

    assert report.status == "READY_WITH_WARNINGS"
    assert report.ready_for_analysis is True
    assert any(issue.code == "UNRECOGNIZED_REVIEW_STATUS" for issue in report.issues)


def test_analyzer_detects_incomplete_policy_rule(tmp_path: Path) -> None:
    create_valid_input_files(tmp_path)
    rows = list(csv.DictReader((tmp_path / "approval_policy_rules.csv").open("r", encoding="utf-8")))
    rows[0]["required_roles"] = ""
    rows[0]["verdict_boundary"] = ""
    write_csv(tmp_path / "approval_policy_rules.csv", RULE_COLUMNS, rows)

    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=tmp_path)
    report = analyzer.analyze()

    assert report.status == "BLOCKED_BY_INPUT_ERRORS"
    assert any(issue.code == "MISSING_REQUIRED_ROLES" for issue in report.issues)
    assert any(issue.code == "MISSING_VERDICT_BOUNDARY" for issue in report.issues)


def test_generate_input_quality_report_writes_output(tmp_path: Path) -> None:
    input_dir = tmp_path / "input"
    output_file = tmp_path / "output" / "institutional_approval_input_quality_report.json"
    create_valid_input_files(input_dir)

    report = generate_input_quality_report(input_dir=input_dir, output_file=output_file)

    assert report.status == "READY"
    assert output_file.exists()
    payload = json.loads(output_file.read_text(encoding="utf-8"))
    assert payload["report_id"] == "LOCAL_INSTITUTIONAL_APPROVAL_INPUT_QUALITY_REPORT"
    assert payload["status"] == "READY"
    assert payload["summary"]["files_loaded"] == 5


def test_zero_autonomy_boundary_contains_required_constraints() -> None:
    boundary = build_zero_autonomy_boundary()

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
    assert "validates local CSV input structure only" in boundary["statement"]


def test_report_to_dict_contains_expected_top_level_fields(tmp_path: Path) -> None:
    create_valid_input_files(tmp_path)
    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=tmp_path)
    report = analyzer.analyze()
    payload = report.to_dict()

    assert set(payload) == {
        "report_id",
        "report_version",
        "generated_at",
        "status",
        "ready_for_analysis",
        "summary",
        "files",
        "issues",
        "zero_autonomy_boundary",
    }
    assert payload["status"] == "READY"
    assert payload["issues"] == []
