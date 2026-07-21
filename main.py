from src.comparator import compare_sequences
from src.fasta_reader import read_fasta
from src.mutation import mutation_summary

for mismatch in result.mismatches_list:

    print("\nMutation Summary")
print("-" * 40)

for mutation in mutation_summary(result):
    print(mutation)

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

    if result.mismatches_list:
        print("\nMismatch Positions")
        print("-" * 40)

        for mismatch in result.mismatches_list:
            print(
                f"Position {mismatch.position}: "
                f"{mismatch.reference} → {mismatch.observed}"
            )
    else:
        print("\nNo mismatches found.")


if __name__ == "__main__":
    main()