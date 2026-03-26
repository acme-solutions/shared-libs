.PHONY: install test lint dev

install:
	pip install -r requirements.txt

test:
	pytest tests/ -v

lint:
	ruff check src/ tests/

dev:
	uvicorn src.main:app --reload --port 8080
