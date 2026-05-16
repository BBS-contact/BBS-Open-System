r"""
LEO Institutional Approval Evidence Report Validator v0.1

Canonical Path:
D:\BBS-09-01-2026\leo\runtime\demos\institutional_approval_review\institutional_approval_evidence_report_validator.py

Purpose:
Validate the generated Institutional Approval Review evidence report before dashboard,
export package, or presentation work continues.

This validator checks:
- report structure,
- summary consistency,
- finding/evidence parity,
- duplicate IDs,
- evidence linkage integrity,
- rule trace presence,
- allowed severity values,
- allowed signal family values,
- zero-autonomy boundaries,
- and autonomous_actions == 0.

This validator does NOT:
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

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
EVIDENCE_REPORT_FILE = OUTPUT_DIR / "institutional_approval_evidence_report.json"
VALIDATION_OUTPUT_FILE = OUTPUT_DIR / "institutional_approval_evidence_report_validation.json"


EXPECTED_REPORT_ID = "LOCAL_INSTITUTIONAL_APPROVAL_EVIDENCE_REPORT"
EXPECTED_REPORT_VERSION = "v0.1"
EXPECTED_FINDINGS_COUNT = 33
EXPECTED_EVIDENCE_OBJECTS_COUNT = 33
EXPECTED_HIGH_OR_CRITICAL_COUNT = 21


VALID_STATUSES = {"VALID", "VALID_WITH_WARNINGS", "INVALID"}
VALID_SEVERITIES = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
VALID_SIGNAL_FAMILIES = {
    "missing_required_approval",
    "execution_ready_with_pending_review",
    "unresolved_rejection_followed_by_approval",
    "missing_decision_owner",
    "emergency_override_without_reason",
    "exception_without_documentation",
    "legal_review_missing_for_contractual_action",
}


REQUIRED_REPORT_FIELDS = {
    "report_id",
    "report_version",
    "generated_at",
    "source_input_quality_report",
    "input_quality_status",
    "input_quality_ready_for_analysis",
    "summary",
    "findings",
    "evidence_objects",
    "zero_autonomy_boundary",
}


REQUIRED_SUMMARY_FIELDS = {
    "findings_count",
    "evidence_objects_count",
    "high_or_critical_findings_count",
    "signal_families",
    "autonomous_actions",
}


REQUIRED_FINDING_FIELDS = {
    "id",
    "request_id",
    "title",
    "severity",
    "signal_family",
    "detected_signal",
    "why_it_matters",
    "reviewer_question",
    "next_action",
    "responsible_review_layer",
    "rule_trace",
    "evidence_ids",
    "verdict_boundary",
    "zero_autonomy_boundary",
}


REQUIRED_RULE_TRACE_FIELDS = {
    "source_rule_id",
    "source_rule_name",
    "source_rule_file",
    "protocol_reference",
    "human_readable_rule",
    "verdict_boundary",
}


REQUIRED_EVIDENCE_FIELDS = {
    "evidence_id",
    "finding_id",
    "request_id",
    "source_records",
    "signal_family",
    "evidence_summary",
    "data_points",
    "created_at",
    "boundary_statement",
}


REQUIRED_ZERO_AUTONOMY_TRUE_FIELDS = {
    "no_autonomous_approval",
    "no_autonomous_rejection",
    "no_payment_blocking",
    "no_staff_punishment",
    "no_legal_conclusion",
    "no_donor_compliance_conclusion",
    "no_board_decision",
    "no_production_mutation",
    "no_canonical_registry_mutation",
    "no_signing_or_key_access",
    "no_external_execution",
}


@dataclass(frozen=True)
class ValidationIssue:
    """Evidence report validation issue."""

    severity: str
    code: str
    message: str
    item_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
            "item_id": self.item_id,
        }


@dataclass
class ValidationResult:
    """Evidence report validation result."""

    status: str
    is_valid: bool
    report_path: str
    summary: dict[str, Any]
    issues: list[ValidationIssue] = field(default_factory=list)
    zero_autonomy_boundary: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "is_valid": self.is_valid,
            "report_path": self.report_path,
            "summary": self.summary,
            "issues": [issue.to_dict() for issue in self.issues],
            "zero_autonomy_boundary": self.zero_autonomy_boundary,
        }


class InstitutionalApprovalEvidenceReportValidator:
    """Validator for Institutional Approval Review evidence reports."""

    def __init__(self, report_path: Path = EVIDENCE_REPORT_FILE) -> None:
        self.report_path = report_path
        self.issues: list[ValidationIssue] = []
        self.report: dict[str, Any] | None = None

    def validate(self) -> ValidationResult:
        """Run all validation checks."""

        self.report = self._load_report()
        if self.report is None:
            return self._build_result()

        self._validate_top_level_structure()
        self._validate_report_identity()
        self._validate_summary_structure()
        self._validate_summary_consistency()
        self._validate_findings_structure()
        self._validate_evidence_structure()
        self._validate_duplicate_ids()
        self._validate_evidence_links()
        self._validate_signal_family_summary()
        self._validate_zero_autonomy_boundary(self.report.get("zero_autonomy_boundary"), "report")
        self._validate_finding_zero_autonomy_boundaries()

        return self._build_result()

    def _load_report(self) -> dict[str, Any] | None:
        if not self.report_path.exists():
            self._add_issue("ERROR", "REPORT_FILE_MISSING", f"Evidence report file is missing: {self.report_path}")
            return None

        try:
            payload = json.loads(self.report_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            self._add_issue("ERROR", "INVALID_JSON", f"Evidence report is not valid JSON: {exc}")
            return None

        if not isinstance(payload, dict):
            self._add_issue("ERROR", "INVALID_JSON_ROOT", "Evidence report JSON root must be an object.")
            return None

        return payload

    def _validate_top_level_structure(self) -> None:
        assert self.report is not None
        missing = sorted(REQUIRED_REPORT_FIELDS - set(self.report))
        for field_name in missing:
            self._add_issue("ERROR", "MISSING_TOP_LEVEL_FIELD", f"Missing top-level field: {field_name}")

    def _validate_report_identity(self) -> None:
        assert self.report is not None
        if self.report.get("report_id") != EXPECTED_REPORT_ID:
            self._add_issue("ERROR", "UNEXPECTED_REPORT_ID", f"Unexpected report_id: {self.report.get('report_id')}")

        if self.report.get("report_version") != EXPECTED_REPORT_VERSION:
            self._add_issue("ERROR", "UNEXPECTED_REPORT_VERSION", f"Unexpected report_version: {self.report.get('report_version')}")

        if self.report.get("input_quality_ready_for_analysis") is not True:
            self._add_issue("ERROR", "INPUT_QUALITY_NOT_READY", "Evidence report must be generated from ready input quality state.")

    def _validate_summary_structure(self) -> None:
        assert self.report is not None
        summary = self.report.get("summary")
        if not isinstance(summary, dict):
            self._add_issue("ERROR", "INVALID_SUMMARY", "summary must be an object.")
            return

        missing = sorted(REQUIRED_SUMMARY_FIELDS - set(summary))
        for field_name in missing:
            self._add_issue("ERROR", "MISSING_SUMMARY_FIELD", f"Missing summary field: {field_name}")

    def _validate_summary_consistency(self) -> None:
        assert self.report is not None
        summary = self.report.get("summary", {})
        findings = self.report.get("findings", [])
        evidence_objects = self.report.get("evidence_objects", [])

        if not isinstance(summary, dict) or not isinstance(findings, list) or not isinstance(evidence_objects, list):
            return

        expected_values = {
            "findings_count": EXPECTED_FINDINGS_COUNT,
            "evidence_objects_count": EXPECTED_EVIDENCE_OBJECTS_COUNT,
            "high_or_critical_findings_count": EXPECTED_HIGH_OR_CRITICAL_COUNT,
            "autonomous_actions": 0,
        }

        for field_name, expected in expected_values.items():
            actual = summary.get(field_name)
            if actual != expected:
                self._add_issue("ERROR", "UNEXPECTED_SUMMARY_VALUE", f"Expected {field_name}={expected}, received {actual}.")

        if summary.get("findings_count") != len(findings):
            self._add_issue("ERROR", "FINDINGS_COUNT_MISMATCH", f"summary.findings_count={summary.get('findings_count')} but findings length={len(findings)}.")

        if summary.get("evidence_objects_count") != len(evidence_objects):
            self._add_issue("ERROR", "EVIDENCE_COUNT_MISMATCH", f"summary.evidence_objects_count={summary.get('evidence_objects_count')} but evidence length={len(evidence_objects)}.")

        actual_high_critical = sum(
            1 for finding in findings
            if isinstance(finding, dict) and finding.get("severity") in {"HIGH", "CRITICAL"}
        )
        if summary.get("high_or_critical_findings_count") != actual_high_critical:
            self._add_issue(
                "ERROR",
                "HIGH_CRITICAL_COUNT_MISMATCH",
                "summary.high_or_critical_findings_count does not match findings severity count.",
            )

    def _validate_findings_structure(self) -> None:
        assert self.report is not None
        findings = self.report.get("findings")
        if not isinstance(findings, list):
            self._add_issue("ERROR", "INVALID_FINDINGS", "findings must be a list.")
            return

        for finding in findings:
            if not isinstance(finding, dict):
                self._add_issue("ERROR", "INVALID_FINDING_OBJECT", "Each finding must be an object.")
                continue

            finding_id = str(finding.get("id", "UNKNOWN_FINDING"))
            missing = sorted(REQUIRED_FINDING_FIELDS - set(finding))
            for field_name in missing:
                self._add_issue("ERROR", "MISSING_FINDING_FIELD", f"Missing finding field: {field_name}", finding_id)

            severity = finding.get("severity")
            if severity not in VALID_SEVERITIES:
                self._add_issue("ERROR", "INVALID_SEVERITY", f"Invalid severity: {severity}", finding_id)

            signal_family = finding.get("signal_family")
            if signal_family not in VALID_SIGNAL_FAMILIES:
                self._add_issue("ERROR", "INVALID_SIGNAL_FAMILY", f"Invalid signal_family: {signal_family}", finding_id)

            responsible_layers = finding.get("responsible_review_layer")
            if not isinstance(responsible_layers, list) or not responsible_layers:
                self._add_issue("ERROR", "EMPTY_RESPONSIBLE_REVIEW_LAYER", "responsible_review_layer must be a non-empty list.", finding_id)

            evidence_ids = finding.get("evidence_ids")
            if not isinstance(evidence_ids, list) or not evidence_ids:
                self._add_issue("ERROR", "EMPTY_EVIDENCE_IDS", "evidence_ids must be a non-empty list.", finding_id)

            verdict_boundary = finding.get("verdict_boundary", "")
            if "does not approve" not in str(verdict_boundary):
                self._add_issue("ERROR", "WEAK_VERDICT_BOUNDARY", "verdict_boundary must explicitly prevent approval/execution interpretation.", finding_id)

            self._validate_rule_trace(finding.get("rule_trace"), finding_id)

    def _validate_rule_trace(self, rule_trace: Any, finding_id: str) -> None:
        if not isinstance(rule_trace, dict):
            self._add_issue("ERROR", "INVALID_RULE_TRACE", "rule_trace must be an object.", finding_id)
            return

        missing = sorted(REQUIRED_RULE_TRACE_FIELDS - set(rule_trace))
        for field_name in missing:
            self._add_issue("ERROR", "MISSING_RULE_TRACE_FIELD", f"Missing rule_trace field: {field_name}", finding_id)

        source_rule_file = rule_trace.get("source_rule_file")
        if source_rule_file != "approval_policy_rules.csv":
            self._add_issue("WARNING", "UNEXPECTED_RULE_SOURCE", f"Unexpected source_rule_file: {source_rule_file}", finding_id)

        protocol_reference = str(rule_trace.get("protocol_reference", ""))
        if not protocol_reference.endswith(".md"):
            self._add_issue("WARNING", "PROTOCOL_REFERENCE_NOT_MARKDOWN", f"protocol_reference should point to a markdown protocol file: {protocol_reference}", finding_id)

    def _validate_evidence_structure(self) -> None:
        assert self.report is not None
        evidence_objects = self.report.get("evidence_objects")
        if not isinstance(evidence_objects, list):
            self._add_issue("ERROR", "INVALID_EVIDENCE_OBJECTS", "evidence_objects must be a list.")
            return

        for evidence in evidence_objects:
            if not isinstance(evidence, dict):
                self._add_issue("ERROR", "INVALID_EVIDENCE_OBJECT", "Each evidence object must be an object.")
                continue

            evidence_id = str(evidence.get("evidence_id", "UNKNOWN_EVIDENCE"))
            missing = sorted(REQUIRED_EVIDENCE_FIELDS - set(evidence))
            for field_name in missing:
                self._add_issue("ERROR", "MISSING_EVIDENCE_FIELD", f"Missing evidence field: {field_name}", evidence_id)

            source_records = evidence.get("source_records")
            if not isinstance(source_records, list) or not source_records:
                self._add_issue("ERROR", "EMPTY_SOURCE_RECORDS", "source_records must be a non-empty list.", evidence_id)

            boundary = str(evidence.get("boundary_statement", ""))
            if "does not mutate" not in boundary:
                self._add_issue("ERROR", "WEAK_EVIDENCE_BOUNDARY", "boundary_statement must explicitly prevent mutation/execution interpretation.", evidence_id)

            signal_family = evidence.get("signal_family")
            if signal_family not in VALID_SIGNAL_FAMILIES:
                self._add_issue("ERROR", "INVALID_EVIDENCE_SIGNAL_FAMILY", f"Invalid evidence signal_family: {signal_family}", evidence_id)

    def _validate_duplicate_ids(self) -> None:
        assert self.report is not None
        findings = self.report.get("findings", [])
        evidence_objects = self.report.get("evidence_objects", [])

        self._detect_duplicates([finding.get("id") for finding in findings if isinstance(finding, dict)], "DUPLICATE_FINDING_ID")
        self._detect_duplicates([evidence.get("evidence_id") for evidence in evidence_objects if isinstance(evidence, dict)], "DUPLICATE_EVIDENCE_ID")

    def _detect_duplicates(self, values: list[Any], code: str) -> None:
        seen: set[str] = set()
        duplicates: set[str] = set()
        for value in values:
            value_text = str(value)
            if value_text in seen:
                duplicates.add(value_text)
            seen.add(value_text)
        for duplicate in sorted(duplicates):
            self._add_issue("ERROR", code, f"Duplicate ID detected: {duplicate}", duplicate)

    def _validate_evidence_links(self) -> None:
        assert self.report is not None
        findings = self.report.get("findings", [])
        evidence_objects = self.report.get("evidence_objects", [])

        evidence_by_id = {
            evidence.get("evidence_id"): evidence
            for evidence in evidence_objects
            if isinstance(evidence, dict)
        }
        finding_ids = {
            finding.get("id")
            for finding in findings
            if isinstance(finding, dict)
        }

        for finding in findings:
            if not isinstance(finding, dict):
                continue
            finding_id = finding.get("id")
            for evidence_id in finding.get("evidence_ids", []):
                if evidence_id not in evidence_by_id:
                    self._add_issue("ERROR", "MISSING_LINKED_EVIDENCE", f"Finding references missing evidence_id: {evidence_id}", finding_id)
                    continue
                linked = evidence_by_id[evidence_id]
                if linked.get("finding_id") != finding_id:
                    self._add_issue("ERROR", "EVIDENCE_FINDING_LINK_MISMATCH", f"Evidence {evidence_id} points to {linked.get('finding_id')} instead of {finding_id}.", finding_id)

        for evidence in evidence_objects:
            if not isinstance(evidence, dict):
                continue
            evidence_id = evidence.get("evidence_id")
            if evidence.get("finding_id") not in finding_ids:
                self._add_issue("ERROR", "ORPHAN_EVIDENCE_OBJECT", f"Evidence object points to missing finding_id: {evidence.get('finding_id')}", evidence_id)

    def _validate_signal_family_summary(self) -> None:
        assert self.report is not None
        summary = self.report.get("summary", {})
        findings = self.report.get("findings", [])
        if not isinstance(summary, dict) or not isinstance(findings, list):
            return

        expected_counts: dict[str, int] = {}
        for finding in findings:
            if not isinstance(finding, dict):
                continue
            signal = finding.get("signal_family")
            if isinstance(signal, str):
                expected_counts[signal] = expected_counts.get(signal, 0) + 1

        actual_counts = summary.get("signal_families")
        if actual_counts != expected_counts:
            self._add_issue("ERROR", "SIGNAL_FAMILY_SUMMARY_MISMATCH", "summary.signal_families does not match finding signal_family counts.")

    def _validate_finding_zero_autonomy_boundaries(self) -> None:
        assert self.report is not None
        findings = self.report.get("findings", [])
        if not isinstance(findings, list):
            return

        for finding in findings:
            if not isinstance(finding, dict):
                continue
            self._validate_zero_autonomy_boundary(finding.get("zero_autonomy_boundary"), f"finding:{finding.get('id')}")

    def _validate_zero_autonomy_boundary(self, boundary: Any, item_id: str) -> None:
        if not isinstance(boundary, dict):
            self._add_issue("ERROR", "MISSING_ZERO_AUTONOMY_BOUNDARY", "zero_autonomy_boundary missing or invalid.", item_id)
            return

        for field_name in sorted(REQUIRED_ZERO_AUTONOMY_TRUE_FIELDS):
            if boundary.get(field_name) is not True:
                self._add_issue("ERROR", "ZERO_AUTONOMY_BOUNDARY_VIOLATION", f"{field_name} must remain true.", item_id)

    def _build_result(self) -> ValidationResult:
        error_count = sum(1 for issue in self.issues if issue.severity == "ERROR")
        warning_count = sum(1 for issue in self.issues if issue.severity == "WARNING")

        if error_count > 0:
            status = "INVALID"
            is_valid = False
        elif warning_count > 0:
            status = "VALID_WITH_WARNINGS"
            is_valid = True
        else:
            status = "VALID"
            is_valid = True

        summary = {
            "error_count": error_count,
            "warning_count": warning_count,
            "issue_count": len(self.issues),
        }

        if self.report is not None and isinstance(self.report.get("summary"), dict):
            report_summary = self.report["summary"]
            summary.update(
                {
                    "findings_count": report_summary.get("findings_count"),
                    "evidence_objects_count": report_summary.get("evidence_objects_count"),
                    "high_or_critical_findings_count": report_summary.get("high_or_critical_findings_count"),
                    "autonomous_actions": report_summary.get("autonomous_actions"),
                }
            )

        return ValidationResult(
            status=status,
            is_valid=is_valid,
            report_path=str(self.report_path),
            summary=summary,
            issues=self.issues,
            zero_autonomy_boundary=build_validator_zero_autonomy_boundary(),
        )

    def _add_issue(self, severity: str, code: str, message: str, item_id: str | None = None) -> None:
        self.issues.append(
            ValidationIssue(
                severity=severity,
                code=code,
                message=message,
                item_id=item_id,
            )
        )


def build_validator_zero_autonomy_boundary() -> dict[str, Any]:
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
        "statement": "This validator checks local evidence report structure only. It does not approve, reject, block, punish, sign, mutate, or execute institutional actions.",
    }


def validate_institutional_approval_evidence_report(
    report_path: Path = EVIDENCE_REPORT_FILE,
    output_file: Path = VALIDATION_OUTPUT_FILE,
) -> ValidationResult:
    validator = InstitutionalApprovalEvidenceReportValidator(report_path=report_path)
    result = validator.validate()
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(
        json.dumps(result.to_dict(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return result


def main() -> None:
    result = validate_institutional_approval_evidence_report()
    summary = result.summary

    print("=" * 80)
    print("LEO INSTITUTIONAL APPROVAL EVIDENCE REPORT VALIDATOR v0.1")
    print("=" * 80)
    print(f"STATUS: {result.status}")
    print(f"IS VALID: {result.is_valid}")
    print(f"ERRORS: {summary['error_count']}")
    print(f"WARNINGS: {summary['warning_count']}")
    print(f"FINDINGS: {summary.get('findings_count')}")
    print(f"EVIDENCE OBJECTS: {summary.get('evidence_objects_count')}")
    print(f"HIGH / CRITICAL: {summary.get('high_or_critical_findings_count')}")
    print(f"AUTONOMOUS ACTIONS: {summary.get('autonomous_actions')}")
    print(f"OUTPUT: {VALIDATION_OUTPUT_FILE}")

    if result.issues:
        print("\nISSUES:")
        for issue in result.issues:
            print(f"- [{issue.severity}] {issue.code}: {issue.message}")

    print("=" * 80)


if __name__ == "__main__":
    main()
