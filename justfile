list:
    @just --list

init:
    uv venv
    uv pip install -r requirements.txt

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
