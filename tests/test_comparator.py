import pytest

from src.comparator import compare_sequences
from src.models import SequenceRecord


def test_identical_sequences():

    seq1 = SequenceRecord("A", "ATGC")
    seq2 = SequenceRecord("B", "ATGC")

    result = compare_sequences(seq1, seq2)

    assert result.matches == 4
    assert result.mismatches == 0
    assert result.identity == 100.0


def test_single_mismatch():

    seq1 = SequenceRecord("A", "ATGC")
    seq2 = SequenceRecord("B", "ATGT")

    result = compare_sequences(seq1, seq2)

    assert result.matches == 3
    assert result.mismatches == 1
    assert result.identity == 75.0

    mismatch = result.mismatches_list[0]

    assert mismatch.position == 4
    assert mismatch.reference == "C"
    assert mismatch.observed == "T"


def test_different_lengths():

    seq1 = SequenceRecord("A", "ATGC")
    seq2 = SequenceRecord("B", "ATGCA")

    with pytest.raises(ValueError):
        compare_sequences(seq1, seq2)