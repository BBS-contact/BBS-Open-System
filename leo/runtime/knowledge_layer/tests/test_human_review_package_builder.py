from dataclasses import FrozenInstanceError

import pytest

from leo.runtime.knowledge_layer.human_review_package_builder import (
    HumanReviewPackageBuilder,
    KnowledgeLayerHumanReviewPackage,
)
from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)
from leo.runtime.knowledge_layer.knowledge_integration_reference_resolver import (
    KnowledgeIntegrationReferenceResolver,
)
from leo.runtime.knowledge_layer.knowledge_integration_validator import (
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
                "foundation/knowledge_architecture/"
                "LEO_KNOWLEDGE_MODEL.md"
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
    integration_record_id: str = "KIR-HUMAN-REVIEW-PACKAGE-001",
    evidence_lineage_reference: str = "EVIDENCE_LINEAGE_FRAMEWORK.md",
    provenance_reference: str = (
        "INSTITUTIONAL_MEMORY_PROVENANCE_MODEL.md"
    ),
    implementation_limitations: list[str] | None = None,
    reviewer_notes: list[str] | None = None,
) -> KnowledgeIntegrationRecord:
    return KnowledgeIntegrationRecord(
        integration_record_id=integration_record_id,
        integration_record_version="0.1",
        integration_record_status="DRAFT",
        created_at="2026-07-10T00:00:00Z",
        source_artifact_path=(
            "foundation/engineering_ontology/example.md"
        ),
        source_artifact_type="reviewed_document",
        source_artifact_status="reviewed",
        source_artifact_commit="abcdef12",
        referenced_runtime_layer="leo/runtime/process_mode",
        referenced_runtime_output_path="not_applicable",
        ontology_concept_reference=(
            "knowledge_layer_runtime_integration"
        ),
        knowledge_architecture_reference="LEO_KNOWLEDGE_MODEL.md",
        institutional_memory_reference=(
            "INSTITUTIONAL_MEMORY_REGISTRY.md"
        ),
        evidence_lineage_reference=evidence_lineage_reference,
        provenance_reference=provenance_reference,
        public_evaluation_relevance="review_support",
        human_review_required=True,
        implementation_limitations=(
            list(implementation_limitations)
            if implementation_limitations is not None
            else ["Public evaluation suitability is not yet assessed."]
        ),
        reviewer_notes=(
            list(reviewer_notes)
            if reviewer_notes is not None
            else ["Independent human review remains required."]
        ),
    )


def make_validator() -> KnowledgeIntegrationValidator:
    return KnowledgeIntegrationValidator(
        reference_resolver=KnowledgeIntegrationReferenceResolver(
            reference_catalog=make_reference_catalog()
        )
    )


def make_validation_result(
    record: KnowledgeIntegrationRecord,
) -> KnowledgeIntegrationValidationResult:
    return make_validator().validate(record)


def test_builder_creates_read_only_human_review_package() -> None:
    record = make_record()
    validation_result = make_validation_result(record)
    builder = HumanReviewPackageBuilder()

    package = builder.build(record, validation_result)

    assert isinstance(package, KnowledgeLayerHumanReviewPackage)
    assert (
        package.package_type
        == "LEO_KNOWLEDGE_LAYER_HUMAN_REVIEW_PACKAGE"
    )
    assert package.package_version == "0.1"
    assert package.integration_record_id == record.integration_record_id
    assert package.human_review_required is True
    assert package.integration_record == record.to_dict()
    assert package.validation_summary["is_valid"] is True
    assert package.validation_summary["requires_human_review"] is False


def test_builder_preserves_runtime_reference_results() -> None:
    record = make_record()
    validation_result = make_validation_result(record)
    package = HumanReviewPackageBuilder().build(
        record,
        validation_result,
    )

    assert len(package.runtime_references) == len(
        validation_result.reference_resolution_results
    )

    assert tuple(
        reference["reference_type"]
        for reference in package.runtime_references
    ) == tuple(
        result.reference_type
        for result in validation_result.reference_resolution_results
    )


def test_builder_preserves_ontology_and_memory_references() -> None:
    record = make_record()
    validation_result = make_validation_result(record)
    package = HumanReviewPackageBuilder().build(
        record,
        validation_result,
    )

    assert package.ontology_mappings == {
        "ontology_concept_reference": (
            record.ontology_concept_reference
        ),
        "knowledge_architecture_reference": (
            record.knowledge_architecture_reference
        ),
    }

    assert package.institutional_memory_references == (
        record.institutional_memory_reference,
    )


def test_builder_preserves_evidence_lineage_summary() -> None:
    record = make_record(
        evidence_lineage_reference="unknown",
    )
    validation_result = make_validation_result(record)
    package = HumanReviewPackageBuilder().build(
        record,
        validation_result,
    )

    summary = package.evidence_lineage_summary

    assert summary["evidence_lineage_reference"] == "unknown"
    assert summary["validation_available"] is True
    assert summary["is_valid"] is False
    assert summary["requires_human_review"] is True
    assert summary["explicit_unknown_fields"] == [
        "evidence_lineage_reference"
    ]
    assert summary["issues"]


def test_builder_preserves_provenance_summary() -> None:
    record = make_record(
        provenance_reference="missing",
    )
    validation_result = make_validation_result(record)
    package = HumanReviewPackageBuilder().build(
        record,
        validation_result,
    )

    summary = package.provenance_summary

    assert summary["provenance_reference"] == "missing"
    assert summary["source_artifact_path"] == record.source_artifact_path
    assert (
        summary["source_artifact_status"]
        == record.source_artifact_status
    )
    assert (
        summary["source_artifact_commit"]
        == record.source_artifact_commit
    )
    assert summary["validation_available"] is True
    assert summary["is_valid"] is False
    assert summary["requires_human_review"] is True
    assert summary["explicit_unknown_fields"] == [
        "provenance_reference"
    ]
    assert summary["issues"]


def test_builder_preserves_limitations_and_reviewer_notes() -> None:
    limitations = [
        "Canonical status has not been independently assessed.",
        "Archive status is outside the current record contract.",
    ]
    reviewer_notes = [
        "Reviewer must confirm public evaluation suitability.",
        "No autonomous decision has been produced.",
    ]

    record = make_record(
        implementation_limitations=limitations,
        reviewer_notes=reviewer_notes,
    )
    validation_result = make_validation_result(record)
    package = HumanReviewPackageBuilder().build(
        record,
        validation_result,
    )

    assert package.implementation_limitations == tuple(limitations)
    assert package.reviewer_notes == tuple(reviewer_notes)


def test_to_dict_returns_detached_export_structure() -> None:
    record = make_record()
    validation_result = make_validation_result(record)
    package = HumanReviewPackageBuilder().build(
        record,
        validation_result,
    )

    exported = package.to_dict()

    assert exported["package_type"] == package.package_type
    assert exported["integration_record_id"] == (
        record.integration_record_id
    )
    assert isinstance(exported["runtime_references"], list)
    assert isinstance(
        exported["institutional_memory_references"],
        list,
    )
    assert isinstance(exported["implementation_limitations"], list)
    assert isinstance(exported["reviewer_notes"], list)
    assert isinstance(
        exported["validation_summary"][
            "unresolved_reference_types"
        ],
        list,
    )
    assert isinstance(
        exported["validation_summary"]["issues"],
        list,
    )

    exported["integration_record"]["integration_record_id"] = "changed"
    exported["implementation_limitations"].append("changed")

    assert (
        package.integration_record["integration_record_id"]
        == record.integration_record_id
    )
    assert "changed" not in package.implementation_limitations


def test_builder_rejects_non_record_input() -> None:
    record = make_record()
    validation_result = make_validation_result(record)
    builder = HumanReviewPackageBuilder()

    with pytest.raises(
        TypeError,
        match="record must be a KnowledgeIntegrationRecord",
    ):
        builder.build(  # type: ignore[arg-type]
            {"integration_record_id": record.integration_record_id},
            validation_result,
        )


def test_builder_rejects_non_validation_result_input() -> None:
    record = make_record()
    builder = HumanReviewPackageBuilder()

    with pytest.raises(
        TypeError,
        match=(
            "validation_result must be a "
            "KnowledgeIntegrationValidationResult"
        ),
    ):
        builder.build(  # type: ignore[arg-type]
            record,
            {"is_valid": True},
        )


def test_builder_rejects_mismatched_record_identifier() -> None:
    record = make_record(
        integration_record_id="KIR-PACKAGE-RECORD-001",
    )
    other_record = make_record(
        integration_record_id="KIR-PACKAGE-RECORD-002",
    )
    validation_result = make_validation_result(other_record)
    builder = HumanReviewPackageBuilder()

    with pytest.raises(
        ValueError,
        match=(
            "validation_result integration_record_id must match record"
        ),
    ):
        builder.build(record, validation_result)


def test_human_review_package_is_immutable() -> None:
    record = make_record()
    validation_result = make_validation_result(record)
    package = HumanReviewPackageBuilder().build(
        record,
        validation_result,
    )

    with pytest.raises(FrozenInstanceError):
        package.package_version = "changed"  # type: ignore[misc]


def test_builder_does_not_modify_inputs() -> None:
    record = make_record()
    validation_result = make_validation_result(record)
    original_record = record.to_dict()
    original_result = validation_result

    HumanReviewPackageBuilder().build(
        record,
        validation_result,
    )

    assert record.to_dict() == original_record
    assert validation_result == original_result


def test_builder_preserves_governance_boundaries() -> None:
    record = make_record()
    validation_result = make_validation_result(record)
    builder = HumanReviewPackageBuilder()
    package = builder.build(record, validation_result)

    assert builder.is_review_support_only is True
    assert builder.automates_review is False
    assert builder.mutates_record is False
    assert builder.mutates_validation_result is False
    assert builder.writes_files is False
    assert builder.inspects_repository_state is False
    assert builder.infers_missing_information is False
    assert builder.assigns_record_status is False
    assert (
        builder.determines_public_evaluation_suitability
        is False
    )
    assert builder.creates_autonomous_decision is False

    assert package.is_review_support_only is True
    assert package.automates_review is False
    assert package.is_enforcement_output is False
    assert package.is_fraud_verdict is False
    assert package.is_legal_verdict is False
    assert package.is_compliance_verdict is False
    assert package.mutates_production is False