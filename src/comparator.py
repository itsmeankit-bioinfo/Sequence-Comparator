"""
Sequence comparison utilities.
"""

from .models import ComparisonResult, Mismatch, SequenceRecord


def compare_sequences(
    reference: SequenceRecord,
    query: SequenceRecord,
) -> ComparisonResult:
    """
    Compare two sequences of equal length.

    Args:
        reference: First sequence.
        query: Second sequence.

    Returns:
        ComparisonResult object.

    Raises:
        ValueError:
            If sequence lengths differ.
    """

    if reference.length != query.length:
        raise ValueError(
            "Sequences must have the same length."
        )

    matches = 0

    mismatches = []

    for index, (ref, obs) in enumerate(
        zip(reference.sequence, query.sequence),
        start=1,
    ):
        if ref == obs:
            matches += 1
        else:
            mismatches.append(
                Mismatch(
                    position=index,
                    reference=ref,
                    observed=obs,
                )
            )

    total = reference.length

    identity = round((matches / total) * 100, 2)

    return ComparisonResult(
        matches=matches,
        mismatches=len(mismatches),
        identity=identity,
        mismatches_list=mismatches,
    )