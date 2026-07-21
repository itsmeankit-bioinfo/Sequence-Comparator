class FastaFormatError(Exception):
    """Raised when a FASTA file has an invalid format."""


class InvalidSequenceError(Exception):
    """Raised when a sequence contains invalid nucleotides."""