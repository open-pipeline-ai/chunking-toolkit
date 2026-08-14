# Document Processing Toolkit

A reusable, modular toolkit for processing structured content from
documents and knowledge-base sources.

The toolkit is designed to support heterogeneous sources such as PDFs,
Markdown, LaTeX, DOCX, and knowledge-base systems, while providing
common building blocks that can be reused across applications.

Potential applications include document analysis, information extraction,
search, retrieval-augmented generation (RAG), and consistency checking.

## Installation

### For Users

```bash
pip install document-processing-toolkit
```

### For Development

1. Clone the repository:
```bash
git clone https://github.com/open-pipeline-ai/document-processing-toolkit.git
cd document-processing-toolkit
```

2. Install uv (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Create and activate a virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

4. Install the package in editable mode with dev dependencies:
```bash
uv pip install -e ".[dev]"
```

5. Install pre-commit hooks:
```bash
pre-commit install
```

6. Verify installation:
```bash
which python  # Should point to .venv/bin/python
uv pip list
```

## Development

### Running Tests

For quick local testing:

```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_document.py

# Run tests matching a keyword
pytest -k "document"
```


### Running Tests Across Python Versions

Nox runs the test suite across all Python versions configured in
`noxfile.py`:

```bash
# Run the default Nox sessions (tests + lint)
nox

# Run tests on a specific Python version
nox -s tests-3.12

# Pass arguments to pytest
nox -s tests -- -v
```

The Nox test session also generates test coverage reports, including a
terminal summary and an HTML report.

### Code Quality

```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Run linting
nox -s lint

# Run formatting
nox -s format
```

## Project Structure

```
document-processing-toolkit/
├── src/
│   └── document_processing_toolkit/     # Main package
│       └── __init__.py
├── tests/                    # Test files
├── pyproject.toml           # Project configuration
└── README.md               # This file
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## License

This project is licensed under the GNU Lesser General Public License v3.0 or later (LGPLv3+) - see the [LICENSE](LICENSE) file for details.
