from src.fasta_reader import FASTAReader


def main():

    sequences = FASTAReader.read("data/sample1.fasta")

    print("=" * 50)
    print("Sequence Comparator")
    print("=" * 50)

    for sequence in sequences:
        print(f"ID       : {sequence['id']}")
        print(f"Length   : {len(sequence['sequence'])}")
        print(f"Sequence : {sequence['sequence']}")


if __name__ == "__main__":
    main()