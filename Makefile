PYTHONPATH := src

dev:
	PYTHONPATH=$(PYTHONPATH) uv run uvicorn copilot.main:app --reload

test:
	PYTHONPATH=$(PYTHONPATH) uv run pytest

lint:
	uv run ruff check .

format:
	uv run black .

typecheck:
	uv run mypy src

all: format lint test