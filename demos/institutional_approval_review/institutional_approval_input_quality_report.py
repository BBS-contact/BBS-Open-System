r"""
LEO Institutional Approval Review Input Quality Report v0.1

Public demo path:
demos/institutional_approval_review/institutional_approval_input_quality_report.py

Purpose:
Validate the local CSV input files for the Institutional Approval Review demo slice
and generate a structural input quality report.

This module checks only whether local input data is structurally usable for review.

This module does NOT:
- approve decisions,
- reject decisions,
- block operations,
- punish staff,
- issue legal conclusions,
- issue donor compliance conclusions,
- execute workflow transitions,
- mutate production approval records,
- mutate canonical registries,
- access signing keys,
- sign documents,
- connect to ERP systems,
- connect to HR systems,
- or perform external execution.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from datetime import datetime, UTC
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "institutional_approval_input_quality_report.json"


REQUIRED_FILES: dict[str, str] = {
    "approval_requests": "approval_requests.csv",
    "approval_steps": "approval_steps.csv",
    "approval_policy_rules": "approval_policy_rules.csv",
    "approval_role_matrix": "approval_role_matrix.csv",
    "approval_exception_register": "approval_exception_register.csv",
}


REQUIRED_COLUMNS: dict[str, set[str]] = {
    "approval_requests": {
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
    },
    "approval_steps": {
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
    },
    "approval_policy_rules": {
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
    },
    "approval_role_matrix": {
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
    },
    "approval_exception_register": {
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
    },
}


BOOLEAN_FIELDS: dict[str, set[str]] = {
    "approval_requests": {
        "requires_legal_review",
        "requires_finance_review",
        "requires_management_review",
        "emergency_override_used",
        "override_reason_present",
    },
    "approval_steps": {
        "is_required",
        "decision_owner_confirmed",
    },
    "approval_policy_rules": {
        "exception_allowed",
        "exception_requires_reason",
        "exception_requires_documentation",
    },
    "approval_role_matrix": {
        "can_override",
        "requires_note",
        "requires_secondary_review",
        "active_role",
    },
    "approval_exception_register": {
        "reason_provided",
        "documentation_present",
        "post_event_review_required",
        "human_review_required",
    },
}


NUMERIC_FIELDS: dict[str, set[str]] = {
    "approval_requests": {"amount_pln"},
    "approval_steps": {"step_order"},
    "approval_policy_rules": {"amount_threshold_pln"},
    "approval_role_matrix": {"approval_limit_pln"},
}


DATE_FIELDS: dict[str, set[str]] = {
    "approval_requests": {"request_date"},
    "approval_steps": {"review_date"},
    "approval_exception_register": {"exception_date"},
}


ID_FIELDS: dict[str, str] = {
    "approval_requests": "request_id",
    "approval_steps": "step_id",
    "approval_policy_rules": "rule_id",
    "approval_role_matrix": "role",
    "approval_exception_register": "exception_id",
}


VALID_BOOLEAN_VALUES = {"TRUE", "FALSE"}
VALID_RISK_LEVELS = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
VALID_REVIEW_STATUSES = {
    "APPROVED",
    "PENDING",
    "REJECTED",
    "ESCALATED",
    "NEEDS_REPLACEMENT",
    "OVERRIDE_APPROVED",
}


@dataclass
class InputQualityIssue:
    """Represents a structural input quality issue."""

    severity: str
    source: str
    code: str
    message: str
    row_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "severity": self.severity,
            "source": self.source,
            "code": self.code,
            "message": self.message,
            "row_id": self.row_id,
        }


@dataclass
class InputQualityReport:
    """Represents the generated input quality report."""

    report_id: str
    report_version: str
    generated_at: str
    status: str
    ready_for_analysis: bool
    summary: dict[str, Any]
    files: dict[str, Any]
    issues: list[InputQualityIssue] = field(default_factory=list)
    zero_autonomy_boundary: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "report_id": self.report_id,
            "report_version": self.report_version,
            "generated_at": self.generated_at,
            "status": self.status,
            "ready_for_analysis": self.ready_for_analysis,
            "summary": self.summary,
            "files": self.files,
            "issues": [issue.to_dict() for issue in self.issues],
            "zero_autonomy_boundary": self.zero_autonomy_boundary,
        }


class InstitutionalApprovalInputQualityAnalyzer:
    """Analyzes local Institutional Approval Review CSV input quality."""

    def __init__(self, input_dir: Path = INPUT_DIR) -> None:
        self.input_dir = input_dir
        self.issues: list[InputQualityIssue] = []
        self.loaded_rows: dict[str, list[dict[str, str]]] = {}
        self.file_metadata: dict[str, Any] = {}

    def analyze(self) -> InputQualityReport:
        """Run all input quality checks and build a report."""

        self._load_all_files()
        self._validate_required_columns()
        self._validate_duplicate_ids()
        self._validate_references()
        self._validate_dates()
        self._validate_booleans()
        self._validate_numeric_fields()
        self._validate_domain_values()
        self._validate_policy_rule_completeness()

        error_count = sum(1 for issue in self.issues if issue.severity == "ERROR")
        warning_count = sum(1 for issue in self.issues if issue.severity == "WARNING")

        if error_count > 0:
            status = "BLOCKED_BY_INPUT_ERRORS"
            ready_for_analysis = False
        elif warning_count > 0:
            status = "READY_WITH_WARNINGS"
            ready_for_analysis = True
        else:
            status = "READY"
            ready_for_analysis = True

        summary = {
            "files_expected": len(REQUIRED_FILES),
            "files_loaded": sum(1 for metadata in self.file_metadata.values() if metadata.get("exists") is True),
            "approval_requests_count": len(self.loaded_rows.get("approval_requests", [])),
            "approval_steps_count": len(self.loaded_rows.get("approval_steps", [])),
            "approval_policy_rules_count": len(self.loaded_rows.get("approval_policy_rules", [])),
            "approval_role_matrix_count": len(self.loaded_rows.get("approval_role_matrix", [])),
            "approval_exception_register_count": len(self.loaded_rows.get("approval_exception_register", [])),
            "error_count": error_count,
            "warning_count": warning_count,
        }

        return InputQualityReport(
            report_id="LOCAL_INSTITUTIONAL_APPROVAL_INPUT_QUALITY_REPORT",
            report_version="v0.1",
            generated_at=datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
            status=status,
            ready_for_analysis=ready_for_analysis,
            summary=summary,
            files=self.file_metadata,
            issues=self.issues,
            zero_autonomy_boundary=build_zero_autonomy_boundary(),
        )

    def _load_all_files(self) -> None:
        for label, filename in REQUIRED_FILES.items():
            path = self.input_dir / filename
            if not path.exists():
                self.file_metadata[label] = {
                    "path": str(path),
                    "exists": False,
                    "rows_loaded": 0,
                }
                self._add_issue("ERROR", label, "MISSING_REQUIRED_FILE", f"Required input file is missing: {path}")
                self.loaded_rows[label] = []
                continue

            try:
                with path.open("r", encoding="utf-8-sig", newline="") as file:
                    reader = csv.DictReader(file)
                    rows = [dict(row) for row in reader]

                self.loaded_rows[label] = rows
                self.file_metadata[label] = {
                    "path": str(path),
                    "exists": True,
                    "rows_loaded": len(rows),
                    "columns": list(rows[0].keys()) if rows else list(reader.fieldnames or []),
                }

                if len(rows) == 0:
                    self._add_issue("WARNING", label, "EMPTY_FILE", f"Input file has no data rows: {path}")

            except OSError as exc:
                self.file_metadata[label] = {
                    "path": str(path),
                    "exists": True,
                    "rows_loaded": 0,
                    "read_error": str(exc),
                }
                self.loaded_rows[label] = []
                self._add_issue("ERROR", label, "FILE_READ_ERROR", f"Could not read input file {path}: {exc}")

    def _validate_required_columns(self) -> None:
        for label, required_columns in REQUIRED_COLUMNS.items():
            metadata = self.file_metadata.get(label, {})
            if not metadata.get("exists"):
                continue

            actual_columns = set(metadata.get("columns", []))
            missing_columns = sorted(required_columns - actual_columns)

            for column in missing_columns:
                self._add_issue(
                    "ERROR",
                    label,
                    "MISSING_REQUIRED_COLUMN",
                    f"Missing required column '{column}' in {REQUIRED_FILES[label]}",
                )

    def _validate_duplicate_ids(self) -> None:
        for label, id_field in ID_FIELDS.items():
            seen: set[str] = set()
            duplicates: set[str] = set()
            for row in self.loaded_rows.get(label, []):
                row_id = row.get(id_field, "").strip()
                if not row_id:
                    self._add_issue("ERROR", label, "MISSING_ID", f"Missing {id_field} value.")
                    continue
                if row_id in seen:
                    duplicates.add(row_id)
                seen.add(row_id)

            for duplicate in sorted(duplicates):
                self._add_issue("ERROR", label, "DUPLICATE_ID", f"Duplicate {id_field}: {duplicate}", duplicate)

    def _validate_references(self) -> None:
        request_ids = {row.get("request_id", "").strip() for row in self.loaded_rows.get("approval_requests", [])}
        request_ids.discard("")

        for source in ["approval_steps", "approval_exception_register"]:
            for row in self.loaded_rows.get(source, []):
                request_id = row.get("request_id", "").strip()
                row_id = row.get(ID_FIELDS[source], "").strip() or None
                if not request_id:
                    self._add_issue("ERROR", source, "MISSING_REQUEST_REFERENCE", "Missing request_id reference.", row_id)
                elif request_id not in request_ids:
                    self._add_issue("ERROR", source, "UNKNOWN_REQUEST_REFERENCE", f"Unknown request_id reference: {request_id}", row_id)

    def _validate_dates(self) -> None:
        for label, fields in DATE_FIELDS.items():
            for row in self.loaded_rows.get(label, []):
                row_id = row.get(ID_FIELDS.get(label, ""), "").strip() or None
                for field_name in fields:
                    value = row.get(field_name, "").strip()
                    if not value:
                        if label == "approval_steps" and row.get("review_status", "").strip() == "PENDING":
                            continue
                        self._add_issue("WARNING", label, "MISSING_DATE", f"Missing date in field '{field_name}'.", row_id)
                        continue
                    try:
                        datetime.strptime(value, "%Y-%m-%d")
                    except ValueError:
                        self._add_issue("ERROR", label, "INVALID_DATE", f"Invalid date '{value}' in field '{field_name}'.", row_id)

    def _validate_booleans(self) -> None:
        for label, fields in BOOLEAN_FIELDS.items():
            for row in self.loaded_rows.get(label, []):
                row_id = row.get(ID_FIELDS.get(label, ""), "").strip() or None
                for field_name in fields:
                    value = row.get(field_name, "").strip().upper()
                    if value not in VALID_BOOLEAN_VALUES:
                        self._add_issue("ERROR", label, "INVALID_BOOLEAN", f"Invalid boolean '{row.get(field_name, '')}' in field '{field_name}'.", row_id)

    def _validate_numeric_fields(self) -> None:
        for label, fields in NUMERIC_FIELDS.items():
            for row in self.loaded_rows.get(label, []):
                row_id = row.get(ID_FIELDS.get(label, ""), "").strip() or None
                for field_name in fields:
                    value = row.get(field_name, "").strip()
                    try:
                        float(value)
                    except ValueError:
                        self._add_issue("ERROR", label, "INVALID_NUMERIC", f"Invalid numeric value '{value}' in field '{field_name}'.", row_id)

    def _validate_domain_values(self) -> None:
        for row in self.loaded_rows.get("approval_requests", []):
            row_id = row.get("request_id", "").strip() or None
            risk_level = row.get("risk_level", "").strip().upper()
            if risk_level not in VALID_RISK_LEVELS:
                self._add_issue("ERROR", "approval_requests", "INVALID_RISK_LEVEL", f"Invalid risk_level: {risk_level}", row_id)

        for row in self.loaded_rows.get("approval_policy_rules", []):
            row_id = row.get("rule_id", "").strip() or None
            risk_level = row.get("risk_level", "").strip().upper()
            if risk_level not in VALID_RISK_LEVELS:
                self._add_issue("ERROR", "approval_policy_rules", "INVALID_RISK_LEVEL", f"Invalid risk_level: {risk_level}", row_id)

        for row in self.loaded_rows.get("approval_steps", []):
            row_id = row.get("step_id", "").strip() or None
            review_status = row.get("review_status", "").strip().upper()
            if review_status not in VALID_REVIEW_STATUSES:
                self._add_issue("WARNING", "approval_steps", "UNRECOGNIZED_REVIEW_STATUS", f"Unrecognized review_status: {review_status}", row_id)

    def _validate_policy_rule_completeness(self) -> None:
        for row in self.loaded_rows.get("approval_policy_rules", []):
            row_id = row.get("rule_id", "").strip() or None
            required_roles = row.get("required_roles", "").strip()
            required_order = row.get("required_order", "").strip()
            human_rule = row.get("human_readable_rule", "").strip()
            verdict_boundary = row.get("verdict_boundary", "").strip()

            if not required_roles:
                self._add_issue("ERROR", "approval_policy_rules", "MISSING_REQUIRED_ROLES", "Policy rule has no required_roles.", row_id)
            if not required_order:
                self._add_issue("WARNING", "approval_policy_rules", "MISSING_REQUIRED_ORDER", "Policy rule has no required_order.", row_id)
            if not human_rule:
                self._add_issue("WARNING", "approval_policy_rules", "MISSING_HUMAN_READABLE_RULE", "Policy rule has no human_readable_rule.", row_id)
            if not verdict_boundary:
                self._add_issue("ERROR", "approval_policy_rules", "MISSING_VERDICT_BOUNDARY", "Policy rule has no verdict_boundary.", row_id)

    def _add_issue(self, severity: str, source: str, code: str, message: str, row_id: str | None = None) -> None:
        self.issues.append(
            InputQualityIssue(
                severity=severity,
                source=source,
                code=code,
                message=message,
                row_id=row_id,
            )
        )


def build_zero_autonomy_boundary() -> dict[str, Any]:
    """Return the zero-autonomy boundary for this input quality report."""

    return {
        "no_autonomous_approval": True,
        "no_autonomous_rejection": True,
        "no_payment_blocking": True,
        "no_staff_punishment": True,
        "no_legal_conclusion": True,
        "no_donor_compliance_conclusion": True,
        "no_board_decision": True,
        "no_production_mutation": True,
        "no_canonical_registry_mutation": True,
        "no_signing_or_key_access": True,
        "no_external_execution": True,
        "statement": "This report validates local CSV input structure only. It does not approve, reject, block, punish, sign, mutate, or execute institutional actions.",
    }


def generate_input_quality_report(
    input_dir: Path = INPUT_DIR,
    output_file: Path = OUTPUT_FILE,
) -> InputQualityReport:
    """Generate and save the Institutional Approval input quality report."""

    analyzer = InstitutionalApprovalInputQualityAnalyzer(input_dir=input_dir)
    report = analyzer.analyze()

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(
        json.dumps(report.to_dict(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return report


def main() -> None:
    """Generate the report and print a concise summary."""

    report = generate_input_quality_report()
    summary = report.summary

    print("=" * 72)
    print("LEO INSTITUTIONAL APPROVAL INPUT QUALITY REPORT v0.1")
    print("=" * 72)
    print(f"STATUS: {report.status}")
    print(f"READY FOR ANALYSIS: {report.ready_for_analysis}")
    print(f"FILES LOADED: {summary['files_loaded']} / {summary['files_expected']}")
    print(f"APPROVAL REQUESTS: {summary['approval_requests_count']}")
    print(f"APPROVAL STEPS: {summary['approval_steps_count']}")
    print(f"POLICY RULES: {summary['approval_policy_rules_count']}")
    print(f"ROLE MATRIX ROWS: {summary['approval_role_matrix_count']}")
    print(f"EXCEPTION RECORDS: {summary['approval_exception_register_count']}")
    print(f"ERRORS: {summary['error_count']}")
    print(f"WARNINGS: {summary['warning_count']}")
    print(f"OUTPUT: {OUTPUT_FILE}")
    print("=" * 72)


if __name__ == "__main__":
    main()
