"""Human review package builder for the LEO Knowledge Layer Runtime.

This module packages a KnowledgeIntegrationRecord and its independently
reviewable validation result into a deterministic human review artifact.

The builder does not perform review, modify records, assign statuses, infer
missing information, inspect repository state, determine public evaluation
suitability, or produce legal, fraud, compliance, approval, rejection, or
enforcement decisions.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)
from leo.runtime.knowledge_layer.knowledge_integration_validator import (
    KnowledgeIntegrationValidationResult,
)


@dataclass(frozen=True)
class KnowledgeLayerHumanReviewPackage:
    """Immutable top-level human review package."""

    package_type: str
    package_version: str
    integration_record_id: str
    human_review_required: bool
    integration_record: dict[str, Any]
    runtime_references: tuple[dict[str, Any], ...]
    ontology_mappings: dict[str, str]
    institutional_memory_references: tuple[str, ...]
    evidence_lineage_summary: dict[str, Any]
    provenance_summary: dict[str, Any]
    validation_summary: dict[str, Any]
    implementation_limitations: tuple[str, ...]
    reviewer_notes: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        """Return a detached dictionary representation for review export."""

        return {
            "package_type": self.package_type,
            "package_version": self.package_version,
            "integration_record_id": self.integration_record_id,
            "human_review_required": self.human_review_required,
            "integration_record": dict(self.integration_record),
            "runtime_references": [
                dict(reference)
                for reference in self.runtime_references
            ],
            "ontology_mappings": dict(self.ontology_mappings),
            "institutional_memory_references": list(
                self.institutional_memory_references
            ),
            "evidence_lineage_summary": dict(
                self.evidence_lineage_summary
            ),
            "provenance_summary": dict(self.provenance_summary),
            "validation_summary": {
                **self.validation_summary,
                "unresolved_reference_types": list(
                    self.validation_summary.get(
                        "unresolved_reference_types",
                        (),
                    )
                ),
                "issues": [
                    dict(issue)
                    for issue in self.validation_summary.get(
                        "issues",
                        (),
                    )
                ],
            },
            "implementation_limitations": list(
                self.implementation_limitations
            ),
            "reviewer_notes": list(self.reviewer_notes),
        }

    @property
    def is_review_support_only(self) -> bool:
        """Return True because the package only supports human review."""

        return True

    @property
    def automates_review(self) -> bool:
        """Return False because the package does not perform review."""

        return False

    @property
    def is_enforcement_output(self) -> bool:
        """Return False because the package is not enforcement output."""

        return False

    @property
    def is_fraud_verdict(self) -> bool:
        """Return False because the package is not a fraud verdict."""

        return False

    @property
    def is_legal_verdict(self) -> bool:
        """Return False because the package is not a legal verdict."""

        return False

    @property
    def is_compliance_verdict(self) -> bool:
        """Return False because the package is not a compliance verdict."""

        return False

    @property
    def mutates_production(self) -> bool:
        """Return False because the package is read-only."""

        return False


class HumanReviewPackageBuilder:
    """Build deterministic Knowledge Layer human review packages."""

    PACKAGE_TYPE = "LEO_KNOWLEDGE_LAYER_HUMAN_REVIEW_PACKAGE"
    PACKAGE_VERSION = "0.1"

    def build(
        self,
        record: KnowledgeIntegrationRecord,
        validation_result: KnowledgeIntegrationValidationResult,
    ) -> KnowledgeLayerHumanReviewPackage:
        """Build one review-support package without modifying its inputs."""

        if not isinstance(record, KnowledgeIntegrationRecord):
            raise TypeError(
                "record must be a KnowledgeIntegrationRecord"
            )

        if not isinstance(
            validation_result,
            KnowledgeIntegrationValidationResult,
        ):
            raise TypeError(
                "validation_result must be a "
                "KnowledgeIntegrationValidationResult"
            )

        if (
            validation_result.integration_record_id
            != record.integration_record_id
        ):
            raise ValueError(
                "validation_result integration_record_id must match record"
            )

        return KnowledgeLayerHumanReviewPackage(
            package_type=self.PACKAGE_TYPE,
            package_version=self.PACKAGE_VERSION,
            integration_record_id=record.integration_record_id,
            human_review_required=True,
            integration_record=record.to_dict(),
            runtime_references=self._build_runtime_references(
                validation_result
            ),
            ontology_mappings=self._build_ontology_mappings(record),
            institutional_memory_references=(
                record.institutional_memory_reference,
            ),
            evidence_lineage_summary=(
                self._build_evidence_lineage_summary(
                    record,
                    validation_result,
                )
            ),
            provenance_summary=self._build_provenance_summary(
                record,
                validation_result,
            ),
            validation_summary=self._build_validation_summary(
                validation_result
            ),
            implementation_limitations=tuple(
                record.implementation_limitations
            ),
            reviewer_notes=tuple(record.reviewer_notes),
        )

    def _build_runtime_references(
        self,
        validation_result: KnowledgeIntegrationValidationResult,
    ) -> tuple[dict[str, Any], ...]:
        """Return detached runtime and integration reference results."""

        return tuple(
            resolution_result.to_dict()
            for resolution_result
            in validation_result.reference_resolution_results
        )

    def _build_ontology_mappings(
        self,
        record: KnowledgeIntegrationRecord,
    ) -> dict[str, str]:
        """Return explicit ontology and knowledge architecture mappings."""

        return {
            "ontology_concept_reference": (
                record.ontology_concept_reference
            ),
            "knowledge_architecture_reference": (
                record.knowledge_architecture_reference
            ),
        }

    def _build_evidence_lineage_summary(
        self,
        record: KnowledgeIntegrationRecord,
        validation_result: KnowledgeIntegrationValidationResult,
    ) -> dict[str, Any]:
        """Return a reviewable evidence lineage summary."""

        lineage_result = (
            validation_result.evidence_lineage_validation
        )

        if lineage_result is None:
            return {
                "evidence_lineage_reference": (
                    record.evidence_lineage_reference
                ),
                "validation_available": False,
                "is_valid": False,
                "requires_human_review": True,
                "explicit_unknown_fields": [],
                "issues": [],
            }

        return {
            "evidence_lineage_reference": (
                record.evidence_lineage_reference
            ),
            "validation_available": True,
            "is_valid": lineage_result.is_valid,
            "requires_human_review": (
                lineage_result.requires_human_review
            ),
            "explicit_unknown_fields": list(
                lineage_result.explicit_unknown_fields
            ),
            "issues": [
                {
                    "issue_type": issue.issue_type,
                    "message": issue.message,
                    "field_name": issue.field_name,
                }
                for issue in lineage_result.issues
            ],
        }

    def _build_provenance_summary(
        self,
        record: KnowledgeIntegrationRecord,
        validation_result: KnowledgeIntegrationValidationResult,
    ) -> dict[str, Any]:
        """Return a reviewable provenance summary."""

        provenance_result = validation_result.provenance_validation

        if provenance_result is None:
            return {
                "provenance_reference": record.provenance_reference,
                "source_artifact_path": record.source_artifact_path,
                "source_artifact_status": record.source_artifact_status,
                "source_artifact_commit": record.source_artifact_commit,
                "validation_available": False,
                "is_valid": False,
                "requires_human_review": True,
                "explicit_unknown_fields": [],
                "issues": [],
            }

        return {
            "provenance_reference": record.provenance_reference,
            "source_artifact_path": record.source_artifact_path,
            "source_artifact_status": record.source_artifact_status,
            "source_artifact_commit": record.source_artifact_commit,
            "validation_available": True,
            "is_valid": provenance_result.is_valid,
            "requires_human_review": (
                provenance_result.requires_human_review
            ),
            "explicit_unknown_fields": list(
                provenance_result.explicit_unknown_fields
            ),
            "issues": [
                {
                    "issue_type": issue.issue_type,
                    "message": issue.message,
                    "field_name": issue.field_name,
                }
                for issue in provenance_result.issues
            ],
        }

    def _build_validation_summary(
        self,
        validation_result: KnowledgeIntegrationValidationResult,
    ) -> dict[str, Any]:
        """Return the independently reviewable aggregate summary."""

        return {
            "is_valid": validation_result.is_valid,
            "requires_human_review": (
                validation_result.requires_human_review
            ),
            "integration_record_status": (
                validation_result.integration_record_status
            ),
            "public_evaluation_relevance": (
                validation_result.public_evaluation_relevance
            ),
            "review_status_consistency_assessed": (
                validation_result.review_status_consistency_assessed
            ),
            "public_evaluation_suitability_assessed": (
                validation_result.public_evaluation_suitability_assessed
            ),
            "unresolved_reference_types": tuple(
                validation_result.unresolved_reference_types
            ),
            "issues": tuple(
                {
                    "issue_type": issue.issue_type,
                    "message": issue.message,
                    "component": issue.component,
                    "field_name": issue.field_name,
                }
                for issue in validation_result.issues
            ),
        }

    @property
    def is_review_support_only(self) -> bool:
        """Return True because the builder supports human review."""

        return True

    @property
    def automates_review(self) -> bool:
        """Return False because the builder does not conduct review."""

        return False

    @property
    def mutates_record(self) -> bool:
        """Return False because the builder never changes records."""

        return False

    @property
    def mutates_validation_result(self) -> bool:
        """Return False because validation results remain unchanged."""

        return False

    @property
    def writes_files(self) -> bool:
        """Return False because export belongs to a separate component."""

        return False

    @property
    def inspects_repository_state(self) -> bool:
        """Return False because repository inspection is outside scope."""

        return False

    @property
    def infers_missing_information(self) -> bool:
        """Return False because missing information remains explicit."""

        return False

    @property
    def assigns_record_status(self) -> bool:
        """Return False because status assignment requires separate control."""

        return False

    @property
    def determines_public_evaluation_suitability(self) -> bool:
        """Return False because no approved suitability matrix exists."""

        return False

    @property
    def creates_autonomous_decision(self) -> bool:
        """Return False because the builder does not make decisions."""

        return False