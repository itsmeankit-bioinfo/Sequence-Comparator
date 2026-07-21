# Contributing to Sequence Comparator

First off, thank you for considering contributing to Sequence Comparator! 🎉

We welcome contributions that improve the project, fix bugs, enhance documentation, or introduce new bioinformatics features.

---

# Development Philosophy

This project aims to provide a clean, educational, and professional implementation of DNA and RNA sequence comparison tools.

Our goals are:

- Write clean and readable Python code.
- Follow modular software architecture.
- Maintain high test coverage.
- Keep documentation up to date.
- Build features incrementally through sprint-based development.

---

# Getting Started

## 1. Fork the Repository

Click the **Fork** button on GitHub.

## 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/SequenceComparator.git

cd SequenceComparator
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Project Structure

```text
SequenceComparator/
│
├── data/
├── output/
├── src/
├── tests/
├── README.md
├── requirements.txt
└── main.py
```

---

# Development Workflow

We follow a sprint-based workflow.

For every new feature:

1. Create a new branch.
2. Implement the feature.
3. Write or update tests.
4. Run all tests.
5. Update documentation if required.
6. Commit using Conventional Commits.
7. Open a Pull Request.

---

# Coding Standards

Please follow these guidelines:

- Python 3.11+
- Follow PEP 8 style guide
- Use meaningful variable names
- Add type hints where appropriate
- Write Google-style docstrings
- Keep functions focused on a single responsibility

Example:

```python
def calculate_gc_content(sequence: str) -> float:
    """
    Calculate the GC content of a nucleotide sequence.

    Args:
        sequence: DNA or RNA sequence.

    Returns:
        GC percentage as a float.
    """
```

---

# Testing

Run all tests before submitting changes.

```bash
pytest
```

New features should include appropriate unit tests whenever possible.

---

# Commit Messages

We follow the Conventional Commits specification.

Examples:

```text
feat: add FASTA parser

fix: handle empty FASTA files

docs: update README

test: add FASTA parser tests

refactor: simplify comparison engine
```

---

# Pull Requests

Please ensure that your pull request:

- Includes a clear description
- References related issues (if applicable)
- Passes all tests
- Does not introduce unrelated changes

Small, focused pull requests are preferred over large ones.

---

# Reporting Issues

If you discover a bug, please include:

- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior

---

# Feature Requests

Feature requests are welcome.

Please describe:

- The problem you're trying to solve
- Your proposed solution
- Why it would benefit the project

---

# Questions

If you're unsure about anything, feel free to open an issue for discussion before starting work.

---

Thank you for helping improve Sequence Comparator! 🧬