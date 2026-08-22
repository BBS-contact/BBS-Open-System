"""Orchestration validation for KnowledgeIntegrationRecord objects.

This module coordinates the existing read-only reference resolver,
evidence lineage validator, and provenance validator.

It aggregates independently reviewable validation results without
duplicating component-specific rules, modifying records, inferring
missing information, inspecting repository state, or producing legal,
fraud, compliance, approval, rejection, or enforcement decisions.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from leo.runtime.knowledge_layer.evidence_lineage_validator import (
    EvidenceLineageValidationResult,
    EvidenceLineageValidator,
)
from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)
from leo.runtime.knowledge_layer.knowledge_integration_reference_resolver import (
    KnowledgeIntegrationReferenceResolver,
    ReferenceResolutionResult,
)
from leo.runtime.knowledge_layer.provenance_validator import (
    ProvenanceValidationResult,
    ProvenanceValidator,
)


@dataclass(frozen=True)
class KnowledgeIntegrationValidationIssue:
    """An immutable aggregate integration validation issue."""

    issue_type: str
    message: str
    component: str
    field_name: str | None = None


@dataclass(frozen=True)
class KnowledgeIntegrationValidationResult:
    """Immutable aggregate result for one integration record."""

    integration_record_id: str
    is_valid: bool
    requires_human_review: bool
    unresolved_reference_types: tuple[str, ...] = field(default_factory=tuple)
    reference_resolution_results: tuple[ReferenceResolutionResult, ...] = field(
        default_factory=tuple
    )
    evidence_lineage_validation: EvidenceLineageValidationResult | None = None
    provenance_validation: ProvenanceValidationResult | None = None
    integration_record_status: str = ""
    public_evaluation_relevance: str = ""
    review_status_consistency_assessed: bool = False
    public_evaluation_suitability_assessed: bool = False
    issues: tuple[KnowledgeIntegrationValidationIssue, ...] = field(
        default_factory=tuple
    )

    @property
    def is_review_support_only(self) -> bool:
        """Return True because aggregate validation supports human review."""

        return True

    @property
    def is_enforcement_output(self) -> bool:
        """Return False because aggregate validation is not enforcement."""

        return False

    @property
    def is_fraud_verdict(self) -> bool:
        """Return False because aggregate validation is not a fraud verdict."""

        return False

    @property
    def is_legal_verdict(self) -> bool:
        """Return False because aggregate validation is not a legal verdict."""

        return False

    @property
    def is_compliance_verdict(self) -> bool:
        """Return False because aggregate validation is not a compliance verdict."""

        return False

    @property
    def mutates_production(self) -> bool:
        """Return False because aggregate validation is read-only."""

        return False


@dataclass
class KnowledgeIntegrationValidator:
    """Coordinate existing validators without duplicating their rules."""

    reference_resolver: KnowledgeIntegrationReferenceResolver = field(
        default_factory=KnowledgeIntegrationReferenceResolver
    )
    evidence_lineage_validator: EvidenceLineageValidator = field(
        default_factory=EvidenceLineageValidator
    )
    provenance_validator: ProvenanceValidator = field(
        default_factory=ProvenanceValidator
    )

    REFERENCE_FIELD_MAP: tuple[tuple[str, str], ...] = (
        ("runtime_layer_reference", "referenced_runtime_layer"),
        ("runtime_output_reference", "referenced_runtime_output_path"),
        ("ontology_reference", "ontology_concept_reference"),
        ("knowledge_architecture_reference", "knowledge_architecture_reference"),
        ("institutional_memory_reference", "institutional_memory_reference"),
        ("evidence_lineage_reference", "evidence_lineage_reference"),
        ("provenance_reference", "provenance_reference"),
    )

    def validate(
        self,
        record: KnowledgeIntegrationRecord,
    ) -> KnowledgeIntegrationValidationResult:
        """Validate one record through explicit read-only components."""

        if not isinstance(record, KnowledgeIntegrationRecord):
            raise TypeError("record must be a KnowledgeIntegrationRecord")

        reference_results = self._resolve_record_references(record)
        lineage_result = self.evidence_lineage_validator.validate(record)
        provenance_result = self.provenance_validator.validate(record)

        unresolved_reference_types = tuple(
            result.reference_type
            for result in reference_results
            if not result.resolved
            and result.resolution_status != "not_applicable"
        )

        issues = self._build_aggregate_issues(
            reference_results=reference_results,
            lineage_result=lineage_result,
            provenance_result=provenance_result,
        )

        requires_human_review = (
            bool(unresolved_reference_types)
            or lineage_result.requires_human_review
            or provenance_result.requires_human_review
            or bool(issues)
        )

        return KnowledgeIntegrationValidationResult(
            integration_record_id=record.integration_record_id,
            is_valid=not issues,
            requires_human_review=requires_human_review,
            unresolved_reference_types=unresolved_reference_types,
            reference_resolution_results=reference_results,
            evidence_lineage_validation=lineage_result,
            provenance_validation=provenance_result,
            integration_record_status=record.integration_record_status,
            public_evaluation_relevance=record.public_evaluation_relevance,
            review_status_consistency_assessed=False,
            public_evaluation_suitability_assessed=False,
            issues=issues,
        )

    def _resolve_record_references(
        self,
        record: KnowledgeIntegrationRecord,
    ) -> tuple[ReferenceResolutionResult, ...]:
        """Resolve explicitly declared record references."""

        references = {
            reference_type: getattr(record, field_name)
            for reference_type, field_name in self.REFERENCE_FIELD_MAP
        }

        resolved = self.reference_resolver.resolve_many(references)

        return tuple(
            resolved[reference_type]
            for reference_type, _ in self.REFERENCE_FIELD_MAP
        )

    def _build_aggregate_issues(
        self,
        *,
        reference_results: tuple[ReferenceResolutionResult, ...],
        lineage_result: EvidenceLineageValidationResult,
        provenance_result: ProvenanceValidationResult,
    ) -> tuple[KnowledgeIntegrationValidationIssue, ...]:
        """Build independently reviewable aggregate issues."""

        issues: list[KnowledgeIntegrationValidationIssue] = []

        for resolution_result in reference_results:
            if (
                resolution_result.resolved
                or resolution_result.resolution_status == "not_applicable"
            ):
                continue

            issues.append(
                KnowledgeIntegrationValidationIssue(
                    issue_type="unresolved_reference",
                    message=(
                        f"{resolution_result.reference_type} was not resolved: "
                        f"{resolution_result.resolution_status}"
                    ),
                    component="reference_resolver",
                    field_name=resolution_result.reference_type,
                )
            )

        for lineage_issue in lineage_result.issues:
            issues.append(
                KnowledgeIntegrationValidationIssue(
                    issue_type=lineage_issue.issue_type,
                    message=lineage_issue.message,
                    component="evidence_lineage_validator",
                    field_name=lineage_issue.field_name,
                )
            )

        for provenance_issue in provenance_result.issues:
            issues.append(
                KnowledgeIntegrationValidationIssue(
                    issue_type=provenance_issue.issue_type,
                    message=provenance_issue.message,
                    component="provenance_validator",
                    field_name=provenance_issue.field_name,
                )
            )

        return tuple(issues)

    @property
    def is_review_support_only(self) -> bool:
        """Return True because the validator supports human review."""

        return True

    @property
    def mutates_record(self) -> bool:
        """Return False because aggregate validation never changes records."""

        return False

    @property
    def mutates_production(self) -> bool:
        """Return False because aggregate validation is read-only."""

        return False

    @property
    def inspects_repository_state(self) -> bool:
        """Return False because repository inspection is outside this component."""

        return False

    @property
    def infers_missing_information(self) -> bool:
        """Return False because missing information remains explicit."""

        return False

    @property
    def assigns_record_status(self) -> bool:
        """Return False because record status changes require separate control."""

        return False

    @property
    def determines_public_evaluation_suitability(self) -> bool:
        """Return False because no approved suitability matrix exists yet."""

        return False

    @property
    def creates_autonomous_decision(self) -> bool:
        """Return False because aggregate validation does not make decisions."""

        return False