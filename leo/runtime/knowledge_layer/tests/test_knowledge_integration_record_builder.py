"""Tests for KnowledgeIntegrationRecordBuilder."""

import pytest

from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)
from leo.runtime.knowledge_layer.knowledge_integration_record_builder import (
    KnowledgeIntegrationRecordBuilder,
)


def valid_fields():
    return {
        "integration_record_id": "kir-builder-001",
        "integration_record_version": "0.1",
        "integration_record_status": "DRAFT",
        "created_at": "2026-07-08",
        "source_artifact_path": "foundation/engineering_ontology/example.md",
        "source_artifact_type": "reviewed_document",
        "source_artifact_status": "reviewed",
        "source_artifact_commit": "unknown",
        "referenced_runtime_layer": "leo/runtime/process_mode",
        "referenced_runtime_output_path": "not_applicable",
        "ontology_concept_reference": "knowledge_layer_runtime_integration",
        "knowledge_architecture_reference": "LEO_KNOWLEDGE_MODEL.md",
        "institutional_memory_reference": "foundation/institutional_memory",
        "evidence_lineage_reference": "unknown",
        "provenance_reference": "unknown",
        "public_evaluation_relevance": "supported",
        "human_review_required": True,
        "implementation_limitations": ["builder test"],
        "reviewer_notes": ["created by builder"],
    }


def test_builder_starts_without_required_fields():
    builder = KnowledgeIntegrationRecordBuilder()

    assert builder.has_all_required_fields() is False
    assert "integration_record_id" in builder.missing_required_fields()


def test_builder_sets_single_field():
    builder = KnowledgeIntegrationRecordBuilder()
    result = builder.set_field("integration_record_id", "kir-builder-001")

    assert result is builder
    assert builder.to_draft_dict()["integration_record_id"] == "kir-builder-001"


def test_builder_rejects_unknown_field():
    builder = KnowledgeIntegrationRecordBuilder()

    with pytest.raises(ValueError):
        builder.set_field("unknown_field", "value")


def test_builder_sets_multiple_fields():
    builder = KnowledgeIntegrationRecordBuilder()
    builder.set_fields(**valid_fields())

    assert builder.has_all_required_fields() is True


def test_builder_builds_knowledge_integration_record():
    builder = KnowledgeIntegrationRecordBuilder()
    builder.set_fields(**valid_fields())

    record = builder.build()

    assert isinstance(record, KnowledgeIntegrationRecord)
    assert record.integration_record_id == "kir-builder-001"
    assert record.human_review_required is True


def test_builder_requires_all_required_fields_before_build():
    builder = KnowledgeIntegrationRecordBuilder()
    builder.set_field("integration_record_id", "kir-builder-001")

    with pytest.raises(ValueError):
        builder.build()


def test_builder_does_not_infer_missing_values():
    builder = KnowledgeIntegrationRecordBuilder()
    fields = valid_fields()
    fields.pop("provenance_reference")
    builder.set_fields(**fields)

    assert "provenance_reference" in builder.missing_required_fields()

    with pytest.raises(ValueError):
        builder.build()


def test_builder_preserves_explicit_unknown_values():
    fields = valid_fields()
    fields["source_artifact_commit"] = "unknown"
    fields["referenced_runtime_output_path"] = "not_applicable"
    fields["evidence_lineage_reference"] = "missing"
    fields["provenance_reference"] = "unknown"

    builder = KnowledgeIntegrationRecordBuilder()
    record = builder.set_fields(**fields).build()

    assert record.source_artifact_commit == "unknown"
    assert record.referenced_runtime_output_path == "not_applicable"
    assert record.evidence_lineage_reference == "missing"
    assert record.provenance_reference == "unknown"


def test_builder_respects_record_validation():
    fields = valid_fields()
    fields["human_review_required"] = False

    builder = KnowledgeIntegrationRecordBuilder()
    builder.set_fields(**fields)

    with pytest.raises(ValueError):
        builder.build()


def test_builder_does_not_claim_prohibited_authority():
    builder = KnowledgeIntegrationRecordBuilder()

    assert builder.is_review_support_only is True
    assert builder.mutates_production is False
    assert builder.creates_autonomous_decision is False