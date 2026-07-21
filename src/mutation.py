"""
Mutation analysis utilities.
"""

from .models import ComparisonResult


def mutation_summary(result: ComparisonResult) -> list[str]:
    """
    Convert mismatches into readable mutation descriptions.

    Args:
        result: ComparisonResult object.

    Returns:
        List of mutation descriptions.
    """

    mutations = []

    for mismatch in result.mismatches_list:
        mutations.append(
            f"Position {mismatch.position}: "
            f"{mismatch.reference} → {mismatch.observed}"
        )

    return mutations