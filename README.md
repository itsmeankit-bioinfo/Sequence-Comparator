# 🧬 Sequence Comparator

> A professional Python toolkit for comparing DNA and RNA sequences with detailed statistics, mutation detection, and similarity analysis.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange.svg)

---

## 📖 Overview

Sequence Comparator is an open-source bioinformatics tool designed to compare DNA and RNA sequences efficiently. It provides sequence statistics, similarity analysis, mutation detection, and detailed comparison reports through a clean and modular Python implementation.

This project is being developed as part of the **GenomeInsight** ecosystem with a focus on clean architecture, testability, and professional software engineering practices.

---

## ✨ Features

### Current Features

- Read FASTA files
- Support for single-sequence FASTA
- DNA/RNA sequence validation
- Modular project architecture

### Planned Features

- Multi-FASTA support
- Sequence statistics
- GC% and AT% calculation
- Match and mismatch analysis
- Similarity percentage
- Mutation detection
- Pairwise sequence alignment
- Report generation (TXT, CSV, HTML)
- Protein sequence comparison
- Rich command-line interface

---

## 📂 Project Structure

```text
SequenceComparator/
│
├── data/
├── output/
├── src/
│   ├── __init__.py
│   ├── comparator.py
│   ├── fasta_reader.py
│   ├── report.py
│   ├── statistics.py
│   └── validator.py
│
├── tests/
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── main.py
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SequenceComparator.git

cd SequenceComparator
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application

```bash
python main.py
```

Future versions will support

```bash
python main.py compare data/sample1.fasta data/sample2.fasta
```

---

## 🧬 Example Output

```text
========================================
Sequence Comparator
========================================

Sequence 1 Length : 4823 bp
Sequence 2 Length : 4823 bp

Similarity : 99.82%

Matches : 4814
Mismatches : 9

Mutations Found : 9
```

---

## 🛣️ Roadmap

### Version 0.1
- Project initialization
- FASTA parser

### Version 0.2
- Sequence statistics

### Version 0.3
- Comparison engine

### Version 0.4
- Mutation detection

### Version 0.5
- Pairwise alignment

### Version 1.0
- Stable production release

---

## 🧪 Testing

Run all tests

```bash
pytest
```

---

## 🤝 Contributing

Contributions are welcome.

Please read the **CONTRIBUTING.md** guide before submitting issues or pull requests.

---

## 📄 License

This project is licensed under the MIT License.

See the **LICENSE** file for details.

---

## 👨‍💻 Author

Ankit Raj

M.Sc. Bioinformatics

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.

It helps support future development.