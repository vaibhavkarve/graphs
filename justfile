list:
    @just --list

install:
    uv venv
    uv pip install -e .

lint:
    .venv/bin/ruff check graphs tests

typecheck:
    .venv/bin/pyright graphs tests
    .venv/bin/mypy graphs tests

test:
    .venv/bin/pytest tests

all: lint typecheck test

notebook:
    .venv/bin/marimo run

watch:
    .venv/bin/pytest --maxfail=1 --disable-warnings -x -q --tb=short --looponfail
