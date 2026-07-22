from src.cli import create_parser
from src.fasta_reader import read_fasta
from src.statistics import sequence_summary
from src.comparator import compare_sequences
from src.report import generate_text_report
from src.mutation import mutation_summary


def stats_command(fasta_file):
    sequence = read_fasta(fasta_file)[0]
    summary = sequence_summary(sequence)

    print("\nSequence Statistics")
    print("-" * 40)

    for key, value in summary.items():
        print(f"{key}: {value}")


def compare_command(reference_file, query_file):
    reference = read_fasta(reference_file)[0]
    query = read_fasta(query_file)[0]

    result = compare_sequences(reference, query)

    print("\nComparison Result")
    print("-" * 40)
    print(f"Matches    : {result.matches}")
    print(f"Mismatches : {result.mismatches}")
    print(f"Identity   : {result.identity}%")

    if result.mismatches_list:
        print("\nMutation Summary")
        print("-" * 40)

        for mutation in mutation_summary(result):
            print(mutation)
    else:
        print("\nNo mutations found.")


def report_command(reference_file, query_file):
    reference = read_fasta(reference_file)[0]
    query = read_fasta(query_file)[0]

    result = compare_sequences(reference, query)

    generate_text_report(
        reference,
        query,
        result,
        "output/comparison_report.txt",
    )

    print("✅ Report generated successfully!")
    print("Saved to output/comparison_report.txt")


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "stats":
        stats_command(args.fasta)

    elif args.command == "compare":
        compare_command(args.reference, args.query)

    elif args.command == "report":
        report_command(args.reference, args.query)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()