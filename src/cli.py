import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="SequenceComparator",
        description="A simple bioinformatics sequence comparison tool.",
    )

    subparsers = parser.add_subparsers(dest="command")

    # stats command
    stats = subparsers.add_parser(
        "stats",
        help="Show sequence statistics",
    )
    stats.add_argument("fasta")

    # compare command
    compare = subparsers.add_parser(
        "compare",
        help="Compare two FASTA files",
    )
    compare.add_argument("reference")
    compare.add_argument("query")

    # report command
    report = subparsers.add_parser(
        "report",
        help="Generate comparison report",
    )
    report.add_argument("reference")
    report.add_argument("query")

    return parser