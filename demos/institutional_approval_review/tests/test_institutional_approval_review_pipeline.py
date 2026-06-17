r"""
Tests for LEO Institutional Approval Review Pipeline v0.1

Canonical Path:
D:\BBS-09-01-2026\leo\runtime\demos\institutional_approval_review\tests\test_institutional_approval_review_pipeline.py

Purpose:
Validate the Institutional Approval Review evidence-generating pipeline without
performing production mutation, workflow execution, legal interpretation,
payment action, staff action, canonical registry mutation, signing, key access,
ERP/HR integration, or external execution.
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

from institutional_approval_review_pipeline import (
    InstitutionalApprovalReviewPipeline,
    build_rule_trace,
    build_zero_autonomy_boundary,
    generate_institutional_approval_evidence_report,
    protocol_for_signal,
    severity_for_request,
    source_records_for,
    split_pipe,
    to_bool,
    utc_now,
)
from institutional_approval_input_quality_report import generate_input_quality_report


EXPECTED_FINDINGS_COUNT = 33
EXPECTED_EVIDENCE_OBJECTS_COUNT = 33
EXPECTED_HIGH_OR_CRITICAL_COUNT = 21


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
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_quality_report(base_dir: Path, ready: bool = True) -> None:
    output_dir = base_dir / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "report_id": "LOCAL_INSTITUTIONAL_APPROVAL_INPUT_QUALITY_REPORT",
        "report_version": "v0.1",
        "status": "READY" if ready else "BLOCKED_BY_INPUT_ERRORS",
        "ready_for_analysis": ready,
        "summary": {
            "files_expected": 5,
            "files_loaded": 5 if ready else 0,
            "error_count": 0 if ready else 1,
            "warning_count": 0,
        },
        "issues": [] if ready else [{"severity": "ERROR", "code": "TEST_BLOCK"}],
        "zero_autonomy_boundary": build_zero_autonomy_boundary(),
    }
    (output_dir / "institutional_approval_input_quality_report.json").write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )


def create_pipeline_fixture(base_dir: Path) -> None:
    input_dir = base_dir / "input"

    write_csv(
        input_dir / "approval_requests.csv",
        REQUEST_COLUMNS,
        [
            {
                "request_id": "REQ-001",
                "request_type": "PROCUREMENT",
                "request_title": "Missing Management Approval",
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
                "notes": "Management step missing",
            },
            {
                "request_id": "REQ-002",
                "request_type": "PROCUREMENT",
                "request_title": "Ready With Pending Legal",
                "request_date": "2026-03-02",
                "requested_by": "Piotr Zielinski",
                "department": "Infrastructure",
                "amount_pln": "240000",
                "risk_level": "HIGH",
                "execution_status": "EXECUTION_READY",
                "handoff_status": "HANDOFF_READY",
                "current_owner": "executive_override",
                "final_decision_state": "APPROVED",
                "requires_legal_review": "TRUE",
                "requires_finance_review": "TRUE",
                "requires_management_review": "TRUE",
                "emergency_override_used": "TRUE",
                "override_reason_present": "FALSE",
                "linked_contract_reference": "CTR-002",
                "linked_budget_reference": "BL-002",
                "notes": "Pending legal and missing override reason",
            },
            {
                "request_id": "REQ-003",
                "request_type": "LEGAL_SERVICE",
                "request_title": "Rejection Followed By Approval",
                "request_date": "2026-03-03",
                "requested_by": "Katarzyna Nowak",
                "department": "Legal",
                "amount_pln": "46000",
                "risk_level": "HIGH",
                "execution_status": "READY_FOR_HANDOFF",
                "handoff_status": "HANDOFF_PENDING",
                "current_owner": "legal_review",
                "final_decision_state": "REJECTED",
                "requires_legal_review": "TRUE",
                "requires_finance_review": "TRUE",
                "requires_management_review": "TRUE",
                "emergency_override_used": "FALSE",
                "override_reason_present": "FALSE",
                "linked_contract_reference": "CTR-003",
                "linked_budget_reference": "BL-003",
                "notes": "Rejected legal then approved board",
            },
            {
                "request_id": "REQ-004",
                "request_type": "PROCUREMENT",
                "request_title": "Legal Review Skipped",
                "request_date": "2026-03-04",
                "requested_by": "Marek Wisniewski",
                "department": "Administration",
                "amount_pln": "99000",
                "risk_level": "MEDIUM",
                "execution_status": "READY_FOR_HANDOFF",
                "handoff_status": "HANDOFF_PENDING",
                "current_owner": "finance_review",
                "final_decision_state": "APPROVED",
                "requires_legal_review": "TRUE",
                "requires_finance_review": "TRUE",
                "requires_management_review": "FALSE",
                "emergency_override_used": "FALSE",
                "override_reason_present": "FALSE",
                "linked_contract_reference": "CTR-004",
                "linked_budget_reference": "BL-004",
                "notes": "Legal review skipped",
            },
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
                "review_note": "Budget approved",
                "is_required": "TRUE",
                "approval_scope": "budget_validation",
                "override_reference": "",
                "review_layer": "finance",
                "decision_owner_confirmed": "TRUE",
            },
            {
                "step_id": "STEP-002",
                "request_id": "REQ-001",
                "step_order": "2",
                "role": "legal_review",
                "reviewer_name": "Tomasz Dabrowski",
                "review_status": "APPROVED",
                "review_date": "2026-03-03",
                "review_note": "Contract approved",
                "is_required": "TRUE",
                "approval_scope": "contractual_review",
                "override_reference": "",
                "review_layer": "legal",
                "decision_owner_confirmed": "TRUE",
            },
            {
                "step_id": "STEP-003",
                "request_id": "REQ-002",
                "step_order": "1",
                "role": "finance_review",
                "reviewer_name": "Anna Kurek",
                "review_status": "APPROVED",
                "review_date": "2026-03-03",
                "review_note": "Emergency budget approved",
                "is_required": "TRUE",
                "approval_scope": "budget_validation",
                "override_reference": "",
                "review_layer": "finance",
                "decision_owner_confirmed": "TRUE",
            },
            {
                "step_id": "STEP-004",
                "request_id": "REQ-002",
                "step_order": "2",
                "role": "legal_review",
                "reviewer_name": "Tomasz Dabrowski",
                "review_status": "PENDING",
                "review_date": "",
                "review_note": "Pending legal review",
                "is_required": "TRUE",
                "approval_scope": "contractual_review",
                "override_reference": "",
                "review_layer": "legal",
                "decision_owner_confirmed": "FALSE",
            },
            {
                "step_id": "STEP-005",
                "request_id": "REQ-002",
                "step_order": "3",
                "role": "executive_override",
                "reviewer_name": "Jan Kowalczyk",
                "review_status": "OVERRIDE_APPROVED",
                "review_date": "2026-03-04",
                "review_note": "Emergency override without reason",
                "is_required": "TRUE",
                "approval_scope": "emergency_override",
                "override_reference": "OVR-001",
                "review_layer": "executive",
                "decision_owner_confirmed": "FALSE",
            },
            {
                "step_id": "STEP-006",
                "request_id": "REQ-003",
                "step_order": "1",
                "role": "legal_review",
                "reviewer_name": "Tomasz Dabrowski",
                "review_status": "REJECTED",
                "review_date": "2026-03-05",
                "review_note": "Legal conflict detected",
                "is_required": "TRUE",
                "approval_scope": "contractual_review",
                "override_reference": "",
                "review_layer": "legal",
                "decision_owner_confirmed": "TRUE",
            },
            {
                "step_id": "STEP-007",
                "request_id": "REQ-003",
                "step_order": "2",
                "role": "management_board",
                "reviewer_name": "Piotr Malinowski",
                "review_status": "APPROVED",
                "review_date": "2026-03-06",
                "review_note": "Continuation approved",
                "is_required": "TRUE",
                "approval_scope": "exceptional_review",
                "override_reference": "",
                "review_layer": "management_board",
                "decision_owner_confirmed": "FALSE",
            },
            {
                "step_id": "STEP-008",
                "request_id": "REQ-004",
                "step_order": "1",
                "role": "finance_review",
                "reviewer_name": "Anna Kurek",
                "review_status": "APPROVED",
                "review_date": "2026-03-07",
                "review_note": "Budget approved",
                "is_required": "TRUE",
                "approval_scope": "budget_validation",
                "override_reference": "",
                "review_layer": "finance",
                "decision_owner_confirmed": "TRUE",
            },
        ],
    )

    write_csv(
        input_dir / "approval_policy_rules.csv",
        RULE_COLUMNS,
        [
            {
                "rule_id": "APR-RULE-003",
                "request_type": "PROCUREMENT",
                "risk_level": "HIGH",
                "amount_threshold_pln": "100000",
                "required_roles": "finance_review|legal_review|management_board",
                "required_order": "finance_review>legal_review>management_board",
                "exception_allowed": "TRUE",
                "exception_requires_reason": "TRUE",
                "exception_requires_documentation": "TRUE",
                "human_readable_rule": "High-value procurement requires finance, legal, and management board review.",
                "verdict_boundary": "This rule creates a human review requirement only.",
            },
            {
                "rule_id": "APR-RULE-010",
                "request_type": "LEGAL_SERVICE",
                "risk_level": "HIGH",
                "amount_threshold_pln": "30000",
                "required_roles": "legal_review|finance_review|management_board",
                "required_order": "legal_review>finance_review>management_board",
                "exception_allowed": "FALSE",
                "exception_requires_reason": "TRUE",
                "exception_requires_documentation": "TRUE",
                "human_readable_rule": "High-risk legal service request requires legal, finance, and management review.",
                "verdict_boundary": "This rule creates a human review requirement only.",
            },
            {
                "rule_id": "APR-RULE-002",
                "request_type": "PROCUREMENT",
                "risk_level": "MEDIUM",
                "amount_threshold_pln": "50000",
                "required_roles": "finance_review|legal_review",
                "required_order": "finance_review>legal_review",
                "exception_allowed": "TRUE",
                "exception_requires_reason": "TRUE",
                "exception_requires_documentation": "TRUE",
                "human_readable_rule": "Medium procurement requires finance and legal review.",
                "verdict_boundary": "This rule creates a human review requirement only.",
            },
        ],
    )

    write_csv(
        input_dir / "approval_role_matrix.csv",
        ROLE_COLUMNS,
        [
            {
                "role": "finance_review",
                "allowed_request_types": "PROCUREMENT|LEGAL_SERVICE",
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
                "request_id": "REQ-002",
                "exception_type": "EMERGENCY_OVERRIDE",
                "approved_by": "Jan Kowalczyk",
                "approved_role": "executive_override",
                "exception_date": "2026-03-04",
                "reason_provided": "FALSE",
                "reason_text": "",
                "documentation_reference": "documents/OVR-001.md",
                "documentation_present": "FALSE",
                "post_event_review_required": "TRUE",
                "post_event_review_status": "PENDING",
                "human_review_required": "TRUE",
                "notes": "Missing reason and documentation",
            }
        ],
    )

    write_quality_report(base_dir, ready=True)


def test_pipeline_generates_real_baseline_from_current_demo_files() -> None:
    pipeline = InstitutionalApprovalReviewPipeline(base_dir=DEMO_DIR)
    result = pipeline.run()
    payload = result.to_dict()

    assert result.input_quality_ready_for_analysis is True
    assert result.input_quality_status == "READY"
    assert payload["summary"]["findings_count"] == EXPECTED_FINDINGS_COUNT
    assert payload["summary"]["evidence_objects_count"] == EXPECTED_EVIDENCE_OBJECTS_COUNT
    assert payload["summary"]["high_or_critical_findings_count"] == EXPECTED_HIGH_OR_CRITICAL_COUNT
    assert payload["summary"]["autonomous_actions"] == 0
    assert len(payload["findings"]) == EXPECTED_FINDINGS_COUNT
    assert len(payload["evidence_objects"]) == EXPECTED_EVIDENCE_OBJECTS_COUNT


def test_pipeline_generates_expected_signal_families_from_current_demo_files() -> None:
    pipeline = InstitutionalApprovalReviewPipeline(base_dir=DEMO_DIR)
    result = pipeline.run()
    signal_families = result.to_dict()["summary"]["signal_families"]

    assert signal_families["missing_required_approval"] >= 1
    assert signal_families["execution_ready_with_pending_review"] >= 1
    assert signal_families["unresolved_rejection_followed_by_approval"] >= 1
    assert signal_families["missing_decision_owner"] >= 1
    assert signal_families["emergency_override_without_reason"] >= 1
    assert signal_families["exception_without_documentation"] >= 1
    assert signal_families["legal_review_missing_for_contractual_action"] >= 1


def test_pipeline_preserves_zero_autonomy_boundary_from_current_demo_files() -> None:
    pipeline = InstitutionalApprovalReviewPipeline(base_dir=DEMO_DIR)
    result = pipeline.run()
    payload = result.to_dict()
    boundary = payload["zero_autonomy_boundary"]

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

    for finding in payload["findings"]:
        assert finding["zero_autonomy_boundary"]["no_external_execution"] is True
        assert "human-review signal only" in finding["verdict_boundary"]


def test_pipeline_returns_empty_result_when_input_quality_not_ready(tmp_path: Path) -> None:
    create_pipeline_fixture(tmp_path)
    write_quality_report(tmp_path, ready=False)
    pipeline = InstitutionalApprovalReviewPipeline(base_dir=tmp_path)

    result = pipeline.run()
    payload = result.to_dict()

    assert result.input_quality_ready_for_analysis is False
    assert result.input_quality_status == "BLOCKED_BY_INPUT_ERRORS"
    assert payload["summary"]["findings_count"] == 0
    assert payload["summary"]["evidence_objects_count"] == 0
    assert payload["summary"]["autonomous_actions"] == 0


def test_pipeline_detects_expected_fixture_signals(tmp_path: Path) -> None:
    create_pipeline_fixture(tmp_path)
    pipeline = InstitutionalApprovalReviewPipeline(base_dir=tmp_path)

    result = pipeline.run()
    payload = result.to_dict()
    families = {finding["signal_family"] for finding in payload["findings"]}

    assert "missing_required_approval" in families
    assert "execution_ready_with_pending_review" in families
    assert "unresolved_rejection_followed_by_approval" in families
    assert "emergency_override_without_reason" in families
    assert "exception_without_documentation" in families
    assert "legal_review_missing_for_contractual_action" in families
    assert payload["summary"]["autonomous_actions"] == 0


def test_pipeline_fixture_findings_have_evidence_objects(tmp_path: Path) -> None:
    create_pipeline_fixture(tmp_path)
    pipeline = InstitutionalApprovalReviewPipeline(base_dir=tmp_path)

    result = pipeline.run()
    payload = result.to_dict()
    evidence_ids = {evidence["evidence_id"] for evidence in payload["evidence_objects"]}

    assert payload["summary"]["findings_count"] == payload["summary"]["evidence_objects_count"]
    for finding in payload["findings"]:
        assert finding["evidence_ids"]
        assert finding["evidence_ids"][0] in evidence_ids
        assert finding["rule_trace"]["source_rule_file"] == "approval_policy_rules.csv"
        assert finding["responsible_review_layer"]


def test_generate_institutional_approval_evidence_report_writes_output(tmp_path: Path) -> None:
    create_pipeline_fixture(tmp_path)
    output_file = tmp_path / "output" / "institutional_approval_evidence_report.json"

    result = generate_institutional_approval_evidence_report(output_file=output_file)

    assert output_file.exists()
    payload = json.loads(output_file.read_text(encoding="utf-8"))
    assert payload["report_id"] == "LOCAL_INSTITUTIONAL_APPROVAL_EVIDENCE_REPORT"
    assert payload["summary"]["autonomous_actions"] == 0
    assert result.to_dict()["report_id"] == "LOCAL_INSTITUTIONAL_APPROVAL_EVIDENCE_REPORT"


def test_split_pipe_ignores_empty_parts() -> None:
    assert split_pipe("finance_review|legal_review||management_board|") == {
        "finance_review",
        "legal_review",
        "management_board",
    }


def test_to_bool_accepts_true_values_only() -> None:
    assert to_bool("TRUE") is True
    assert to_bool("true") is True
    assert to_bool(True) is True
    assert to_bool("FALSE") is False
    assert to_bool("yes") is False
    assert to_bool(None) is False


def test_severity_for_request_uses_valid_risk_level() -> None:
    assert severity_for_request({"risk_level": "CRITICAL"}) == "CRITICAL"
    assert severity_for_request({"risk_level": "HIGH"}) == "HIGH"
    assert severity_for_request({"risk_level": "UNKNOWN"}, default="MEDIUM") == "MEDIUM"


def test_source_records_for_combines_request_steps_and_exceptions() -> None:
    records = source_records_for(
        {"request_id": "REQ-001"},
        [{"step_id": "STEP-001"}],
        [{"exception_id": "OVR-001"}],
    )

    assert records == [
        "approval_requests:REQ-001",
        "approval_steps:STEP-001",
        "approval_exception_register:OVR-001",
    ]


def test_protocol_for_signal_maps_known_signals() -> None:
    assert protocol_for_signal("missing_required_approval") == "MISSING_REQUIRED_APPROVAL_PROTOCOL_v0.1.md"
    assert protocol_for_signal("unresolved_rejection_followed_by_approval") == "UNRESOLVED_REJECTION_PROTOCOL_v0.1.md"
    assert protocol_for_signal("unknown_signal") == "INSTITUTIONAL_APPROVAL_REVIEW_GENERAL_PROTOCOL_v0.1.md"


def test_build_rule_trace_uses_matched_rule() -> None:
    trace = build_rule_trace(
        [
            {
                "rule_id": "APR-RULE-003",
                "human_readable_rule": "High-value procurement requires review.",
                "verdict_boundary": "Human review only.",
            }
        ],
        "missing_required_approval",
    )

    assert trace["source_rule_id"] == "APR-RULE-003"
    assert trace["source_rule_file"] == "approval_policy_rules.csv"
    assert trace["protocol_reference"] == "MISSING_REQUIRED_APPROVAL_PROTOCOL_v0.1.md"
    assert trace["verdict_boundary"] == "Human review only."


def test_build_rule_trace_falls_back_to_general_rule() -> None:
    trace = build_rule_trace([], "missing_decision_owner")

    assert trace["source_rule_id"] == "IAR-GENERAL-CONTINUITY-RULE"
    assert trace["protocol_reference"] == "MISSING_DECISION_OWNER_PROTOCOL_v0.1.md"
    assert "human review" in trace["human_readable_rule"].lower()


def test_utc_now_returns_z_timestamp() -> None:
    timestamp = utc_now()

    assert timestamp.endswith("Z")
    assert "T" in timestamp
