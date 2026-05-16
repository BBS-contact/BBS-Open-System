r"""
LEO Institutional Approval Human Review Package

Canonical save path:
D:\\BBS-09-01-2026\\leo\\runtime\\demos\\institutional_approval_review\\institutional_approval_human_review_package.py

Purpose:
Create a local, human-controlled review export package for the Institutional Approval
Review demo slice.

Boundary:
- Does not approve institutional actions.
- Does not reject institutional actions.
- Does not enforce institutional actions.
- Does not mutate the source evidence report.
- Does not write to canonical registries.
- Does not interact with production systems.
- Does not access keys or signatures.
"""

from __future__ import annotations

import json
from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence


PACKAGE_TYPE = "LEO_INSTITUTIONAL_APPROVAL_HUMAN_REVIEW_PACKAGE"
PACKAGE_VERSION = "v0.1"
SOURCE_SLICE = "institutional_approval_review"

DEFAULT_SOURCE_REPORT_PATH = Path("output") / "institutional_approval_evidence_report.json"
DEFAULT_OUTPUT_PACKAGE_PATH = Path("output") / "institutional_approval_human_review_package.json"

ALLOWED_REVIEW_ACTIONS = frozenset(
    {
        "ESCALATE_FOR_REVIEW",
        "ACCEPT_AS_JUSTIFIED",
        "MARK_FALSE_POSITIVE",
        "REQUEST_MORE_EVIDENCE",
        "DEFER_REVIEW",
    }
)

ACTIONS_REQUIRING_REVIEWER_NOTE = frozenset(
    {
        "ESCALATE_FOR_REVIEW",
        "MARK_FALSE_POSITIVE",
        "REQUEST_MORE_EVIDENCE",
        "DEFER_REVIEW",
    }
)

ZERO_AUTONOMY_BOUNDARY: Dict[str, bool] = {
    "autonomous_approval": False,
    "autonomous_rejection": False,
    "autonomous_enforcement": False,
    "production_mutation": False,
    "canonical_registry_mutation": False,
    "legal_verdict": False,
    "donor_compliance_verdict": False,
    "payment_blocking": False,
}

PROHIBITED_PACKAGE_KEYS = frozenset(
    {
        "approval_decision",
        "rejection_decision",
        "autonomous_decision",
        "enforcement_instruction",
        "production_write_instruction",
        "canonical_registry_write_instruction",
        "legal_verdict_result",
        "fraud_verdict",
        "corruption_verdict",
    }
)


class HumanReviewPackageError(ValueError):
    """Raised when a human review package cannot be created safely."""


@dataclass(frozen=True)
class HumanReviewRecord:
    """
    Human review layer placed on top of an existing LEO finding.

    This record class is intentionally separate from the generated evidence report.
    It records human treatment of a signal without altering the signal itself.
    """

    finding_id: str
    review_action: str
    reviewer_note: str
    reviewer_id: str = "local_reviewer"
    reviewed_at: Optional[str] = None
    source_report_id: Optional[str] = None
    source_evidence_ids: Sequence[str] = field(default_factory=tuple)
    zero_autonomy_acknowledged: bool = True
    follow_up_required: bool = False
    follow_up_reason: Optional[str] = None
    related_document_references: Sequence[str] = field(default_factory=tuple)
    institutional_unit: Optional[str] = None
    review_priority_override: Optional[str] = None
    review_confidence: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        reviewed_at = self.reviewed_at or _utc_now_iso()
        return {
            "finding_id": self.finding_id,
            "review_action": self.review_action,
            "reviewer_note": self.reviewer_note,
            "reviewer_id": self.reviewer_id,
            "reviewed_at": reviewed_at,
            "source_report_id": self.source_report_id,
            "source_evidence_ids": list(self.source_evidence_ids),
            "zero_autonomy_acknowledged": self.zero_autonomy_acknowledged,
            "follow_up_required": self.follow_up_required,
            "follow_up_reason": self.follow_up_reason,
            "related_document_references": list(self.related_document_references),
            "institutional_unit": self.institutional_unit,
            "review_priority_override": self.review_priority_override,
            "review_confidence": self.review_confidence,
        }


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_json_file(path: Path | str) -> Dict[str, Any]:
    resolved_path = Path(path)
    if not resolved_path.exists():
        raise HumanReviewPackageError(f"Source report not found: {resolved_path}")
    if not resolved_path.is_file():
        raise HumanReviewPackageError(f"Source report path is not a file: {resolved_path}")

    try:
        loaded = json.loads(resolved_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise HumanReviewPackageError(f"Invalid JSON source report: {resolved_path}") from exc

    if not isinstance(loaded, dict):
        raise HumanReviewPackageError("Source report must be a JSON object.")

    return loaded


def write_json_file(path: Path | str, payload: Mapping[str, Any]) -> None:
    resolved_path = Path(path)
    resolved_path.parent.mkdir(parents=True, exist_ok=True)
    resolved_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def create_review_record(
    *,
    finding_id: str,
    review_action: str,
    reviewer_note: str,
    reviewer_id: str = "local_reviewer",
    reviewed_at: Optional[str] = None,
    source_report_id: Optional[str] = None,
    source_evidence_ids: Optional[Sequence[str]] = None,
    zero_autonomy_acknowledged: bool = True,
    follow_up_required: bool = False,
    follow_up_reason: Optional[str] = None,
    related_document_references: Optional[Sequence[str]] = None,
    institutional_unit: Optional[str] = None,
    review_priority_override: Optional[str] = None,
    review_confidence: Optional[str] = None,
) -> Dict[str, Any]:
    """Create and validate a dictionary representation of a human review record."""

    record = HumanReviewRecord(
        finding_id=finding_id,
        review_action=review_action,
        reviewer_note=reviewer_note,
        reviewer_id=reviewer_id,
        reviewed_at=reviewed_at,
        source_report_id=source_report_id,
        source_evidence_ids=tuple(source_evidence_ids or ()),
        zero_autonomy_acknowledged=zero_autonomy_acknowledged,
        follow_up_required=follow_up_required,
        follow_up_reason=follow_up_reason,
        related_document_references=tuple(related_document_references or ()),
        institutional_unit=institutional_unit,
        review_priority_override=review_priority_override,
        review_confidence=review_confidence,
    ).to_dict()
    validate_review_record(record)
    return record


def validate_review_record(record: Mapping[str, Any]) -> None:
    if not isinstance(record, Mapping):
        raise HumanReviewPackageError("Review record must be an object.")

    finding_id = record.get("finding_id")
    if not isinstance(finding_id, str) or not finding_id.strip():
        raise HumanReviewPackageError("Review record requires a non-empty finding_id.")

    review_action = record.get("review_action")
    if review_action not in ALLOWED_REVIEW_ACTIONS:
        raise HumanReviewPackageError(f"Unknown review_action: {review_action}")

    reviewer_note = record.get("reviewer_note")
    if not isinstance(reviewer_note, str):
        raise HumanReviewPackageError("reviewer_note must be a string.")

    if review_action in ACTIONS_REQUIRING_REVIEWER_NOTE and not reviewer_note.strip():
        raise HumanReviewPackageError(
            f"reviewer_note is required for review_action {review_action}."
        )

    reviewer_id = record.get("reviewer_id")
    if not isinstance(reviewer_id, str) or not reviewer_id.strip():
        raise HumanReviewPackageError("reviewer_id must be a non-empty string.")

    source_evidence_ids = record.get("source_evidence_ids", [])
    if not isinstance(source_evidence_ids, list):
        raise HumanReviewPackageError("source_evidence_ids must be a list.")
    if any(not isinstance(item, str) or not item.strip() for item in source_evidence_ids):
        raise HumanReviewPackageError("source_evidence_ids must contain only non-empty strings.")

    if record.get("zero_autonomy_acknowledged") is not True:
        raise HumanReviewPackageError("zero_autonomy_acknowledged must be true.")

    follow_up_required = record.get("follow_up_required", False)
    if not isinstance(follow_up_required, bool):
        raise HumanReviewPackageError("follow_up_required must be boolean.")

    follow_up_reason = record.get("follow_up_reason")
    if follow_up_required and (not isinstance(follow_up_reason, str) or not follow_up_reason.strip()):
        raise HumanReviewPackageError("follow_up_reason is required when follow_up_required is true.")


def validate_review_records(records: Iterable[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    validated: List[Dict[str, Any]] = []
    for record in records:
        validate_review_record(record)
        validated.append(deepcopy(dict(record)))
    return validated


def _extract_source_report_id(source_report: Mapping[str, Any]) -> str:
    for key in (
        "report_id",
        "evidence_report_id",
        "source_report_id",
        "run_id",
        "generated_report_id",
    ):
        value = source_report.get(key)
        if isinstance(value, str) and value.strip():
            return value
    return "institutional_approval_evidence_report_local"


def _extract_findings(source_report: Mapping[str, Any]) -> List[Mapping[str, Any]]:
    findings = source_report.get("findings", [])
    if not isinstance(findings, list):
        raise HumanReviewPackageError("Source report findings must be a list when present.")
    if any(not isinstance(item, Mapping) for item in findings):
        raise HumanReviewPackageError("Source report findings must contain only objects.")
    return findings


def _extract_evidence_objects(source_report: Mapping[str, Any]) -> List[Mapping[str, Any]]:
    for key in ("evidence_objects", "evidence", "evidence_items"):
        value = source_report.get(key)
        if value is None:
            continue
        if not isinstance(value, list):
            raise HumanReviewPackageError(f"Source report {key} must be a list when present.")
        if any(not isinstance(item, Mapping) for item in value):
            raise HumanReviewPackageError(f"Source report {key} must contain only objects.")
        return value
    return []


def _count_by_key(items: Sequence[Mapping[str, Any]], key_candidates: Sequence[str]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for item in items:
        selected_value = None
        for key in key_candidates:
            value = item.get(key)
            if isinstance(value, str) and value.strip():
                selected_value = value.strip()
                break
        if selected_value is None:
            selected_value = "UNSPECIFIED"
        counts[selected_value] = counts.get(selected_value, 0) + 1
    return dict(sorted(counts.items()))


def build_source_report_summary(source_report: Mapping[str, Any]) -> Dict[str, Any]:
    findings = _extract_findings(source_report)
    evidence_objects = _extract_evidence_objects(source_report)

    return {
        "source_report_id": _extract_source_report_id(source_report),
        "findings_count": len(findings),
        "evidence_objects_count": len(evidence_objects),
        "findings_by_severity": _count_by_key(findings, ("severity", "risk_level", "priority")),
        "findings_by_signal_family": _count_by_key(
            findings,
            ("signal_family", "finding_type", "risk_signal", "category"),
        ),
    }


def _enrich_review_records_with_source_report(
    records: Sequence[Mapping[str, Any]],
    source_report_id: str,
) -> List[Dict[str, Any]]:
    enriched: List[Dict[str, Any]] = []
    for record in records:
        item = deepcopy(dict(record))
        if not item.get("source_report_id"):
            item["source_report_id"] = source_report_id
        if not item.get("reviewed_at"):
            item["reviewed_at"] = _utc_now_iso()
        enriched.append(item)
    return enriched


def assert_no_prohibited_package_keys(payload: Mapping[str, Any]) -> None:
    present = PROHIBITED_PACKAGE_KEYS.intersection(payload.keys())
    if present:
        joined = ", ".join(sorted(present))
        raise HumanReviewPackageError(f"Package contains prohibited top-level keys: {joined}")


def build_human_review_package(
    *,
    source_report: Mapping[str, Any],
    review_records: Optional[Iterable[Mapping[str, Any]]] = None,
    generated_at: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Build a local human review export package from an evidence report.

    The function does not mutate source_report. It returns a new dictionary that may be
    written to disk by the caller.
    """

    if not isinstance(source_report, Mapping):
        raise HumanReviewPackageError("source_report must be an object.")

    source_report_summary = build_source_report_summary(source_report)
    source_report_id = source_report_summary["source_report_id"]

    validated_records = validate_review_records(review_records or [])
    enriched_records = _enrich_review_records_with_source_report(validated_records, source_report_id)

    package: Dict[str, Any] = {
        "package_type": PACKAGE_TYPE,
        "package_version": PACKAGE_VERSION,
        "source_slice": SOURCE_SLICE,
        "source_report_id": source_report_id,
        "generated_at": generated_at or _utc_now_iso(),
        "reviewed_findings_count": len(enriched_records),
        "review_records": enriched_records,
        "zero_autonomy_boundary": deepcopy(ZERO_AUTONOMY_BOUNDARY),
        "source_report_summary": source_report_summary,
        "export_integrity_notes": [
            "Local human review package only.",
            "Source evidence report is not modified by this package builder.",
            "Review records are separated from generated findings.",
            "No autonomous approval, rejection, enforcement, production mutation, or legal verdict is produced.",
        ],
    }

    assert_no_prohibited_package_keys(package)
    return package


def generate_human_review_package_file(
    *,
    source_report_path: Path | str = DEFAULT_SOURCE_REPORT_PATH,
    output_package_path: Path | str = DEFAULT_OUTPUT_PACKAGE_PATH,
    review_records: Optional[Iterable[Mapping[str, Any]]] = None,
    generated_at: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Load a source evidence report and write a local human review package JSON.

    This function creates or overwrites only the export package file supplied through
    output_package_path. It never writes to the source evidence report path.
    """

    source_path = Path(source_report_path)
    output_path = Path(output_package_path)

    if source_path.resolve() == output_path.resolve():
        raise HumanReviewPackageError("Output package path must differ from source report path.")

    source_report = load_json_file(source_path)
    package = build_human_review_package(
        source_report=source_report,
        review_records=review_records,
        generated_at=generated_at,
    )
    write_json_file(output_path, package)
    return package


def main() -> None:
    package = generate_human_review_package_file()
    print(
        json.dumps(
            {
                "package_type": package["package_type"],
                "package_version": package["package_version"],
                "source_slice": package["source_slice"],
                "source_report_id": package["source_report_id"],
                "reviewed_findings_count": package["reviewed_findings_count"],
                "output_path": str(DEFAULT_OUTPUT_PACKAGE_PATH),
                "zero_autonomy_boundary": package["zero_autonomy_boundary"],
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
