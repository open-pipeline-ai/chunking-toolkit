# Contributing to Chunking Toolkit

Contributions are always welcome, no matter how large or small. Before contributing, please read the [code of conduct](CODE_OF_CONDUCT.md).

Some guidelines to help you contribute effectively:

## Communication Style

1. Include screenshots for visual changes (if applicable).
2. Provide a detailed description in your Pull Request—leave nothing ambiguous for the reviewer.
3. Review your code first. Comment on complex or noteworthy code for the reviewer.
4. Maintain clear communication. Whether in an issue or a pull request, keep discussions open and informative.

## Development Setup

Follow the installation instructions in the [README](README.md#for-development), then return here for development workflow guidance.

**After setup, verify everything works:**
```bash
pytest  # Should run (even if no tests yet)
pre-commit run --all-files  # Should pass
```

## Development Workflow

See [README](README.md#development) for basic testing and code quality commands.

### Advanced Testing

```bash
# Run tests across all Python versions (3.10, 3.11, 3.12)
nox

# Run specific nox session
nox -s tests
nox -s lint
nox -s coverage
```

### Code Style Standards

- **Line length:** 120 characters
- **Formatter:** Black
- **Import sorting:** isort (Black-compatible profile)
- **Linter:** Ruff
- **Type hints:** Encouraged for public APIs

## Pull Requests

We actively welcome your pull requests. Linking to an existing issue is preferred.

### PR Workflow

1. **Create a feature branch from `main`:**
   ```bash
   git checkout -b feat/issue-number-add-new-thing
   ```
   
   Branch naming conventions:
   - `feat/` - New features
   - `fix/` - Bug fixes
   - `docs/` - Documentation changes
   - `refactor/` - Code refactoring
   - `test/` - Test additions/changes

2. **Make your changes:**
   - Add tests for new code where applicable
   - Update documentation for API changes
   - Ensure the test suite passes (`pytest`)
   - Resolve any lint warnings (`pre-commit run --all-files`)

3. **Commit your changes:**
   ```bash
   git add .
   git commit -m "feat: add semantic chunking strategy"
   ```
   
   Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format:
   - `feat:` - New features
   - `fix:` - Bug fixes
   - `docs:` - Documentation changes
   - `test:` - Test changes
   - `refactor:` - Code refactoring
   - `chore:` - Maintenance tasks

4. **Push your branch:**
   ```bash
   git push origin feat/issue-number-add-new-thing
   ```

5. **Create a Pull Request:**
   - Use the PR template
   - Link to the related issue
   - Provide a clear description of changes
   - Include test results if applicable
   - Add screenshots for visual changes (if applicable)

6. **Address review feedback:**
   - Make requested changes
   - Push updates to your branch
   - Re-request review when ready

### PR Requirements

- ✅ All tests pass
- ✅ Code is formatted (Black, isort)
- ✅ No linting errors (Ruff)
- ✅ Pre-commit hooks pass
- ✅ Linked to an issue
- ✅ Descriptive PR title following Conventional Commits
- ✅ Documentation updated (if needed)
- ✅ Changelog entry added (using scriv)

### PR Title Examples

- `feat: add hierarchical chunking strategy`
- `fix: correct token counting in semantic chunker`
- `docs: add examples for custom chunking strategies`
- `test: add integration tests for chunker API`
- `refactor: simplify metadata handling`

### Work in Progress

Use GitHub draft pull request feature to indicate ongoing work. This will disable the merge button until the PR is ready for review.

## Changelog Management

This project uses [scriv](https://scriv.readthedocs.io/) for changelog management.

### Adding a Changelog Entry

When making a significant change, create a changelog fragment:

```bash
# Create a new changelog fragment
scriv create

# This creates a file in changelog.d/
# Edit the file to describe your changes
```

**Categories:**
- `Added` - New features
- `Changed` - Changes in existing functionality
- `Deprecated` - Soon-to-be removed features
- `Removed` - Removed features
- `Fixed` - Bug fixes
- `Security` - Security fixes

**Example fragment:**
```markdown
### Added

- Semantic chunking strategy with configurable similarity thresholds

### Fixed

- Token counting edge case in long documents
```

## Testing Guidelines

### Writing Tests

- Place tests in the `tests/` directory
- Mirror the structure of `src/chunking_toolkit/`
- Name test files with `test_` prefix (e.g., `test_chunker.py`)
- Use descriptive test function names (e.g., `test_semantic_chunker_handles_empty_input`)

### Test Structure

```python
import pytest
from chunking_toolkit import Chunker

def test_chunker_basic_functionality():
    """Test that chunker processes simple text correctly."""
    chunker = Chunker()
    result = chunker.chunk("Sample text")
    assert len(result) > 0
    assert result[0].text == "Sample text"

def test_chunker_with_invalid_input():
    """Test that chunker handles invalid input gracefully."""
    chunker = Chunker()
    with pytest.raises(ValueError):
        chunker.chunk(None)
```

### Running Specific Tests

```bash
# Run a specific test file
pytest tests/test_chunker.py

# Run a specific test function
pytest tests/test_chunker.py::test_chunker_basic_functionality

# Run tests matching a pattern
pytest -k "semantic"
```

## Issues

To contribute based on an open issue:

1. **Find an issue** - Browse [open issues](https://github.com/open-pipeline-ai/chunking-toolkit/issues)
2. **Assign yourself** - Comment `.take` or ask to be assigned
3. **Start work** - Create a branch and follow the PR workflow above

### Good First Issues

For first-time contributors, look for issues labeled:
- `good first issue` - Beginner-friendly tasks
- `help wanted` - Issues where contributions are especially welcome
- `documentation` - Documentation improvements

### Reporting Bugs

When reporting bugs, please include:
- Python version (`python --version`)
- Package version (`uv pip show chunking-toolkit`)
- Minimal reproducible example
- Expected vs. actual behavior
- Error messages and stack traces

### Requesting Features

When requesting features, please include:
- Use case description
- Proposed API or interface
- Alternative solutions considered
- Willingness to contribute implementation

## Code Review Process

1. **All PRs require review** - At least one approval before merging
2. **CI must pass** - All automated checks must succeed
3. **Respond promptly** - Address feedback within a reasonable timeframe
4. **Be respectful** - Constructive criticism helps everyone learn

## Getting Help

- **Questions?** Open a [discussion](https://github.com/open-pipeline-ai/chunking-toolkit/discussions)
- **Stuck?** Comment on the relevant issue
- **Need clarification?** Ask in your PR

All questions are welcome!

## License

By contributing to this project, you agree to license your contributions under the [GNU Lesser General Public License v3 (LGPLv3)](LICENSE).

---

Thank you for contributing to Chunking Toolkit! 🎉