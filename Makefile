install:
	poetry install

gendiff:
	poetry run gendiff

build: 
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

make lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

 test-coverage:
	poetry run coverage run -m pytest 
	poetry run coverage xml

check: selfcheck test lint

.PHONY: gendiff