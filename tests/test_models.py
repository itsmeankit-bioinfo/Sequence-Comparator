from src.models import SequenceRecord


def test_length():
    record = SequenceRecord("gene", "ATGC")
    assert record.length == 4


def test_gc_content():
    record = SequenceRecord("gene", "GGCC")
    assert record.gc_content == 100.0


def test_at_content():
    record = SequenceRecord("gene", "AATT")
    assert record.at_content == 100.0


def test_is_dna():
    record = SequenceRecord("gene", "ATGC")
    assert record.is_dna


def test_is_rna():
    record = SequenceRecord("gene", "AUGC")
    assert record.is_rna