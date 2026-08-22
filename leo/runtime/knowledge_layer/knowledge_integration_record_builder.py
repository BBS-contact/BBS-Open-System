"""Builder for KnowledgeIntegrationRecord objects.

The builder creates review-support records from explicit, caller-provided
values. It does not infer provenance, invent evidence, mutate source
artifacts, or produce institutional decisions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)


_REQUIRED_FIELDS = {
    "integration_record_id",
    "integration_record_version",
    "integration_record_status",
    "created_at",
    "source_artifact_path",
    "source_artifact_type",
    "source_artifact_status",
    "source_artifact_commit",
    "referenced_runtime_layer",
    "referenced_runtime_output_path",
    "ontology_concept_reference",
    "knowledge_architecture_reference",
    "institutional_memory_reference",
    "evidence_lineage_reference",
    "provenance_reference",
    "public_evaluation_relevance",
    "human_review_required",
}


@dataclass
class KnowledgeIntegrationRecordBuilder:
    """Controlled builder for KnowledgeIntegrationRecord.

    The builder is intentionally simple and read-only. It stores draft field
    values in memory and returns a frozen KnowledgeIntegrationRecord when all
    required fields are explicit.
    """

    values: dict[str, Any] = field(default_factory=dict)

    def set_field(self, field_name: str, value: Any) -> "KnowledgeIntegrationRecordBuilder":
        """Set a single field value and return the builder."""

        if field_name not in self.allowed_fields:
            raise ValueError(f"Unsupported KnowledgeIntegrationRecord field: {field_name}")

        self.values[field_name] = value
        return self

    def set_fields(self, **fields: Any) -> "KnowledgeIntegrationRecordBuilder":
        """Set multiple field values and return the builder."""

        for field_name, value in fields.items():
            self.set_field(field_name, value)
        return self

    def build(self) -> KnowledgeIntegrationRecord:
        """Build a KnowledgeIntegrationRecord from explicit values."""

        missing_fields = self.missing_required_fields()
        if missing_fields:
            raise ValueError(
                "Cannot build KnowledgeIntegrationRecord; missing required fields: "
                + ", ".join(sorted(missing_fields))
            )

        return KnowledgeIntegrationRecord(**self.values)

    def missing_required_fields(self) -> set[str]:
        """Return required fields that are not yet present."""

        return _REQUIRED_FIELDS.difference(self.values)

    def has_all_required_fields(self) -> bool:
        """Return True when all required fields have been provided."""

        return not self.missing_required_fields()

    def to_draft_dict(self) -> dict[str, Any]:
        """Return a copy of currently collected values."""

        return dict(self.values)

    @property
    def allowed_fields(self) -> set[str]:
        """Return all field names accepted by the builder."""

        return set(KnowledgeIntegrationRecord.__dataclass_fields__)

    @property
    def is_review_support_only(self) -> bool:
        """Return True to mark the builder as review-support only."""

        return True

    @property
    def mutates_production(self) -> bool:
        """Return False because the builder must not mutate production."""

        return False

    @property
    def creates_autonomous_decision(self) -> bool:
        """Return False because the builder must not create autonomous decisions."""

        return False