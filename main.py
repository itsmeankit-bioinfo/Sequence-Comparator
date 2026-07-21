from src.fasta_reader import read_fasta
from src.statistics import sequence_summary


def main():
    print("=" * 60)
    print("🧬 Sequence Comparator v0.1.0")
    print("=" * 60)

    records = read_fasta("data/sample1.fasta")

    for record in records:
        summary = sequence_summary(record)

        print(f"\nIdentifier : {summary['Identifier']}")
        print(f"Length     : {summary['Length']} bp")
        print(f"Type       : {summary['Type']}")
        print(f"GC Content : {summary['GC (%)']}%")
        print(f"AT Content : {summary['AT (%)']}%")
        print("Base Counts")

        for base, count in summary["Base Counts"].items():
            print(f"  {base}: {count}")


if __name__ == "__main__":
    main()