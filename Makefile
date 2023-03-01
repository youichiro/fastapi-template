test:
	poetry run pytest --cov --cov-report term-missing -n 2

lint:
	poetry run isort .
	poetry run black .
	poetry run flake8
	poetry run mypy .

setup_development_db:
	cd db && poetry run alembic upgrade head

setup_test_db:
	sh db/test/import_schema.sh
	sh db/test/insert_seeds.sh

clear_cache_files:
	find . | grep -E __pycache__ | xargs rm -rf
	find . | grep -E .pytest_cache | xargs rm -rf
	find . | grep -E .mypy_cache | xargs rm -rf

clear_poetry_cache:
	poetry cache clear . --all
