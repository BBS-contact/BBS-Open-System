from dataclasses import FrozenInstanceError

import pytest

from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)
from leo.runtime.knowledge_layer.knowledge_integration_reference_resolver import (
    KnowledgeIntegrationReferenceResolver,
)
from leo.runtime.knowledge_layer.knowledge_integration_validator import (
    KnowledgeIntegrationValidationIssue,
    KnowledgeIntegrationValidationResult,
    KnowledgeIntegrationValidator,
)


def make_reference_catalog() -> dict[str, dict[str, str]]:
    return {
        "runtime_layer_reference": {
            "leo/runtime/process_mode": "leo/runtime/process_mode",
        },
        "runtime_output_reference": {
            "not_applicable": "not_applicable",
        },
        "ontology_reference": {
            "knowledge_layer_runtime_integration": (
                "foundation/engineering_ontology/"
                "LEO_KNOWLEDGE_LAYER_RUNTIME_INTEGRATION_SPEC.md"
            ),
        },
        "knowledge_architecture_reference": {
            "LEO_KNOWLEDGE_MODEL.md": (
                "foundation/knowledge_architecture/LEO_KNOWLEDGE_MODEL.md"
            ),
        },
        "institutional_memory_reference": {
            "INSTITUTIONAL_MEMORY_REGISTRY.md": (
                "foundation/institutional_memory/"
                "INSTITUTIONAL_MEMORY_REGISTRY.md"
            ),
        },
        "evidence_lineage_reference": {
            "EVIDENCE_LINEAGE_FRAMEWORK.md": (
                "foundation/evidence_lineage/"
                "EVIDENCE_LINEAGE_FRAMEWORK.md"
            ),
        },
        "provenance_reference": {
            "INSTITUTIONAL_MEMORY_PROVENANCE_MODEL.md": (
                "foundation/institutional_memory/"
                "INSTITUTIONAL_MEMORY_PROVENANCE_MODEL.md"
            ),
        },
    }


def make_record(
    *,
    referenced_runtime_layer: str = "leo/runtime/process_mode",
    referenced_runtime_output_path: str = "not_applicable",
    ontology_concept_reference: str = "knowledge_layer_runtime_integration",
    knowledge_architecture_reference: str = "LEO_KNOWLEDGE_MODEL.md",
    institutional_memory_reference: str = "INSTITUTIONAL_MEMORY_REGISTRY.md",
    evidence_lineage_reference: str = "EVIDENCE_LINEAGE_FRAMEWORK.md",
    provenance_reference: str = "INSTITUTIONAL_MEMORY_PROVENANCE_MODEL.md",
    integration_record_status: str = "DRAFT",
    public_evaluation_relevance: str = "review_support",
) -> KnowledgeIntegrationRecord:
    return KnowledgeIntegrationRecord(
        integration_record_id="KIR-INTEGRATION-VALIDATOR-TEST-001",
        integration_record_version="0.1",
        integration_record_status=integration_record_status,
        created_at="2026-07-10T00:00:00Z",
        source_artifact_path="foundation/engineering_ontology/example.md",
        source_artifact_type="reviewed_document",
        source_artifact_status="reviewed",
        source_artifact_commit="abcdef12",
        referenced_runtime_layer=referenced_runtime_layer,
        referenced_runtime_output_path=referenced_runtime_output_path,
        ontology_concept_reference=ontology_concept_reference,
        knowledge_architecture_reference=knowledge_architecture_reference,
        institutional_memory_reference=institutional_memory_reference,
        evidence_lineage_reference=evidence_lineage_reference,
        provenance_reference=provenance_reference,
        public_evaluation_relevance=public_evaluation_relevance,
        human_review_required=True,
    )


def make_validator() -> KnowledgeIntegrationValidator:
    return KnowledgeIntegrationValidator(
        reference_resolver=KnowledgeIntegrationReferenceResolver(
            reference_catalog=make_reference_catalog()
        )
    )


def test_fully_resolved_record_passes_aggregate_validation() -> None:
    validator = make_validator()
    record = make_record()

    result = validator.validate(record)

    assert isinstance(result, KnowledgeIntegrationValidationResult)
    assert result.integration_record_id == record.integration_record_id
    assert result.is_valid is True
    assert result.requires_human_review is False
    assert result.unresolved_reference_types == ()
    assert result.issues == ()
    assert result.evidence_lineage_validation is not None
    assert result.evidence_lineage_validation.is_valid is True
    assert result.provenance_validation is not None
    assert result.provenance_validation.is_valid is True
    assert result.integration_record_status == "DRAFT"
    assert result.public_evaluation_relevance == "review_support"
    assert result.review_status_consistency_assessed is False
    assert result.public_evaluation_suitability_assessed is False


def test_unresolved_reference_is_reported() -> None:
    validator = make_validator()
    record = make_record(
        ontology_concept_reference="unregistered_ontology_reference",
    )

    result = validator.validate(record)

    assert result.is_valid is False
    assert result.requires_human_review is True
    assert "ontology_reference" in result.unresolved_reference_types
    assert KnowledgeIntegrationValidationIssue(
        issue_type="unresolved_reference",
        message="ontology_reference was not resolved: unresolved",
        component="reference_resolver",
        field_name="ontology_reference",
    ) in result.issues


def test_explicit_unknown_reference_is_preserved_and_reported() -> None:
    validator = make_validator()
    record = make_record(
        institutional_memory_reference="unknown",
    )

    result = validator.validate(record)

    assert result.is_valid is False
    assert result.requires_human_review is True
    assert "institutional_memory_reference" in result.unresolved_reference_types
    assert KnowledgeIntegrationValidationIssue(
        issue_type="unresolved_reference",
        message="institutional_memory_reference was not resolved: unknown",
        component="reference_resolver",
        field_name="institutional_memory_reference",
    ) in result.issues


def test_evidence_lineage_issues_are_aggregated() -> None:
    validator = make_validator()
    record = make_record(
        evidence_lineage_reference="unknown",
    )

    result = validator.validate(record)

    assert result.is_valid is False
    assert result.requires_human_review is True
    assert KnowledgeIntegrationValidationIssue(
        issue_type="explicit_unknown_reference",
        message=(
            "evidence_lineage_reference uses an explicit unknown marker "
            "and requires human review: unknown"
        ),
        component="evidence_lineage_validator",
        field_name="evidence_lineage_reference",
    ) in result.issues


def test_provenance_issues_are_aggregated() -> None:
    validator = make_validator()
    record = make_record(
        provenance_reference="missing",
    )

    result = validator.validate(record)

    assert result.is_valid is False
    assert result.requires_human_review is True
    assert KnowledgeIntegrationValidationIssue(
        issue_type="explicit_unknown_provenance",
        message=(
            "provenance_reference uses an explicit unknown marker "
            "and requires human review: missing"
        ),
        component="provenance_validator",
        field_name="provenance_reference",
    ) in result.issues


def test_multiple_component_issues_are_preserved() -> None:
    validator = make_validator()
    record = make_record(
        ontology_concept_reference="unregistered_ontology_reference",
        evidence_lineage_reference="unknown",
        provenance_reference="missing",
    )

    result = validator.validate(record)

    assert result.is_valid is False
    assert result.requires_human_review is True

    components = {issue.component for issue in result.issues}

    assert "reference_resolver" in components
    assert "evidence_lineage_validator" in components
    assert "provenance_validator" in components


def test_reference_results_follow_declared_reference_order() -> None:
    validator = make_validator()
    result = validator.validate(make_record())

    assert tuple(
        reference_result.reference_type
        for reference_result in result.reference_resolution_results
    ) == tuple(
        reference_type
        for reference_type, _ in validator.REFERENCE_FIELD_MAP
    )


def test_validator_rejects_non_record_input() -> None:
    validator = make_validator()

    with pytest.raises(
        TypeError,
        match="record must be a KnowledgeIntegrationRecord",
    ):
        validator.validate({"integration_record_id": "example"})  # type: ignore[arg-type]


def test_aggregate_result_is_immutable() -> None:
    validator = make_validator()
    result = validator.validate(make_record())

    with pytest.raises(FrozenInstanceError):
        result.is_valid = False  # type: ignore[misc]


def test_validator_does_not_modify_record() -> None:
    validator = make_validator()
    record = make_record()
    original_record = record.to_dict()

    validator.validate(record)

    assert record.to_dict() == original_record


def test_validator_preserves_governance_boundaries() -> None:
    validator = make_validator()
    result = validator.validate(make_record())

    assert validator.is_review_support_only is True
    assert validator.mutates_record is False
    assert validator.mutates_production is False
    assert validator.inspects_repository_state is False
    assert validator.infers_missing_information is False
    assert validator.assigns_record_status is False
    assert validator.determines_public_evaluation_suitability is False
    assert validator.creates_autonomous_decision is False

    assert result.is_review_support_only is True
    assert result.is_enforcement_output is False
    assert result.is_fraud_verdict is False
    assert result.is_legal_verdict is False
    assert result.is_compliance_verdict is False
    assert result.mutates_production is False