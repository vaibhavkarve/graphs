list:
    @just --list

install:
    uv venv
    uv pip install -e .

lint:
    ruff check graphs tests

typecheck:
    pyright graphs
    mypy graphs

test:
    pytest

all: lint typecheck test

notebook:
    marimo run

watch:
    pytest --maxfail=1 --disable-warnings -x -q --tb=short --looponfail
