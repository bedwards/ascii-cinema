.PHONY: install install-dev test test-cov lint format type-check clean help

help:
	@echo "ASCII Cinema - Development Commands"
	@echo ""
	@echo "install          Install package in editable mode"
	@echo "install-dev      Install package with development dependencies"
	@echo "test             Run tests"
	@echo "test-cov         Run tests with coverage report"
	@echo "lint             Run linting checks"
	@echo "format           Format code with black"
	@echo "type-check       Run type checking with mypy"
	@echo "clean            Remove build artifacts and cache files"
	@echo "all              Run format, lint, type-check, and test"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev,video]"

test:
	pytest -v

test-cov:
	pytest --cov=ascii_cinema --cov-report=html --cov-report=term-missing

lint:
	ruff check ascii_cinema tests

format:
	black ascii_cinema tests

type-check:
	mypy ascii_cinema

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

all: format lint type-check test
