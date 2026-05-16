r"""
LEO Institutional Approval Review Pipeline v0.1

Canonical Path:
D:\BBS-09-01-2026\leo\runtime\demos\institutional_approval_review\institutional_approval_review_pipeline.py

Purpose:
Generate evidence-backed institutional approval continuity review findings from
local CSV inputs after the input quality layer confirms structural readiness.

This pipeline identifies review-worthy approval continuity signals such as:
- missing required approvals,
- pending required review while execution/handoff is ready,
- unresolved rejection followed by approval,
- conflicting approval states,
- emergency override without documented reason,
- exception without documentation,
- missing decision owner confirmation,
- and legal/finance/management continuity gaps.

This pipeline does NOT:
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
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
INPUT_QUALITY_REPORT_FILE = OUTPUT_DIR / "institutional_approval_input_quality_report.json"
OUTPUT_FILE = OUTPUT_DIR / "institutional_approval_evidence_report.json"


REQUESTS_FILE = INPUT_DIR / "approval_requests.csv"
STEPS_FILE = INPUT_DIR / "approval_steps.csv"
POLICY_RULES_FILE = INPUT_DIR / "approval_policy_rules.csv"
ROLE_MATRIX_FILE = INPUT_DIR / "approval_role_matrix.csv"
EXCEPTIONS_FILE = INPUT_DIR / "approval_exception_register.csv"


REVIEW_POSITIVE_STATES = {"APPROVED", "OVERRIDE_APPROVED"}
REVIEW_BLOCKING_STATES = {"PENDING", "REJECTED", "ESCALATED", "NEEDS_REPLACEMENT"}
READY_EXECUTION_STATES = {"READY_FOR_HANDOFF", "EXECUTION_READY"}
READY_HANDOFF_STATES = {"HANDOFF_READY", "HANDOFF_PENDING"}
HIGH_RISK_LEVELS = {"HIGH", "CRITICAL"}


@dataclass(frozen=True)
class Finding:
    """Evidence-backed approval continuity review finding."""

    id: str
    request_id: str
    title: str
    severity: str
    signal_family: str
    detected_signal: str
    why_it_matters: str
    reviewer_question: str
    next_action: str
    responsible_review_layer: list[str]
    rule_trace: dict[str, Any]
    evidence_ids: list[str]
    verdict_boundary: str
    zero_autonomy_boundary: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "request_id": self.request_id,
            "title": self.title,
            "severity": self.severity,
            "signal_family": self.signal_family,
            "detected_signal": self.detected_signal,
            "why_it_matters": self.why_it_matters,
            "reviewer_question": self.reviewer_question,
            "next_action": self.next_action,
            "responsible_review_layer": self.responsible_review_layer,
            "rule_trace": self.rule_trace,
            "evidence_ids": self.evidence_ids,
            "verdict_boundary": self.verdict_boundary,
            "zero_autonomy_boundary": self.zero_autonomy_boundary,
        }


@dataclass(frozen=True)
class EvidenceObject:
    """Evidence object preserving approval continuity review context."""

    evidence_id: str
    finding_id: str
    request_id: str
    source_records: list[str]
    signal_family: str
    evidence_summary: str
    data_points: dict[str, Any]
    created_at: str
    boundary_statement: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "evidence_id": self.evidence_id,
            "finding_id": self.finding_id,
            "request_id": self.request_id,
            "source_records": self.source_records,
            "signal_family": self.signal_family,
            "evidence_summary": self.evidence_summary,
            "data_points": self.data_points,
            "created_at": self.created_at,
            "boundary_statement": self.boundary_statement,
        }


@dataclass
class PipelineResult:
    """Container for pipeline output."""

    report_id: str
    report_version: str
    generated_at: str
    source_input_quality_report: str
    input_quality_status: str
    input_quality_ready_for_analysis: bool
    findings: list[Finding] = field(default_factory=list)
    evidence_objects: list[EvidenceObject] = field(default_factory=list)
    zero_autonomy_boundary: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        high_or_critical_count = sum(
            1 for finding in self.findings if finding.severity in {"HIGH", "CRITICAL"}
        )
        signal_families: dict[str, int] = {}
        for finding in self.findings:
            signal_families[finding.signal_family] = signal_families.get(finding.signal_family, 0) + 1

        return {
            "report_id": self.report_id,
            "report_version": self.report_version,
            "generated_at": self.generated_at,
            "source_input_quality_report": self.source_input_quality_report,
            "input_quality_status": self.input_quality_status,
            "input_quality_ready_for_analysis": self.input_quality_ready_for_analysis,
            "summary": {
                "findings_count": len(self.findings),
                "evidence_objects_count": len(self.evidence_objects),
                "high_or_critical_findings_count": high_or_critical_count,
                "signal_families": signal_families,
                "autonomous_actions": 0,
            },
            "findings": [finding.to_dict() for finding in self.findings],
            "evidence_objects": [evidence.to_dict() for evidence in self.evidence_objects],
            "zero_autonomy_boundary": self.zero_autonomy_boundary,
        }


class InstitutionalApprovalReviewPipeline:
    """Generates approval continuity review findings from local CSV inputs."""

    def __init__(self, base_dir: Path = BASE_DIR) -> None:
        self.base_dir = base_dir
        self.input_dir = base_dir / "input"
        self.output_dir = base_dir / "output"
        self.requests: list[dict[str, str]] = []
        self.steps: list[dict[str, str]] = []
        self.rules: list[dict[str, str]] = []
        self.roles: list[dict[str, str]] = []
        self.exceptions: list[dict[str, str]] = []
        self.findings: list[Finding] = []
        self.evidence_objects: list[EvidenceObject] = []
        self.finding_counter = 0

    def run(self) -> PipelineResult:
        """Run the approval review pipeline."""

        quality_report = self._load_input_quality_report()
        quality_status = str(quality_report.get("status", "UNKNOWN"))
        ready_for_analysis = bool(quality_report.get("ready_for_analysis", False))

        if not ready_for_analysis:
            return PipelineResult(
                report_id="LOCAL_INSTITUTIONAL_APPROVAL_EVIDENCE_REPORT",
                report_version="v0.1",
                generated_at=utc_now(),
                source_input_quality_report=str(INPUT_QUALITY_REPORT_FILE),
                input_quality_status=quality_status,
                input_quality_ready_for_analysis=False,
                findings=[],
                evidence_objects=[],
                zero_autonomy_boundary=build_zero_autonomy_boundary(),
            )

        self._load_inputs()
        self._generate_findings()

        return PipelineResult(
            report_id="LOCAL_INSTITUTIONAL_APPROVAL_EVIDENCE_REPORT",
            report_version="v0.1",
            generated_at=utc_now(),
            source_input_quality_report=str(self.output_dir / "institutional_approval_input_quality_report.json"),
            input_quality_status=quality_status,
            input_quality_ready_for_analysis=True,
            findings=self.findings,
            evidence_objects=self.evidence_objects,
            zero_autonomy_boundary=build_zero_autonomy_boundary(),
        )

    def _load_input_quality_report(self) -> dict[str, Any]:
        quality_report_file = self.output_dir / "institutional_approval_input_quality_report.json"

        if not quality_report_file.exists():
            raise FileNotFoundError(
                f"Input quality report missing: {quality_report_file}. "
                "Run institutional_approval_input_quality_report.py first."
            )

        return json.loads(quality_report_file.read_text(encoding="utf-8"))

    def _load_inputs(self) -> None:
        self.requests = read_csv(REQUESTS_FILE)
        self.steps = read_csv(STEPS_FILE)
        self.rules = read_csv(POLICY_RULES_FILE)
        self.roles = read_csv(ROLE_MATRIX_FILE)
        self.exceptions = read_csv(EXCEPTIONS_FILE)

    def _generate_findings(self) -> None:
        steps_by_request = group_by(self.steps, "request_id")
        exceptions_by_request = group_by(self.exceptions, "request_id")

        for request in self.requests:
            request_id = request["request_id"]
            request_steps = steps_by_request.get(request_id, [])
            request_exceptions = exceptions_by_request.get(request_id, [])
            matched_rules = self._match_policy_rules(request)
            required_roles = self._required_roles_for_request(request, matched_rules)

            self._detect_missing_required_approval(request, request_steps, required_roles, matched_rules)
            self._detect_pending_required_review_with_ready_state(request, request_steps, matched_rules)
            self._detect_unresolved_rejection_followed_by_approval(request, request_steps, matched_rules)
            self._detect_missing_decision_owner(request, request_steps, matched_rules)
            self._detect_emergency_override_without_reason(request, request_steps, request_exceptions, matched_rules)
            self._detect_exception_without_documentation(request, request_exceptions, matched_rules)
            self._detect_legal_review_missing_for_contractual_request(request, request_steps, matched_rules)

    def _match_policy_rules(self, request: dict[str, str]) -> list[dict[str, str]]:
        request_type = request.get("request_type", "")
        risk_level = request.get("risk_level", "")
        amount = safe_float(request.get("amount_pln", "0"))

        matches: list[dict[str, str]] = []
        for rule in self.rules:
            rule_type = rule.get("request_type", "")
            rule_risk = rule.get("risk_level", "")
            threshold = safe_float(rule.get("amount_threshold_pln", "0"))
            if rule_type not in {request_type, "ANY"}:
                continue
            if rule_risk != risk_level:
                continue
            if amount >= threshold:
                matches.append(rule)
        return matches

    def _required_roles_for_request(
        self,
        request: dict[str, str],
        matched_rules: list[dict[str, str]],
    ) -> set[str]:
        required: set[str] = set()
        for rule in matched_rules:
            required.update(split_pipe(rule.get("required_roles", "")))

        if to_bool(request.get("requires_legal_review")):
            required.add("legal_review")
        if to_bool(request.get("requires_finance_review")):
            required.add("finance_review")
        if to_bool(request.get("requires_management_review")):
            required.add("management_board")
        if to_bool(request.get("emergency_override_used")):
            required.add("executive_override")

        return required

    def _detect_missing_required_approval(
        self,
        request: dict[str, str],
        request_steps: list[dict[str, str]],
        required_roles: set[str],
        matched_rules: list[dict[str, str]],
    ) -> None:
        present_roles = {step.get("role", "") for step in request_steps}
        missing_roles = sorted(required_roles - present_roles)
        if not missing_roles:
            return

        severity = severity_for_request(request, default="HIGH")
        self._add_finding(
            request=request,
            title="Missing required approval",
            severity=severity,
            signal_family="missing_required_approval",
            detected_signal=f"Required approval role(s) missing: {', '.join(missing_roles)}.",
            why_it_matters="The request appears to require one or more approval roles that are not present in the recorded approval chain.",
            reviewer_question="Which required approval role is missing, and should the request remain blocked for handoff until reviewed?",
            next_action="Request missing approval evidence or escalate for institutional review.",
            responsible_review_layer=missing_roles,
            matched_rules=matched_rules,
            source_records=source_records_for(request, request_steps, []),
            data_points={"missing_roles": missing_roles, "present_roles": sorted(present_roles)},
        )

    def _detect_pending_required_review_with_ready_state(
        self,
        request: dict[str, str],
        request_steps: list[dict[str, str]],
        matched_rules: list[dict[str, str]],
    ) -> None:
        execution_status = request.get("execution_status", "")
        handoff_status = request.get("handoff_status", "")
        if execution_status not in READY_EXECUTION_STATES and handoff_status not in READY_HANDOFF_STATES:
            return

        pending_steps = [
            step for step in request_steps
            if step.get("is_required", "").upper() == "TRUE"
            and step.get("review_status", "") in {"PENDING", "NEEDS_REPLACEMENT", "ESCALATED"}
        ]
        if not pending_steps:
            return

        roles = [step.get("role", "UNKNOWN_ROLE") for step in pending_steps]
        self._add_finding(
            request=request,
            title="Ready state with unresolved required review",
            severity=severity_for_request(request, default="HIGH"),
            signal_family="execution_ready_with_pending_review",
            detected_signal=f"Request is marked {execution_status}/{handoff_status} while required review remains unresolved: {', '.join(roles)}.",
            why_it_matters="A request should not appear ready for handoff or execution while a required review state remains pending, escalated, or requiring replacement.",
            reviewer_question="Why is readiness indicated before required review closure?",
            next_action="Hold readiness interpretation and request human review of unresolved steps.",
            responsible_review_layer=roles,
            matched_rules=matched_rules,
            source_records=source_records_for(request, pending_steps, []),
            data_points={"execution_status": execution_status, "handoff_status": handoff_status, "unresolved_roles": roles},
        )

    def _detect_unresolved_rejection_followed_by_approval(
        self,
        request: dict[str, str],
        request_steps: list[dict[str, str]],
        matched_rules: list[dict[str, str]],
    ) -> None:
        sorted_steps = sorted(request_steps, key=lambda step: safe_int(step.get("step_order", "0")))
        rejection_seen = False
        rejected_roles: list[str] = []
        later_approval_roles: list[str] = []

        for step in sorted_steps:
            status = step.get("review_status", "")
            role = step.get("role", "UNKNOWN_ROLE")
            if status == "REJECTED":
                rejection_seen = True
                rejected_roles.append(role)
            elif rejection_seen and status in REVIEW_POSITIVE_STATES:
                later_approval_roles.append(role)

        if not rejected_roles or not later_approval_roles:
            return

        self._add_finding(
            request=request,
            title="Unresolved rejection followed by approval",
            severity="HIGH",
            signal_family="unresolved_rejection_followed_by_approval",
            detected_signal=f"Rejected review role(s) {', '.join(rejected_roles)} were followed by approval role(s) {', '.join(later_approval_roles)}.",
            why_it_matters="A rejection followed by approval can be legitimate, but the exception path must be documented and reviewed.",
            reviewer_question="Was the rejection resolved through a documented exception or institutional escalation path?",
            next_action="Escalate for institutional review and verify exception documentation.",
            responsible_review_layer=sorted(set(rejected_roles + later_approval_roles)),
            matched_rules=matched_rules,
            source_records=source_records_for(request, sorted_steps, []),
            data_points={"rejected_roles": rejected_roles, "later_approval_roles": later_approval_roles},
        )

    def _detect_missing_decision_owner(
        self,
        request: dict[str, str],
        request_steps: list[dict[str, str]],
        matched_rules: list[dict[str, str]],
    ) -> None:
        owner = request.get("current_owner", "").strip()
        final_state = request.get("final_decision_state", "").strip()
        confirmed_steps = [
            step for step in request_steps
            if step.get("decision_owner_confirmed", "").upper() == "TRUE"
        ]

        if owner and confirmed_steps:
            return

        if final_state in {"UNDER_REVIEW", "PENDING", "UNDER_ESCALATION"} or not confirmed_steps:
            self._add_finding(
                request=request,
                title="Missing or unclear decision owner",
                severity=severity_for_request(request, default="MEDIUM"),
                signal_family="missing_decision_owner",
                detected_signal="Decision ownership is unclear or not confirmed by the recorded approval chain.",
                why_it_matters="Institutional review requires a clear responsible owner before handoff or escalation can be interpreted reliably.",
                reviewer_question="Who currently owns the decision and what review layer must close it?",
                next_action="Assign or confirm responsible human review owner before handoff.",
                responsible_review_layer=[owner or "UNDEFINED_OWNER"],
                matched_rules=matched_rules,
                source_records=source_records_for(request, request_steps, []),
                data_points={"current_owner": owner, "final_decision_state": final_state, "confirmed_owner_steps": len(confirmed_steps)},
            )

    def _detect_emergency_override_without_reason(
        self,
        request: dict[str, str],
        request_steps: list[dict[str, str]],
        request_exceptions: list[dict[str, str]],
        matched_rules: list[dict[str, str]],
    ) -> None:
        override_used = to_bool(request.get("emergency_override_used"))
        if not override_used:
            return

        request_reason = to_bool(request.get("override_reason_present"))
        exception_reason_present = any(to_bool(exception.get("reason_provided")) for exception in request_exceptions)
        if request_reason and exception_reason_present:
            return

        override_steps = [step for step in request_steps if step.get("role") == "executive_override"]
        self._add_finding(
            request=request,
            title="Emergency override without documented reason",
            severity="CRITICAL" if request.get("risk_level") == "CRITICAL" else "HIGH",
            signal_family="emergency_override_without_reason",
            detected_signal="Emergency override was used but documented reason is missing or incomplete.",
            why_it_matters="Emergency override may be necessary, but it must remain traceable and reviewable after the event.",
            reviewer_question="What documented reason justified the emergency override and where is it preserved?",
            next_action="Request override reason documentation and post-event review.",
            responsible_review_layer=["executive_override", "internal_audit"],
            matched_rules=matched_rules,
            source_records=source_records_for(request, override_steps, request_exceptions),
            data_points={"request_override_reason_present": request_reason, "exception_reason_present": exception_reason_present},
        )

    def _detect_exception_without_documentation(
        self,
        request: dict[str, str],
        request_exceptions: list[dict[str, str]],
        matched_rules: list[dict[str, str]],
    ) -> None:
        for exception in request_exceptions:
            if to_bool(exception.get("documentation_present")):
                continue
            self._add_finding(
                request=request,
                title="Exception record without supporting documentation",
                severity=severity_for_request(request, default="HIGH"),
                signal_family="exception_without_documentation",
                detected_signal=f"Exception {exception.get('exception_id')} references missing or unavailable documentation.",
                why_it_matters="Exceptional approval paths require supporting documentation for auditability and accountability.",
                reviewer_question="Where is the supporting exception documentation and who must review it?",
                next_action="Request exception documentation before handoff readiness is accepted.",
                responsible_review_layer=[exception.get("approved_role", "exception_review"), "internal_audit"],
                matched_rules=matched_rules,
                source_records=source_records_for(request, [], [exception]),
                data_points={
                    "exception_id": exception.get("exception_id"),
                    "exception_type": exception.get("exception_type"),
                    "documentation_reference": exception.get("documentation_reference"),
                    "documentation_present": exception.get("documentation_present"),
                },
            )

    def _detect_legal_review_missing_for_contractual_request(
        self,
        request: dict[str, str],
        request_steps: list[dict[str, str]],
        matched_rules: list[dict[str, str]],
    ) -> None:
        linked_contract = request.get("linked_contract_reference", "").strip()
        requires_legal = to_bool(request.get("requires_legal_review"))
        if not linked_contract and not requires_legal:
            return

        legal_steps = [step for step in request_steps if step.get("role") == "legal_review"]
        if legal_steps:
            return

        self._add_finding(
            request=request,
            title="Legal review missing for contractual request",
            severity=severity_for_request(request, default="HIGH"),
            signal_family="legal_review_missing_for_contractual_action",
            detected_signal="Request has contractual/legal review requirement but no legal review step is recorded.",
            why_it_matters="Contractual actions should remain reviewable by the responsible legal review layer before handoff readiness is accepted.",
            reviewer_question="Why is legal review missing for this request and who must review the contract reference?",
            next_action="Request legal review record or documented exception.",
            responsible_review_layer=["legal_review"],
            matched_rules=matched_rules,
            source_records=source_records_for(request, request_steps, []),
            data_points={"linked_contract_reference": linked_contract, "requires_legal_review": requires_legal},
        )

    def _add_finding(
        self,
        request: dict[str, str],
        title: str,
        severity: str,
        signal_family: str,
        detected_signal: str,
        why_it_matters: str,
        reviewer_question: str,
        next_action: str,
        responsible_review_layer: list[str],
        matched_rules: list[dict[str, str]],
        source_records: list[str],
        data_points: dict[str, Any],
    ) -> None:
        self.finding_counter += 1
        finding_id = f"IAR-{self.finding_counter:03d}"
        evidence_id = f"IAE-{self.finding_counter:03d}"
        rule_trace = build_rule_trace(matched_rules, signal_family)
        boundary = build_zero_autonomy_boundary()
        request_id = request.get("request_id", "UNKNOWN_REQUEST")

        finding = Finding(
            id=finding_id,
            request_id=request_id,
            title=title,
            severity=severity,
            signal_family=signal_family,
            detected_signal=detected_signal,
            why_it_matters=why_it_matters,
            reviewer_question=reviewer_question,
            next_action=next_action,
            responsible_review_layer=sorted(set(layer for layer in responsible_review_layer if layer)),
            rule_trace=rule_trace,
            evidence_ids=[evidence_id],
            verdict_boundary="This finding is a human-review signal only. It does not approve, reject, block, punish, sign, mutate, or execute any institutional action.",
            zero_autonomy_boundary=boundary,
        )
        evidence = EvidenceObject(
            evidence_id=evidence_id,
            finding_id=finding_id,
            request_id=request_id,
            source_records=source_records,
            signal_family=signal_family,
            evidence_summary=detected_signal,
            data_points=data_points,
            created_at=utc_now(),
            boundary_statement="Evidence object preserves local review context only and does not mutate source records or execute institutional action.",
        )
        self.findings.append(finding)
        self.evidence_objects.append(evidence)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return [dict(row) for row in csv.DictReader(file)]


def group_by(rows: list[dict[str, str]], key: str) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row.get(key, ""), []).append(row)
    return grouped


def split_pipe(value: str) -> set[str]:
    return {part.strip() for part in value.split("|") if part.strip()}


def to_bool(value: str | bool | None) -> bool:
    if isinstance(value, bool):
        return value
    return str(value or "").strip().upper() == "TRUE"


def safe_float(value: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def safe_int(value: str) -> int:
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return 0


def severity_for_request(request: dict[str, str], default: str = "MEDIUM") -> str:
    risk_level = request.get("risk_level", "").strip().upper()
    if risk_level in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
        return risk_level
    return default


def source_records_for(
    request: dict[str, str],
    steps: list[dict[str, str]],
    exceptions: list[dict[str, str]],
) -> list[str]:
    records = [f"approval_requests:{request.get('request_id', 'UNKNOWN_REQUEST')}"]
    records.extend(f"approval_steps:{step.get('step_id', 'UNKNOWN_STEP')}" for step in steps)
    records.extend(f"approval_exception_register:{exception.get('exception_id', 'UNKNOWN_EXCEPTION')}" for exception in exceptions)
    return records


def build_rule_trace(
    matched_rules: list[dict[str, str]],
    signal_family: str,
) -> dict[str, Any]:
    if matched_rules:
        rule = matched_rules[0]
        return {
            "source_rule_id": rule.get("rule_id", "UNMATCHED_RULE"),
            "source_rule_name": rule.get("human_readable_rule", "Matched institutional approval rule"),
            "source_rule_file": "approval_policy_rules.csv",
            "protocol_reference": protocol_for_signal(signal_family),
            "human_readable_rule": rule.get("human_readable_rule", "Human review is required."),
            "verdict_boundary": rule.get("verdict_boundary", default_verdict_boundary()),
        }

    return {
        "source_rule_id": "IAR-GENERAL-CONTINUITY-RULE",
        "source_rule_name": "General Institutional Approval Continuity Review Rule",
        "source_rule_file": "approval_policy_rules.csv",
        "protocol_reference": protocol_for_signal(signal_family),
        "human_readable_rule": "Approval continuity gaps require human review when recorded decision states are incomplete, conflicting, or not ready for handoff.",
        "verdict_boundary": default_verdict_boundary(),
    }


def protocol_for_signal(signal_family: str) -> str:
    mapping = {
        "missing_required_approval": "MISSING_REQUIRED_APPROVAL_PROTOCOL_v0.1.md",
        "execution_ready_with_pending_review": "APPROVAL_ORDER_INCONSISTENCY_PROTOCOL_v0.1.md",
        "unresolved_rejection_followed_by_approval": "UNRESOLVED_REJECTION_PROTOCOL_v0.1.md",
        "missing_decision_owner": "MISSING_DECISION_OWNER_PROTOCOL_v0.1.md",
        "emergency_override_without_reason": "EMERGENCY_OVERRIDE_REVIEW_PROTOCOL_v0.1.md",
        "exception_without_documentation": "EMERGENCY_OVERRIDE_REVIEW_PROTOCOL_v0.1.md",
        "legal_review_missing_for_contractual_action": "MISSING_REQUIRED_APPROVAL_PROTOCOL_v0.1.md",
    }
    return mapping.get(signal_family, "INSTITUTIONAL_APPROVAL_REVIEW_GENERAL_PROTOCOL_v0.1.md")


def default_verdict_boundary() -> str:
    return "This rule creates a human review requirement only. It does not approve, reject, block, punish, sign, mutate, or execute any institutional action."


def build_zero_autonomy_boundary() -> dict[str, Any]:
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
        "statement": "This report contains evidence-backed approval continuity review signals only. It does not approve, reject, block, punish, sign, mutate, or execute institutional actions.",
    }


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def generate_institutional_approval_evidence_report(
    output_file: Path = OUTPUT_FILE,
) -> PipelineResult:
    pipeline = InstitutionalApprovalReviewPipeline()
    result = pipeline.run()
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(
        json.dumps(result.to_dict(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return result


def main() -> None:
    result = generate_institutional_approval_evidence_report()
    payload = result.to_dict()
    summary = payload["summary"]

    print("=" * 76)
    print("LEO INSTITUTIONAL APPROVAL REVIEW PIPELINE v0.1")
    print("=" * 76)
    print(f"INPUT QUALITY STATUS: {result.input_quality_status}")
    print(f"READY FOR ANALYSIS: {result.input_quality_ready_for_analysis}")
    print(f"FINDINGS: {summary['findings_count']}")
    print(f"EVIDENCE OBJECTS: {summary['evidence_objects_count']}")
    print(f"HIGH / CRITICAL: {summary['high_or_critical_findings_count']}")
    print(f"AUTONOMOUS ACTIONS: {summary['autonomous_actions']}")
    print(f"OUTPUT: {OUTPUT_FILE}")
    print("=" * 76)


if __name__ == "__main__":
    main()
