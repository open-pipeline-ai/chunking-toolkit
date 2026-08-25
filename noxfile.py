"""Nox sessions for document-processing-toolkit."""

import nox

# Default sessions to run when you just type `nox`
nox.options.sessions = ["tests", "lint"]


def install_dev(session):
    session.run_install(
        "uv",
        "sync",
        "--extra=dev",
        "--locked",
        f"--python={session.virtualenv.location}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )


@nox.session(venv_backend="uv", python=["3.10", "3.11", "3.12"])
def tests(session):
    """Run tests with pytest."""
    install_dev(session)
    session.run(
        "pytest",
        "--cov=document_processing_toolkit",
        "--cov-report=term-missing",
        "--cov-report=html",
        *session.posargs,
    )


@nox.session(venv_backend="uv")
def lint(session):
    """Run linting checks."""
    session.install(".[dev]")
    session.run("ruff", "check", ".")
    session.run("ruff", "format", "--check", ".")


@nox.session(venv_backend="uv")
def format(session):
    """Auto-format code."""
    session.install(".[dev]")
    session.run("ruff", "format", ".")
