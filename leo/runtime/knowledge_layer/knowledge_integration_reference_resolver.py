"""Reference resolver for the LEO Knowledge Layer Runtime.

The resolver checks whether explicitly declared references can be resolved
inside an approved reference catalog. It does not infer, fabricate, fetch,
mutate, or certify references.

Resolution results are review-support artifacts only.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ReferenceResolutionResult:
    """Read-only result of resolving one reference."""

    reference_type: str
    reference_value: str
    resolved: bool
    resolution_status: str
    resolved_target: str
    reviewer_note: str

    def to_dict(self) -> dict[str, Any]:
        """Return a plain dictionary representation."""

        return {
            "reference_type": self.reference_type,
            "reference_value": self.reference_value,
            "resolved": self.resolved,
            "resolution_status": self.resolution_status,
            "resolved_target": self.resolved_target,
            "reviewer_note": self.reviewer_note,
        }

    @property
    def is_review_support_only(self) -> bool:
        """Return True because resolution results support review only."""

        return True

    @property
    def mutates_source(self) -> bool:
        """Return False because reference resolution must not mutate sources."""

        return False


@dataclass
class KnowledgeIntegrationReferenceResolver:
    """Controlled read-only resolver for knowledge integration references."""

    reference_catalog: dict[str, dict[str, str]] = field(default_factory=dict)

    def resolve(self, reference_type: str, reference_value: str) -> ReferenceResolutionResult:
        """Resolve a single reference against the explicit catalog."""

        self._validate_reference(reference_type, reference_value)

        if reference_value in {"missing", "unknown", "not_applicable"}:
            return ReferenceResolutionResult(
                reference_type=reference_type,
                reference_value=reference_value,
                resolved=False,
                resolution_status=reference_value,
                resolved_target=reference_value,
                reviewer_note="Explicit unresolved value preserved without inference.",
            )

        typed_catalog = self.reference_catalog.get(reference_type, {})

        if reference_value in typed_catalog:
            return ReferenceResolutionResult(
                reference_type=reference_type,
                reference_value=reference_value,
                resolved=True,
                resolution_status="resolved",
                resolved_target=typed_catalog[reference_value],
                reviewer_note="Reference resolved from explicit catalog.",
            )

        return ReferenceResolutionResult(
            reference_type=reference_type,
            reference_value=reference_value,
            resolved=False,
            resolution_status="unresolved",
            resolved_target="missing",
            reviewer_note="Reference not found in explicit catalog.",
        )

    def resolve_many(
        self,
        references: dict[str, str],
    ) -> dict[str, ReferenceResolutionResult]:
        """Resolve multiple references by reference type."""

        if not isinstance(references, dict):
            raise TypeError("references must be a dictionary")

        return {
            reference_type: self.resolve(reference_type, reference_value)
            for reference_type, reference_value in references.items()
        }

    def has_reference(self, reference_type: str, reference_value: str) -> bool:
        """Return True when a reference exists in the explicit catalog."""

        self._validate_reference(reference_type, reference_value)

        return reference_value in self.reference_catalog.get(reference_type, {})

    def _validate_reference(self, reference_type: str, reference_value: str) -> None:
        if not isinstance(reference_type, str):
            raise TypeError("reference_type must be a string")
        if not isinstance(reference_value, str):
            raise TypeError("reference_value must be a string")
        if reference_type == "":
            raise ValueError("reference_type must not be empty")
        if reference_value == "":
            raise ValueError(
                "reference_value must not be empty; use missing, unknown, "
                "or not_applicable when unavailable"
            )

    @property
    def is_review_support_only(self) -> bool:
        """Return True to mark the resolver as review-support only."""

        return True

    @property
    def mutates_production(self) -> bool:
        """Return False because the resolver must not mutate production."""

        return False

    @property
    def creates_autonomous_decision(self) -> bool:
        """Return False because the resolver must not create decisions."""

        return False

    @property
    def infers_missing_references(self) -> bool:
        """Return False because unresolved references must remain explicit."""

        return False