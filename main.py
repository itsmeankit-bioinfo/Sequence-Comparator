from src.comparator import compare_sequences
from src.fasta_reader import read_fasta
from src.mutation import mutation_summary
from src.report import generate_text_report


def main():
    print("=" * 60)
    print("🧬 Sequence Comparator v0.1.0")
    print("=" * 60)

    reference = read_fasta("data/sample1.fasta")[0]
    query = read_fasta("data/sample2.fasta")[0]

    result = compare_sequences(reference, query)

    print(f"\nReference : {reference.identifier}")
    print(f"Query     : {query.identifier}")

    print(f"\nLength    : {reference.length}")
    print(f"Matches   : {result.matches}")
    print(f"Mismatches: {result.mismatches}")
    print(f"Identity  : {result.identity}%")

    print("\nMutation Summary")
    print("-" * 40)

    if result.mismatches_list:
        for mutation in mutation_summary(result):
            print(mutation)
    else:
        print("No mutations found.")

    generate_text_report(
        reference,
        query,
        result,
        "output/comparison_report.txt",
    )

    print("\n✅ Report saved to output/comparison_report.txt")


if __name__ == "__main__":
    main()