from dataclasses import FrozenInstanceError

import pytest

from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)
from leo.runtime.knowledge_layer.provenance_validator import (
    ProvenanceValidationIssue,
    ProvenanceValidationResult,
    ProvenanceValidator,
)


def make_record(
    *,
    integration_record_status: str = "DRAFT",
    source_artifact_path: str = "foundation/engineering_ontology/example.md",
    source_artifact_status: str = "reviewed",
    source_artifact_commit: str = "abcdef12",
    provenance_reference: str = (
        "foundation/institutional_memory/"
        "INSTITUTIONAL_MEMORY_PROVENANCE_MODEL.md"
    ),
) -> KnowledgeIntegrationRecord:
    return KnowledgeIntegrationRecord(
        integration_record_id="KIR-PROVENANCE-TEST-001",
        integration_record_version="0.1",
        integration_record_status=integration_record_status,
        created_at="2026-07-10T00:00:00Z",
        source_artifact_path=source_artifact_path,
        source_artifact_type="reviewed_document",
        source_artifact_status=source_artifact_status,
        source_artifact_commit=source_artifact_commit,
        referenced_runtime_layer="leo/runtime/process_mode",
        referenced_runtime_output_path="not_applicable",
        ontology_concept_reference="knowledge_layer_runtime_integration",
        knowledge_architecture_reference="LEO_KNOWLEDGE_MODEL.md",
        institutional_memory_reference="INSTITUTIONAL_MEMORY_REGISTRY.md",
        evidence_lineage_reference="EVIDENCE_LINEAGE_FRAMEWORK.md",
        provenance_reference=provenance_reference,
        public_evaluation_relevance="review_support",
        human_review_required=True,
    )


def test_valid_provenance_fields_pass_validation() -> None:
    validator = ProvenanceValidator()
    record = make_record()

    result = validator.validate(record)

    assert isinstance(result, ProvenanceValidationResult)
    assert result.is_valid is True
    assert result.explicit_unknown_fields == ()
    assert result.issues == ()
    assert result.requires_human_review is False


@pytest.mark.parametrize(
    ("field_name", "marker"),
    [
        ("provenance_reference", "missing"),
        ("provenance_reference", "unknown"),
        ("provenance_reference", "not_applicable"),
        ("source_artifact_path", "missing"),
        ("source_artifact_status", "unknown"),
        ("source_artifact_commit", "unknown"),
    ],
)
def test_explicit_unknown_provenance_requires_human_review(
    field_name: str,
    marker: str,
) -> None:
    validator = ProvenanceValidator()
    record = make_record(**{field_name: marker})

    result = validator.validate(record)

    assert result.is_valid is False
    assert result.explicit_unknown_fields == (field_name,)
    assert result.requires_human_review is True
    assert ProvenanceValidationIssue(
        issue_type="explicit_unknown_provenance",
        message=(
            f"{field_name} uses an explicit unknown marker "
            f"and requires human review: {marker}"
        ),
        field_name=field_name,
    ) in result.issues


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("provenance_reference", " provenance/reference.md"),
        ("provenance_reference", "provenance/reference.md "),
        ("source_artifact_path", " foundation/example.md"),
        ("source_artifact_path", "foundation/example.md "),
        ("source_artifact_status", " reviewed"),
        ("source_artifact_status", "reviewed "),
        ("source_artifact_commit", " abcdef12"),
        ("source_artifact_commit", "abcdef12 "),
    ],
)
def test_non_normalized_provenance_whitespace_is_detected(
    field_name: str,
    value: str,
) -> None:
    validator = ProvenanceValidator()
    record = make_record(**{field_name: value})

    result = validator.validate(record)

    assert result.is_valid is False
    assert result.explicit_unknown_fields == ()
    assert result.requires_human_review is True
    assert ProvenanceValidationIssue(
        issue_type="provenance_whitespace_not_normalized",
        message=(
            f"{field_name} must not contain leading or trailing whitespace"
        ),
        field_name=field_name,
    ) in result.issues


def test_multiple_unknown_provenance_fields_are_reported_together() -> None:
    validator = ProvenanceValidator()
    record = make_record(
        provenance_reference="unknown",
        source_artifact_commit="missing",
    )

    result = validator.validate(record)

    assert result.is_valid is False
    assert result.explicit_unknown_fields == (
        "provenance_reference",
        "source_artifact_commit",
    )
    assert len(result.issues) == 2
    assert result.requires_human_review is True


def test_validator_rejects_non_record_input() -> None:
    validator = ProvenanceValidator()

    with pytest.raises(
        TypeError,
        match="record must be a KnowledgeIntegrationRecord",
    ):
        validator.validate({"provenance_reference": "example"})  # type: ignore[arg-type]


def test_validation_result_is_immutable() -> None:
    validator = ProvenanceValidator()
    result = validator.validate(make_record())

    with pytest.raises(FrozenInstanceError):
        result.is_valid = False  # type: ignore[misc]


def test_validator_preserves_read_only_governance_boundaries() -> None:
    validator = ProvenanceValidator()
    result = validator.validate(make_record())

    assert validator.is_review_support_only is True
    assert validator.mutates_record is False
    assert validator.resolves_external_references is False
    assert validator.inspects_repository_state is False
    assert validator.infers_provenance is False
    assert validator.determines_canonical_status is False
    assert validator.determines_archive_status is False
    assert validator.creates_autonomous_decision is False

    assert result.is_review_support_only is True
    assert result.is_enforcement_output is False
    assert result.is_fraud_verdict is False
    assert result.is_legal_verdict is False
    assert result.mutates_production is False