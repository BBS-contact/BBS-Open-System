"""Tests for KnowledgeIntegrationReferenceResolver."""

import pytest

from leo.runtime.knowledge_layer.knowledge_integration_reference_resolver import (
    KnowledgeIntegrationReferenceResolver,
    ReferenceResolutionResult,
)


def catalog():
    return {
        "ontology_concept_reference": {
            "knowledge_layer_runtime_integration": "foundation/engineering_ontology/LEO_KNOWLEDGE_LAYER_RUNTIME_INTEGRATION_SPEC.md",
        },
        "knowledge_architecture_reference": {
            "LEO_KNOWLEDGE_MODEL.md": "foundation/knowledge_architecture/LEO_KNOWLEDGE_MODEL.md",
        },
        "institutional_memory_reference": {
            "foundation/institutional_memory": "foundation/institutional_memory",
        },
        "referenced_runtime_layer": {
            "leo/runtime/process_mode": "leo/runtime/process_mode",
            "leo/runtime/anomaly_library": "leo/runtime/anomaly_library",
        },
    }


def test_resolver_resolves_known_reference():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    result = resolver.resolve(
        "referenced_runtime_layer",
        "leo/runtime/process_mode",
    )

    assert isinstance(result, ReferenceResolutionResult)
    assert result.resolved is True
    assert result.resolution_status == "resolved"
    assert result.resolved_target == "leo/runtime/process_mode"


def test_resolver_marks_unknown_reference_as_unresolved():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    result = resolver.resolve(
        "referenced_runtime_layer",
        "leo/runtime/unknown_layer",
    )

    assert result.resolved is False
    assert result.resolution_status == "unresolved"
    assert result.resolved_target == "missing"


def test_resolver_preserves_explicit_unknown_values():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    result = resolver.resolve("provenance_reference", "unknown")

    assert result.resolved is False
    assert result.resolution_status == "unknown"
    assert result.resolved_target == "unknown"


def test_resolver_preserves_explicit_missing_values():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    result = resolver.resolve("evidence_lineage_reference", "missing")

    assert result.resolved is False
    assert result.resolution_status == "missing"
    assert result.resolved_target == "missing"


def test_resolver_preserves_not_applicable_values():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    result = resolver.resolve("referenced_runtime_output_path", "not_applicable")

    assert result.resolved is False
    assert result.resolution_status == "not_applicable"
    assert result.resolved_target == "not_applicable"


def test_resolver_rejects_empty_reference_type():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    with pytest.raises(ValueError):
        resolver.resolve("", "leo/runtime/process_mode")


def test_resolver_rejects_empty_reference_value():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    with pytest.raises(ValueError):
        resolver.resolve("referenced_runtime_layer", "")


def test_resolver_rejects_non_string_reference_type():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    with pytest.raises(TypeError):
        resolver.resolve(123, "leo/runtime/process_mode")


def test_resolver_rejects_non_string_reference_value():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    with pytest.raises(TypeError):
        resolver.resolve("referenced_runtime_layer", 123)


def test_resolver_resolves_many_references():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    results = resolver.resolve_many(
        {
            "referenced_runtime_layer": "leo/runtime/process_mode",
            "provenance_reference": "unknown",
        }
    )

    assert results["referenced_runtime_layer"].resolved is True
    assert results["provenance_reference"].resolution_status == "unknown"


def test_resolver_rejects_non_dict_batch():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    with pytest.raises(TypeError):
        resolver.resolve_many(["not", "a", "dict"])


def test_has_reference_reports_catalog_presence():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    assert resolver.has_reference("referenced_runtime_layer", "leo/runtime/process_mode") is True
    assert resolver.has_reference("referenced_runtime_layer", "leo/runtime/missing") is False


def test_resolution_result_to_dict_is_review_safe():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    result = resolver.resolve("provenance_reference", "unknown")
    data = result.to_dict()

    assert data["reference_type"] == "provenance_reference"
    assert data["reference_value"] == "unknown"
    assert data["resolved"] is False
    assert data["resolution_status"] == "unknown"


def test_resolver_does_not_claim_prohibited_authority():
    resolver = KnowledgeIntegrationReferenceResolver(reference_catalog=catalog())

    assert resolver.is_review_support_only is True
    assert resolver.mutates_production is False
    assert resolver.creates_autonomous_decision is False
    assert resolver.infers_missing_references is False