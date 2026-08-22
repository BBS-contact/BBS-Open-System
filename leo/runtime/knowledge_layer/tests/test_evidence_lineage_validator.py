from dataclasses import FrozenInstanceError

import pytest

from leo.runtime.knowledge_layer.evidence_lineage_validator import (
    EvidenceLineageValidationIssue,
    EvidenceLineageValidationResult,
    EvidenceLineageValidator,
)
from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)


def make_record(
    *,
    evidence_lineage_reference: str = (
        "foundation/evidence_lineage/EVIDENCE_LINEAGE_FRAMEWORK.md"
    ),
    provenance_reference: str = (
        "foundation/institutional_memory/"
        "INSTITUTIONAL_MEMORY_PROVENANCE_MODEL.md"
    ),
) -> KnowledgeIntegrationRecord:
    return KnowledgeIntegrationRecord(
        integration_record_id="KIR-TEST-001",
        integration_record_version="0.1",
        integration_record_status="DRAFT",
        created_at="2026-07-10T00:00:00Z",
        source_artifact_path="foundation/example.md",
        source_artifact_type="reviewed_document",
        source_artifact_status="reviewed",
        source_artifact_commit="abcdef12",
        referenced_runtime_layer="knowledge_layer",
        referenced_runtime_output_path="not_applicable",
        ontology_concept_reference="LEO_ENGINEERING_ONTOLOGY_FOUNDATION.md",
        knowledge_architecture_reference="LEO_KNOWLEDGE_MODEL.md",
        institutional_memory_reference="INSTITUTIONAL_MEMORY_REGISTRY.md",
        evidence_lineage_reference=evidence_lineage_reference,
        provenance_reference=provenance_reference,
        public_evaluation_relevance="review_support",
        human_review_required=True,
    )


def test_valid_explicit_references_pass_validation() -> None:
    validator = EvidenceLineageValidator()
    record = make_record()

    result = validator.validate(record)

    assert isinstance(result, EvidenceLineageValidationResult)
    assert result.is_valid is True
    assert result.explicit_unknown_fields == ()
    assert result.issues == ()
    assert result.requires_human_review is False


@pytest.mark.parametrize(
    ("field_name", "marker"),
    [
        ("evidence_lineage_reference", "missing"),
        ("evidence_lineage_reference", "unknown"),
        ("evidence_lineage_reference", "not_applicable"),
        ("provenance_reference", "missing"),
        ("provenance_reference", "unknown"),
        ("provenance_reference", "not_applicable"),
    ],
)
def test_explicit_unknown_reference_requires_human_review(
    field_name: str,
    marker: str,
) -> None:
    validator = EvidenceLineageValidator()
    record = make_record(**{field_name: marker})

    result = validator.validate(record)

    assert result.is_valid is False
    assert result.explicit_unknown_fields == (field_name,)
    assert result.requires_human_review is True
    assert EvidenceLineageValidationIssue(
        issue_type="explicit_unknown_reference",
        message=(
            f"{field_name} uses an explicit unknown marker "
            f"and requires human review: {marker}"
        ),
        field_name=field_name,
    ) in result.issues


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("evidence_lineage_reference", " lineage/reference.md"),
        ("evidence_lineage_reference", "lineage/reference.md "),
        ("provenance_reference", " provenance/reference.md"),
        ("provenance_reference", "provenance/reference.md "),
    ],
)
def test_non_normalized_reference_whitespace_is_detected(
    field_name: str,
    value: str,
) -> None:
    validator = EvidenceLineageValidator()
    record = make_record(**{field_name: value})

    result = validator.validate(record)

    assert result.is_valid is False
    assert result.explicit_unknown_fields == ()
    assert result.requires_human_review is True
    assert EvidenceLineageValidationIssue(
        issue_type="reference_whitespace_not_normalized",
        message=(
            f"{field_name} must not contain leading or trailing whitespace"
        ),
        field_name=field_name,
    ) in result.issues


def test_multiple_unresolved_references_are_reported_together() -> None:
    validator = EvidenceLineageValidator()
    record = make_record(
        evidence_lineage_reference="unknown",
        provenance_reference="missing",
    )

    result = validator.validate(record)

    assert result.is_valid is False
    assert result.explicit_unknown_fields == (
        "evidence_lineage_reference",
        "provenance_reference",
    )
    assert len(result.issues) == 2
    assert result.requires_human_review is True


def test_validator_rejects_non_record_input() -> None:
    validator = EvidenceLineageValidator()

    with pytest.raises(
        TypeError,
        match="record must be a KnowledgeIntegrationRecord",
    ):
        validator.validate({"evidence_lineage_reference": "example"})  # type: ignore[arg-type]


def test_validation_result_is_immutable() -> None:
    validator = EvidenceLineageValidator()
    result = validator.validate(make_record())

    with pytest.raises(FrozenInstanceError):
        result.is_valid = False  # type: ignore[misc]


def test_validator_preserves_review_support_boundaries() -> None:
    validator = EvidenceLineageValidator()
    result = validator.validate(make_record())

    assert validator.is_review_support_only is True
    assert validator.mutates_record is False
    assert validator.resolves_external_references is False
    assert validator.creates_autonomous_decision is False

    assert result.is_enforcement_output is False
    assert result.is_fraud_verdict is False
    assert result.mutates_production is False
