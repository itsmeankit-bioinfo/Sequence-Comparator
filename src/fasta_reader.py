from pathlib import Path


class FASTAReader:
    """Reads DNA/RNA sequences from FASTA files."""

    @staticmethod
    def read(file_path):
        """
        Reads sequences from a FASTA file.

        Returns:
            list of dictionaries:
            [
                {
                    "id": "...",
                    "sequence": "ATGC..."
                }
            ]
        """

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        sequences = []

        current_id = None
        current_sequence = []

        with open(file_path, "r") as fasta:

            for line in fasta:

                line = line.strip()

                if not line:
                    continue

                if line.startswith(">"):

                    if current_id is not None:

                        sequences.append(
                            {
                                "id": current_id,
                                "sequence": "".join(current_sequence).upper(),
                            }
                        )

                    current_id = line[1:]
                    current_sequence = []

                else:

                    current_sequence.append(line)

        if current_id is not None:

            sequences.append(
                {
                    "id": current_id,
                    "sequence": "".join(current_sequence).upper(),
                }
            )

        return sequences