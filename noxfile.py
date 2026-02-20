"""Nox sessions for chunking-toolkit."""

import nox

# Default sessions to run when you just type `nox`
nox.options.sessions = ["tests", "lint"]


@nox.session(python=["3.10", "3.11", "3.12"])
def tests(session):
    """Run tests with pytest."""
    session.install(".[dev]")
    session.run(
        "pytest",
        "--cov=chunking_toolkit",
        "--cov-report=term-missing",
        "--cov-report=html",
        *session.posargs,
    )


@nox.session
def lint(session):
    """Run linting checks."""
    session.install(".[dev]")
    session.run("ruff", "check", ".")
    session.run("ruff", "format", "--check", ".")


@nox.session
def format(session):
    """Auto-format code."""
    session.install(".[dev]")
    session.run("ruff", "format", ".")
