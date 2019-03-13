
install: dist
	pip install -U dist/*

clean:
	rm -rf build dist __pycache__ *.egg-info src/__pycache__ src/*.egg-info

black: src setup.py
	black setup.py src tests

dist: clean black
	python setup.py bdist_wheel

requirements.txt: Pipfile
	pipenv lock -r >requirements.txt

dev-requirements.txt: Pipfile
	pipenv lock --dev -r >dev-requirements.txt

test: test install #requirements.txt dev-requirements.txt
	pytest


.PHONY: clean dist install test black
