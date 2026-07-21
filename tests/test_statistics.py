from src.models import SequenceRecord
from src.statistics import count_bases, sequence_summary


def test_count_bases():
    record = SequenceRecord("gene", "AATGCC")
    counts = count_bases(record)

    assert counts["A"] == 2
    assert counts["T"] == 1
    assert counts["G"] == 1
    assert counts["C"] == 2


def test_sequence_summary():
    record = SequenceRecord("gene", "AATGCC")
    summary = sequence_summary(record)

    assert summary["Identifier"] == "gene"
    assert summary["Length"] == 6
    assert summary["Type"] == "DNA"