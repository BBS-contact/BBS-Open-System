"""Knowledge integration record model for the LEO Knowledge Layer Runtime.

This module defines the central read-only integration record used to
connect reviewed knowledge artifacts, runtime references, evidence
lineage, provenance, public evaluation context, and human review
requirements.

The record is a review-support artifact only. It is not an enforcement,
fraud, legal, compliance, approval, or rejection decision.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar


_ALLOWED_STATUSES = {
    "DRAFT",
    "BUILT_FROM_REVIEWED_SOURCE",
    "VALIDATION_PASSED",
    "VALIDATION_FAILED",
    "REVIEW_REQUIRED",
    "REVIEWED_ACCEPTED",
    "REVIEWED_REQUIRES_REVISION",
    "ARCHIVED_REFERENCE",
    "SUPERSEDED_WITH_LINEAGE",
    "NOT_FOR_PUBLIC_EVALUATION",
}


@dataclass(frozen=True)
class KnowledgeIntegrationRecord:
    """A controlled read-only integration relationship.

    Missing values must be represented explicitly as one of:
    ``missing``, ``unknown``, or ``not_applicable``.

    The object intentionally carries no behavior that can mutate evidence,
    provenance, institutional memory, runtime outputs, or production systems.
    """

    integration_record_id: str
    integration_record_version: str
    integration_record_status: str
    created_at: str
    source_artifact_path: str
    source_artifact_type: str
    source_artifact_status: str
    source_artifact_commit: str
    referenced_runtime_layer: str
    referenced_runtime_output_path: str
    ontology_concept_reference: str
    knowledge_architecture_reference: str
    institutional_memory_reference: str
    evidence_lineage_reference: str
    provenance_reference: str
    public_evaluation_relevance: str
    human_review_required: bool
    implementation_limitations: list[str] = field(default_factory=list)
    reviewer_notes: list[str] = field(default_factory=list)

    ALLOWED_STATUSES: ClassVar[set[str]] = _ALLOWED_STATUSES
    EXPLICIT_UNKNOWN_VALUES: ClassVar[set[str]] = {
        "missing",
        "unknown",
        "not_applicable",
    }

    def __post_init__(self) -> None:
        self._validate_status()
        self._validate_human_review()
        self._validate_text_fields()
        self._validate_list_fields()

    def _validate_status(self) -> None:
        if self.integration_record_status not in self.ALLOWED_STATUSES:
            raise ValueError(
                "integration_record_status must be one of the approved "
                "KnowledgeIntegrationRecord status values"
            )

    def _validate_human_review(self) -> None:
        if self.human_review_required is not True:
            raise ValueError("human_review_required must be True")

    def _validate_text_fields(self) -> None:
        required_text_fields = {
            "integration_record_id": self.integration_record_id,
            "integration_record_version": self.integration_record_version,
            "created_at": self.created_at,
            "source_artifact_path": self.source_artifact_path,
            "source_artifact_type": self.source_artifact_type,
            "source_artifact_status": self.source_artifact_status,
            "source_artifact_commit": self.source_artifact_commit,
            "referenced_runtime_layer": self.referenced_runtime_layer,
            "referenced_runtime_output_path": self.referenced_runtime_output_path,
            "ontology_concept_reference": self.ontology_concept_reference,
            "knowledge_architecture_reference": self.knowledge_architecture_reference,
            "institutional_memory_reference": self.institutional_memory_reference,
            "evidence_lineage_reference": self.evidence_lineage_reference,
            "provenance_reference": self.provenance_reference,
            "public_evaluation_relevance": self.public_evaluation_relevance,
        }

        for field_name, value in required_text_fields.items():
            if not isinstance(value, str):
                raise TypeError(f"{field_name} must be a string")
            if value == "":
                raise ValueError(
                    f"{field_name} must not be empty; use missing, unknown, "
                    "or not_applicable when the value is unavailable"
                )

    def _validate_list_fields(self) -> None:
        if not isinstance(self.implementation_limitations, list):
            raise TypeError("implementation_limitations must be a list")
        if not isinstance(self.reviewer_notes, list):
            raise TypeError("reviewer_notes must be a list")

        for item in self.implementation_limitations:
            if not isinstance(item, str):
                raise TypeError("implementation_limitations must contain strings only")

        for item in self.reviewer_notes:
            if not isinstance(item, str):
                raise TypeError("reviewer_notes must contain strings only")

    def to_dict(self) -> dict[str, Any]:
        """Return a plain dictionary representation for review packages."""

        return {
            "integration_record_id": self.integration_record_id,
            "integration_record_version": self.integration_record_version,
            "integration_record_status": self.integration_record_status,
            "created_at": self.created_at,
            "source_artifact_path": self.source_artifact_path,
            "source_artifact_type": self.source_artifact_type,
            "source_artifact_status": self.source_artifact_status,
            "source_artifact_commit": self.source_artifact_commit,
            "referenced_runtime_layer": self.referenced_runtime_layer,
            "referenced_runtime_output_path": self.referenced_runtime_output_path,
            "ontology_concept_reference": self.ontology_concept_reference,
            "knowledge_architecture_reference": self.knowledge_architecture_reference,
            "institutional_memory_reference": self.institutional_memory_reference,
            "evidence_lineage_reference": self.evidence_lineage_reference,
            "provenance_reference": self.provenance_reference,
            "public_evaluation_relevance": self.public_evaluation_relevance,
            "human_review_required": self.human_review_required,
            "implementation_limitations": list(self.implementation_limitations),
            "reviewer_notes": list(self.reviewer_notes),
        }

    @property
    def is_review_support_only(self) -> bool:
        """Return True to mark this object as review-support only."""

        return True

    @property
    def is_enforcement_output(self) -> bool:
        """Return False because records must never be enforcement outputs."""

        return False

    @property
    def is_fraud_verdict(self) -> bool:
        """Return False because records must never be fraud verdicts."""

        return False

    @property
    def is_legal_verdict(self) -> bool:
        """Return False because records must never be legal verdicts."""

        return False

    @property
    def mutates_production(self) -> bool:
        """Return False because records must never mutate production."""

        return False