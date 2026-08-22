from dataclasses import FrozenInstanceError

import pytest

from leo.runtime.knowledge_layer.human_review_package_builder import (
    KnowledgeLayerHumanReviewPackage,
)
from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)
from leo.runtime.knowledge_layer.knowledge_integration_reference_resolver import (
    KnowledgeIntegrationReferenceResolver,
)
from leo.runtime.knowledge_layer.knowledge_integration_runtime import (
    KnowledgeIntegrationRuntime,
    KnowledgeIntegrationRuntimeResult,
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


def make_record_fields(
    *,
    integration_record_id: str = "KIR-RUNTIME-TEST-001",
    ontology_concept_reference: str = (
        "knowledge_layer_runtime_integration"
    ),
    evidence_lineage_reference: str = (
        "EVIDENCE_LINEAGE_FRAMEWORK.md"
    ),
    provenance_reference: str = (
        "INSTITUTIONAL_MEMORY_PROVENANCE_MODEL.md"
    ),
) -> dict[str, object]:
    return {
        "integration_record_id": integration_record_id,
        "integration_record_version": "0.1",
        "integration_record_status": "DRAFT",
        "created_at": "2026-07-11T00:00:00Z",
        "source_artifact_path": (
            "foundation/engineering_ontology/example.md"
        ),
        "source_artifact_type": "reviewed_document",
        "source_artifact_status": "reviewed",
        "source_artifact_commit": "abcdef12",
        "referenced_runtime_layer": "leo/runtime/process_mode",
        "referenced_runtime_output_path": "not_applicable",
        "ontology_concept_reference": ontology_concept_reference,
        "knowledge_architecture_reference": (
            "LEO_KNOWLEDGE_MODEL.md"
        ),
        "institutional_memory_reference": (
            "INSTITUTIONAL_MEMORY_REGISTRY.md"
        ),
        "evidence_lineage_reference": (
            evidence_lineage_reference
        ),
        "provenance_reference": provenance_reference,
        "public_evaluation_relevance": "review_support",
        "human_review_required": True,
        "implementation_limitations": [
            "Public evaluation suitability is not yet assessed."
        ],
        "reviewer_notes": [
            "Independent human review remains required."
        ],
    }


def make_runtime() -> KnowledgeIntegrationRuntime:
    return KnowledgeIntegrationRuntime(
        validator=KnowledgeIntegrationValidator(
            reference_resolver=KnowledgeIntegrationReferenceResolver(
                reference_catalog=make_reference_catalog()
            )
        )
    )


def test_runtime_builds_validates_and_packages_record() -> None:
    runtime = make_runtime()

    result = runtime.run(make_record_fields())

    assert isinstance(result, KnowledgeIntegrationRuntimeResult)
    assert isinstance(result.integration_record, KnowledgeIntegrationRecord)
    assert isinstance(
        result.validation_result,
        KnowledgeIntegrationValidationResult,
    )
    assert isinstance(
        result.human_review_package,
        KnowledgeLayerHumanReviewPackage,
    )

    assert result.integration_record.integration_record_id == (
        "KIR-RUNTIME-TEST-001"
    )
    assert result.validation_result.is_valid is True
    assert result.validation_result.requires_human_review is False
    assert result.human_review_package.human_review_required is True


def test_runtime_preserves_validation_issues() -> None:
    runtime = make_runtime()

    result = runtime.run(
        make_record_fields(
            ontology_concept_reference=(
                "unregistered_ontology_reference"
            ),
            evidence_lineage_reference="unknown",
            provenance_reference="missing",
        )
    )

    assert result.validation_result.is_valid is False
    assert result.validation_result.requires_human_review is True
    assert result.validation_result.issues
    assert result.human_review_package.validation_summary[
        "is_valid"
    ] is False
    assert result.human_review_package.validation_summary[
        "requires_human_review"
    ] is True


def test_runtime_can_process_existing_record() -> None:
    runtime = make_runtime()
    record = KnowledgeIntegrationRecord(
        **make_record_fields(
            integration_record_id="KIR-RUNTIME-RECORD-001"
        )
    )

    result = runtime.run_record(record)

    assert result.integration_record is record
    assert result.validation_result.integration_record_id == (
        record.integration_record_id
    )
    assert result.human_review_package.integration_record_id == (
        record.integration_record_id
    )


def test_runtime_run_rejects_non_dictionary_input() -> None:
    runtime = make_runtime()

    with pytest.raises(
        TypeError,
        match="record_fields must be a dictionary",
    ):
        runtime.run(  # type: ignore[arg-type]
            ["invalid", "record", "fields"]
        )


def test_runtime_run_record_rejects_non_record_input() -> None:
    runtime = make_runtime()

    with pytest.raises(
        TypeError,
        match="record must be a KnowledgeIntegrationRecord",
    ):
        runtime.run_record(  # type: ignore[arg-type]
            {"integration_record_id": "invalid"}
        )


def test_runtime_rejects_missing_required_record_fields() -> None:
    runtime = make_runtime()
    fields = make_record_fields()
    fields.pop("provenance_reference")

    with pytest.raises(
        ValueError,
        match="Cannot build KnowledgeIntegrationRecord",
    ):
        runtime.run(fields)


def test_runtime_result_to_dict_returns_detached_structure() -> None:
    runtime = make_runtime()
    result = runtime.run(make_record_fields())

    exported = result.to_dict()

    assert exported["integration_record"][
        "integration_record_id"
    ] == result.integration_record.integration_record_id
    assert exported["validation_result"]["is_valid"] is True
    assert exported["human_review_package"]["package_type"] == (
        "LEO_KNOWLEDGE_LAYER_HUMAN_REVIEW_PACKAGE"
    )

    exported["integration_record"][
        "integration_record_id"
    ] = "changed"
    exported["human_review_package"][
        "implementation_limitations"
    ].append("changed")

    assert result.integration_record.integration_record_id == (
        "KIR-RUNTIME-TEST-001"
    )
    assert "changed" not in (
        result.human_review_package.implementation_limitations
    )


def test_runtime_result_is_immutable() -> None:
    runtime = make_runtime()
    result = runtime.run(make_record_fields())

    with pytest.raises(FrozenInstanceError):
        result.integration_record = result.integration_record  # type: ignore[misc]


def test_runtime_does_not_modify_input_dictionary() -> None:
    runtime = make_runtime()
    record_fields = make_record_fields()
    original_fields = {
        key: (
            list(value)
            if isinstance(value, list)
            else value
        )
        for key, value in record_fields.items()
    }

    runtime.run(record_fields)

    assert record_fields == original_fields


def test_runtime_processing_sequence_is_explicit() -> None:
    runtime = make_runtime()

    assert runtime.processing_sequence == (
        "build_integration_record",
        "resolve_references",
        "validate_evidence_lineage",
        "validate_provenance",
        "validate_integration_record",
        "build_human_review_package",
        "return_review_support_result",
    )


def test_runtime_preserves_governance_boundaries() -> None:
    runtime = make_runtime()
    result = runtime.run(make_record_fields())

    assert runtime.is_deterministic is True
    assert runtime.is_review_support_only is True
    assert runtime.human_review_required is True
    assert runtime.loads_external_artifacts is False
    assert runtime.writes_files is False
    assert runtime.exports_artifacts is False
    assert runtime.mutates_record is False
    assert runtime.mutates_reviewed_sources is False
    assert runtime.mutates_production is False
    assert runtime.inspects_repository_state is False
    assert runtime.infers_missing_information is False
    assert runtime.assigns_record_status is False
    assert runtime.automates_review is False
    assert runtime.creates_autonomous_decision is False

    assert result.is_review_support_only is True
    assert result.human_review_required is True
    assert result.is_enforcement_output is False
    assert result.is_fraud_verdict is False
    assert result.is_legal_verdict is False
    assert result.is_compliance_verdict is False
    assert result.mutates_production is False