---
name: Bug Report
about: Report a bug or unexpected behavior
title: '[BUG] '
labels: bug
assignees: ''
---

## Bug Description

A clear and concise description of what the bug is.

## To Reproduce

Steps to reproduce the behavior:

1. Install version '...'
2. Run the following code '...'
3. Observe error '...'

**Minimal reproducible example:**

```python
# Paste your code here
from chunking_toolkit import Chunker

chunker = Chunker()
# ... code that triggers the bug
```

## Expected Behavior

A clear and concise description of what you expected to happen.

## Actual Behavior

What actually happened instead.

**Error message (if applicable):**

```
Paste the full error message and stack trace here
```

## Environment

Please complete the following information:

- **OS:** [e.g., Ubuntu 22.04, macOS 14, Windows 11]
- **Python version:** [e.g., 3.10.5] (run `python --version`)
- **chunking-toolkit version:** [e.g., 0.1.0] (run `uv pip show chunking-toolkit`)
- **Installation method:** [e.g., pip, uv, from source]

**Installed dependencies:**

```bash
# Run this command and paste output
uv pip list
```

## Additional Context

Add any other context about the problem here, such as:

- Does this happen consistently or intermittently?
- Did this work in a previous version?
- Are there any workarounds you've discovered?
- Links to related issues or discussions

## Possible Solution (optional)

If you have ideas about what might be causing the issue or how to fix it, please share them here.

## Checklist

- [ ] I have searched existing issues to ensure this is not a duplicate
- [ ] I have provided a minimal reproducible example
- [ ] I have included my environment details
- [ ] I have included the full error message (if applicable)
