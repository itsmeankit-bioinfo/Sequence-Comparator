import pytest

from src.exceptions import InvalidSequenceError
from src.validator import validate_sequence


def test_valid_dna():
    validate_sequence("ATGCATGC")


def test_valid_rna():
    validate_sequence("AUGCAUGC", "RNA")


def test_lowercase_sequence():
    validate_sequence("atgc")


def test_sequence_with_n():
    validate_sequence("ATGCNNNN")


def test_invalid_dna():
    with pytest.raises(InvalidSequenceError):
        validate_sequence("ATGX")


def test_invalid_rna():
    with pytest.raises(InvalidSequenceError):
        validate_sequence("AUGTX", "RNA")


def test_invalid_molecule_type():
    with pytest.raises(ValueError):
        validate_sequence("ATGC", "Protein")