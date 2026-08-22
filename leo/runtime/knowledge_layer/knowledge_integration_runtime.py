"""Deterministic orchestration runtime for the LEO Knowledge Layer.

This module coordinates the existing record builder, integration validator,
and human review package builder.

The runtime operates only on explicitly supplied record fields. It does not
load external artifacts, write files, inspect repository state, infer missing
information, mutate reviewed sources, assign record statuses, automate review,
or produce legal, fraud, compliance, approval, rejection, or enforcement
decisions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from leo.runtime.knowledge_layer.human_review_package_builder import (
    HumanReviewPackageBuilder,
    KnowledgeLayerHumanReviewPackage,
)
from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)
from leo.runtime.knowledge_layer.knowledge_integration_record_builder import (
    KnowledgeIntegrationRecordBuilder,
)
from leo.runtime.knowledge_layer.knowledge_integration_validator import (
    KnowledgeIntegrationValidationResult,
    KnowledgeIntegrationValidator,
)


@dataclass(frozen=True)
class KnowledgeIntegrationRuntimeResult:
    """Immutable result of one deterministic runtime execution."""

    integration_record: KnowledgeIntegrationRecord
    validation_result: KnowledgeIntegrationValidationResult
    human_review_package: KnowledgeLayerHumanReviewPackage

    def to_dict(self) -> dict[str, Any]:
        """Return a detached dictionary representation for review export."""

        return {
            "integration_record": self.integration_record.to_dict(),
            "validation_result": {
                "integration_record_id": (
                    self.validation_result.integration_record_id
                ),
                "is_valid": self.validation_result.is_valid,
                "requires_human_review": (
                    self.validation_result.requires_human_review
                ),
                "unresolved_reference_types": list(
                    self.validation_result.unresolved_reference_types
                ),
                "integration_record_status": (
                    self.validation_result.integration_record_status
                ),
                "public_evaluation_relevance": (
                    self.validation_result.public_evaluation_relevance
                ),
                "review_status_consistency_assessed": (
                    self.validation_result.review_status_consistency_assessed
                ),
                "public_evaluation_suitability_assessed": (
                    self.validation_result
                    .public_evaluation_suitability_assessed
                ),
                "issues": [
                    {
                        "issue_type": issue.issue_type,
                        "message": issue.message,
                        "component": issue.component,
                        "field_name": issue.field_name,
                    }
                    for issue in self.validation_result.issues
                ],
            },
            "human_review_package": self.human_review_package.to_dict(),
        }

    @property
    def is_review_support_only(self) -> bool:
        """Return True because runtime output supports human review only."""

        return True

    @property
    def human_review_required(self) -> bool:
        """Return True because every Knowledge Layer output requires review."""

        return True

    @property
    def is_enforcement_output(self) -> bool:
        """Return False because runtime output is not enforcement."""

        return False

    @property
    def is_fraud_verdict(self) -> bool:
        """Return False because runtime output is not a fraud verdict."""

        return False

    @property
    def is_legal_verdict(self) -> bool:
        """Return False because runtime output is not a legal verdict."""

        return False

    @property
    def is_compliance_verdict(self) -> bool:
        """Return False because runtime output is not a compliance verdict."""

        return False

    @property
    def mutates_production(self) -> bool:
        """Return False because runtime execution is read-only."""

        return False


@dataclass
class KnowledgeIntegrationRuntime:
    """Coordinate the deterministic Knowledge Layer processing sequence."""

    validator: KnowledgeIntegrationValidator = field(
        default_factory=KnowledgeIntegrationValidator
    )
    human_review_package_builder: HumanReviewPackageBuilder = field(
        default_factory=HumanReviewPackageBuilder
    )

    def run(
        self,
        record_fields: dict[str, Any],
    ) -> KnowledgeIntegrationRuntimeResult:
        """Build, validate, and package one explicit integration record."""

        if not isinstance(record_fields, dict):
            raise TypeError("record_fields must be a dictionary")

        builder = KnowledgeIntegrationRecordBuilder()
        builder.set_fields(**record_fields)

        record = builder.build()
        validation_result = self.validator.validate(record)
        human_review_package = self.human_review_package_builder.build(
            record,
            validation_result,
        )

        return KnowledgeIntegrationRuntimeResult(
            integration_record=record,
            validation_result=validation_result,
            human_review_package=human_review_package,
        )

    def run_record(
        self,
        record: KnowledgeIntegrationRecord,
    ) -> KnowledgeIntegrationRuntimeResult:
        """Validate and package an already built integration record."""

        if not isinstance(record, KnowledgeIntegrationRecord):
            raise TypeError(
                "record must be a KnowledgeIntegrationRecord"
            )

        validation_result = self.validator.validate(record)
        human_review_package = self.human_review_package_builder.build(
            record,
            validation_result,
        )

        return KnowledgeIntegrationRuntimeResult(
            integration_record=record,
            validation_result=validation_result,
            human_review_package=human_review_package,
        )

    @property
    def processing_sequence(self) -> tuple[str, ...]:
        """Return the explicit deterministic runtime sequence."""

        return (
            "build_integration_record",
            "resolve_references",
            "validate_evidence_lineage",
            "validate_provenance",
            "validate_integration_record",
            "build_human_review_package",
            "return_review_support_result",
        )

    @property
    def is_deterministic(self) -> bool:
        """Return True because identical explicit inputs use one fixed sequence."""

        return True

    @property
    def is_review_support_only(self) -> bool:
        """Return True because the runtime only supports human review."""

        return True

    @property
    def human_review_required(self) -> bool:
        """Return True because runtime output requires human review."""

        return True

    @property
    def loads_external_artifacts(self) -> bool:
        """Return False because artifact loading is outside this component."""

        return False

    @property
    def writes_files(self) -> bool:
        """Return False because export belongs to a separate component."""

        return False

    @property
    def exports_artifacts(self) -> bool:
        """Return False because export is outside the current checkpoint."""

        return False

    @property
    def mutates_record(self) -> bool:
        """Return False because runtime does not modify built records."""

        return False

    @property
    def mutates_reviewed_sources(self) -> bool:
        """Return False because reviewed sources remain unchanged."""

        return False

    @property
    def mutates_production(self) -> bool:
        """Return False because runtime execution is read-only."""

        return False

    @property
    def inspects_repository_state(self) -> bool:
        """Return False because repository inspection is outside scope."""

        return False

    @property
    def infers_missing_information(self) -> bool:
        """Return False because unavailable values must remain explicit."""

        return False

    @property
    def assigns_record_status(self) -> bool:
        """Return False because status assignment requires separate control."""

        return False

    @property
    def automates_review(self) -> bool:
        """Return False because human review remains required."""

        return False

    @property
    def creates_autonomous_decision(self) -> bool:
        """Return False because runtime does not make decisions."""

        return False