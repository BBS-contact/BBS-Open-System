"""Tests for KnowledgeIntegrationRecord."""

import pytest

from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)


def build_record(**overrides):
    values = {
        "integration_record_id": "kir-001",
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
        "implementation_limitations": ["review-support only"],
        "reviewer_notes": ["initial test record"],
    }
    values.update(overrides)
    return KnowledgeIntegrationRecord(**values)


def test_record_can_be_created_with_required_fields():
    record = build_record()

    assert record.integration_record_id == "kir-001"
    assert record.human_review_required is True
    assert record.is_review_support_only is True


def test_record_rejects_unapproved_status():
    with pytest.raises(ValueError):
        build_record(integration_record_status="AUTO_APPROVED")


def test_record_requires_human_review():
    with pytest.raises(ValueError):
        build_record(human_review_required=False)


def test_record_rejects_empty_text_field():
    with pytest.raises(ValueError):
        build_record(source_artifact_path="")


def test_record_accepts_explicit_unknown_values():
    record = build_record(
        source_artifact_commit="unknown",
        referenced_runtime_output_path="not_applicable",
        evidence_lineage_reference="missing",
        provenance_reference="unknown",
    )

    assert record.source_artifact_commit == "unknown"
    assert record.referenced_runtime_output_path == "not_applicable"
    assert record.evidence_lineage_reference == "missing"
    assert record.provenance_reference == "unknown"


def test_record_rejects_non_string_text_field():
    with pytest.raises(TypeError):
        build_record(source_artifact_path=123)


def test_record_rejects_non_list_limitations():
    with pytest.raises(TypeError):
        build_record(implementation_limitations="not-a-list")


def test_record_rejects_non_string_list_items():
    with pytest.raises(TypeError):
        build_record(reviewer_notes=["valid", 123])


def test_to_dict_returns_review_package_safe_dictionary():
    record = build_record()
    data = record.to_dict()

    assert data["integration_record_id"] == "kir-001"
    assert data["human_review_required"] is True
    assert data["implementation_limitations"] == ["review-support only"]
    assert data["reviewer_notes"] == ["initial test record"]


def test_record_does_not_claim_prohibited_authority():
    record = build_record()

    assert record.is_enforcement_output is False
    assert record.is_fraud_verdict is False
    assert record.is_legal_verdict is False
    assert record.mutates_production is False