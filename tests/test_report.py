from src.comparator import compare_sequences
from src.models import SequenceRecord
from src.report import generate_text_report


def test_generate_report(tmp_path):

    reference = SequenceRecord("ref", "ATGC")
    query = SequenceRecord("qry", "ATGT")

    result = compare_sequences(reference, query)

    report = tmp_path / "report.txt"

    generate_text_report(
        reference,
        query,
        result,
        str(report),
    )

    assert report.exists()

    content = report.read_text()

    assert "Sequence Comparison Report" in content
    assert "Identity" in content