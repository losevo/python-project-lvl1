install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

test-start:
	poetry run python -m brain_games.scripts.brain_games
	
lint:
	poetry run flake8 brain_games