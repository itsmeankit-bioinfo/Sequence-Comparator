"""
Utilities for sequence statistics.
"""

from collections import Counter

from .models import SequenceRecord


def count_bases(record: SequenceRecord) -> dict[str, int]:
    """
    Count the occurrence of each nucleotide.

    Args:
        record: A SequenceRecord object.

    Returns:
        Dictionary containing nucleotide counts.
    """
    return dict(Counter(record.sequence))


def sequence_summary(record: SequenceRecord) -> dict:
    """
    Generate a summary of a sequence.

    Args:
        record: A SequenceRecord object.

    Returns:
        Dictionary containing sequence statistics.
    """
    return {
        "Identifier": record.identifier,
        "Length": record.length,
        "GC (%)": record.gc_content,
        "AT (%)": record.at_content,
        "Type": "DNA" if record.is_dna else "RNA",
        "Base Counts": count_bases(record),
    }