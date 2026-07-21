from dataclasses import dataclass


@dataclass(slots=True)
class SequenceRecord:
    """
    Represents a biological sequence.
    """

    identifier: str
    sequence: str
    description: str = ""

    @property
    def length(self) -> int:
        """Return sequence length."""
        return len(self.sequence)

    @property
    def gc_content(self) -> float:
        """Return GC percentage."""
        if not self.sequence:
            return 0.0

        gc = self.sequence.count("G") + self.sequence.count("C")
        return round((gc / self.length) * 100, 2)

    @property
    def at_content(self) -> float:
        """Return AT percentage."""
        if not self.sequence:
            return 0.0

        at = self.sequence.count("A") + self.sequence.count("T")
        return round((at / self.length) * 100, 2)

    @property
    def is_dna(self) -> bool:
        """Return True if the sequence is DNA."""
        return "U" not in self.sequence

    @property
    def is_rna(self) -> bool:
        """Return True if the sequence is RNA."""
        return "U" in self.sequence


@dataclass(slots=True)
class Mismatch:
    """
    Represents a mismatch between two sequences.
    """

    position: int
    reference: str
    observed: str


@dataclass(slots=True)
class ComparisonResult:
    """
    Stores the result of comparing two sequences.
    """

    matches: int
    mismatches: int
    identity: float
    mismatches_list: list[Mismatch]