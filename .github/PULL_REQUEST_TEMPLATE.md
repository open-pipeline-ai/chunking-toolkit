<!--
     For Work In Progress Pull Requests, please use the Draft PR feature.
     
     Before submitting, ensure you've done the following:
     - 📖 Read the [Contributing Guide](CONTRIBUTING.md)
     - 📖 Read the [Code of Conduct](CODE_OF_CONDUCT.md)
     - 👷‍♀️ Create small PRs focusing on a single feature or fix
     - ✅ Provide tests for your changes
     - 📝 Write descriptive commit messages following Conventional Commits
     - 📗 Update documentation where applicable
     - 🧹 Ensure code passes all pre-commit hooks and linting
     - 📋 Add a changelog entry using `scriv create`
     
     NOTE: All PRs require at least one approval and passing CI checks before merging.
-->

## What type of PR is this? (check all applicable)

- [ ] Refactor
- [ ] Feature
- [ ] Bug Fix
- [ ] Optimization
- [ ] Documentation Update
- [ ] CI / DevOps
- [ ] Security

## Description

_Provide a clear and concise description of what this PR does. Explain the problem and the solution._

## Related Issues

<!--
Link related issues using GitHub/GitLab keywords.
Examples:
- "Closes #123" (closes issue on merge)
- "Fixes #456" (fixes issue on merge)
- "Related to #789" (links but doesn't close)
-->

- Related Issue #
- Closes #

## Changes Made

_List the key changes in this PR:_

- 
- 
- 

## Testing

### How Has This Been Tested?

_Describe the tests you ran and how to reproduce them:_

```bash
# Example test commands
pytest tests/test_chunker.py
pytest --cov
```

### Test Configuration

- **Python version(s):** 
- **Operating System:** 
- **Tested with nox:** [ ] Yes [ ] No

## Added/Updated Tests?

- [ ] Yes, added tests
- [ ] Yes, updated existing tests
- [ ] No, and here's why: _explain_
- [ ] I need help with writing tests

## Checklist

- [ ] Code follows the project's style guidelines (Black, isort, Ruff)
- [ ] Pre-commit hooks pass (`pre-commit run --all-files`)
- [ ] All tests pass locally (`pytest`)
- [ ] Added/updated documentation for any API changes
- [ ] Added changelog entry (`scriv create`)
- [ ] PR title follows Conventional Commits format (e.g., `feat:`, `fix:`)
- [ ] Linked to related issue(s)

## Breaking Changes

- [ ] This PR introduces breaking changes

_If yes, describe the breaking changes and migration path:_

## Additional Context

_Add any other context about the PR here, such as:_
- Design decisions made
- Alternative approaches considered
- Known limitations or future improvements
- Dependencies added or update

## Screenshots/Examples (if applicable)

_For API changes, provide before/after examples:_

**Before:**
```python
# Old usage
```

**After:**
```python
# New usage
```

## [Optional] Performance Impact

_If this PR affects performance, describe the impact:_

- [ ] Performance improved
- [ ] Performance unchanged
- [ ] Performance degraded (provide justification)

## [Optional] Post-Merge Tasks

_Are there any follow-up tasks after this PR is merged?_

- [ ] Update documentation site
- [ ] Notify users of breaking changes
- [ ] Create follow-up issues


## [Optional] What GIF best describes this PR or how it makes you feel?

![alt_text](gif_link)


---

**For Reviewers:**

- [ ] Code quality looks good
- [ ] Tests are adequate
- [ ] Documentation is clear
- [ ] No security concerns
- [ ] Approved for merge