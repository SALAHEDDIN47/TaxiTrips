.PHONY: install test sample clean

install:
	pip install -r requirements.txt

test:
	pytest -v tests/

sample:
	python scripts/make_sample.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete