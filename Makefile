.PHONY: install test

install:
	brew bundle --file Brewfile
	pip install -e .
	./scripts/setup_local_llm.sh

test:
	pytest --cov=src/agentic_seek -q
