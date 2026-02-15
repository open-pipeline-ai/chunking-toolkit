# Chunking Toolkit

Modular toolkit for document chunking strategies with support for semantic and hierarchical segmentation.

## Installation

### For Users

```bash
pip install chunking-toolkit
```

### For Development

1. Clone the repository:
```bash
git clone https://github.com/open-pipeline-ai/chunking-toolkit.git
cd chunking-toolkit
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

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific test file
pytest tests/test_chunker.py
```

### Running Tests Across Python Versions

```bash
# Run tests across all configured Python versions
nox

# Run specific session
nox -s tests
nox -s lint
```

### Code Quality

```bash
# Run pre-commit hooks manually
pre-commit run --all-files

# Format code
black src tests
isort src tests

# Lint code
ruff check src tests
```

## Project Structure

```
chunking-toolkit/
├── src/
│   └── chunking_toolkit/     # Main package
│       └── __init__.py
├── tests/                    # Test files
├── docs/                     # Documentation
├── pyproject.toml           # Project configuration
└── README.md               # This file
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## License

This project is licensed under the GNU Lesser General Public License v3.0 or later (LGPLv3+) - see the [LICENSE](LICENSE) file for details.