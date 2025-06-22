set dotenv-path := ".envrc"

list:
    @just --list

install:
    uv venv
    uv sync

lint:
    uv run ruff format graphs tests
    uv run ruff check graphs tests

typecheck:
    uv run mypy graphs tests
    uv run pyright --threads graphs tests

test flags="-xvvs":
    uv run python -m slipcover -m pytest tests {{ flags }}

all: lint typecheck test

notebook:
    uv run marimo run

watch:
    uv run pytest --maxfail=1 --disable-warnings -x -q --tb=short --looponfail
