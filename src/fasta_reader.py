"""
Functions for reading FASTA files.
"""

from pathlib import Path

from .exceptions import FastaFormatError
from .models import SequenceRecord
from .validator import validate_sequence


def read_fasta(path: str, molecule_type: str = "DNA") -> list[SequenceRecord]:
    """
    Read a FASTA or Multi-FASTA file.

    Args:
        path: Path to the FASTA file.
        molecule_type: Either "DNA" or "RNA".

    Returns:
        A list of SequenceRecord objects.

    Raises:
        FileNotFoundError:
            If the file does not exist.
        FastaFormatError:
            If the FASTA file is malformed.
    """

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    records: list[SequenceRecord] = []

    identifier = None
    description = ""
    sequence_lines = []

    with file_path.open("r", encoding="utf-8") as fasta:

        for line in fasta:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):

                if identifier is not None:
                    sequence = "".join(sequence_lines).upper()

                    validate_sequence(sequence, molecule_type)

                    records.append(
                        SequenceRecord(
                            identifier=identifier,
                            description=description,
                            sequence=sequence,
                        )
                    )

                header = line[1:].strip()

                if not header:
                    raise FastaFormatError("Empty FASTA header found.")

                parts = header.split(maxsplit=1)

                identifier = parts[0]
                description = parts[1] if len(parts) > 1 else ""

                sequence_lines = []

            else:

                if identifier is None:
                    raise FastaFormatError(
                        "Sequence found before FASTA header."
                    )

                sequence_lines.append(line)

    if identifier is not None:

        sequence = "".join(sequence_lines).upper()

        validate_sequence(sequence, molecule_type)

        records.append(
            SequenceRecord(
                identifier=identifier,
                description=description,
                sequence=sequence,
            )
        )

    if not records:
        raise FastaFormatError("No FASTA records found.")

    return records