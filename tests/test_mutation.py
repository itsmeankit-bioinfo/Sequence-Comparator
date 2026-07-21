from src.comparator import compare_sequences
from src.models import SequenceRecord
from src.mutation import mutation_summary


def test_mutation_summary():

    reference = SequenceRecord("ref", "ATGC")
    query = SequenceRecord("qry", "ATGT")

    result = compare_sequences(reference, query)

    summary = mutation_summary(result)

    assert len(summary) == 1
    assert summary[0] == "Position 4: C → T"