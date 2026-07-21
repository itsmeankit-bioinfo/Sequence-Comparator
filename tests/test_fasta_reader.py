from src.fasta_reader import read_fasta


def test_single_fasta():

    records = read_fasta("data/sample1.fasta")

    assert len(records) == 1

    assert records[0].identifier == "Sequence_1"

    assert records[0].sequence == "ATGCGATCGATCGATCGATCGATCGATCGATCG"


def test_multiple_records(tmp_path):

    fasta = tmp_path / "multi.fasta"

    fasta.write_text(
        ">Gene1\n"
        "ATGC\n"
        ">Gene2\n"
        "CGTA\n"
    )

    records = read_fasta(str(fasta))

    assert len(records) == 2

    assert records[0].identifier == "Gene1"

    assert records[1].identifier == "Gene2"

    assert records[1].sequence == "CGTA"