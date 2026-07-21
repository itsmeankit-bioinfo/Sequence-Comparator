"""
Validation utilities for biological sequences.
"""

from .exceptions import InvalidSequenceError

DNA_BASES = {"A", "T", "G", "C", "N"}
RNA_BASES = {"A", "U", "G", "C", "N"}


def validate_sequence(sequence: str, molecule_type: str = "DNA") -> None:
    """
    Validate a DNA or RNA sequence.

    Args:
        sequence: Biological sequence to validate.
        molecule_type: Either "DNA" or "RNA".

    Raises:
        InvalidSequenceError:
            If an invalid nucleotide is found.
        ValueError:
            If molecule_type is unsupported.
    """

    sequence = sequence.replace(" ", "").replace("\n", "").upper()

    if molecule_type == "DNA":
        allowed = DNA_BASES
    elif molecule_type == "RNA":
        allowed = RNA_BASES
    else:
        raise ValueError("molecule_type must be 'DNA' or 'RNA'.")

    for index, nucleotide in enumerate(sequence, start=1):
        if nucleotide not in allowed:
            raise InvalidSequenceError(
                f"Invalid nucleotide '{nucleotide}' found at position {index}."
            )