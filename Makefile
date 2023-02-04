setup_development_db:
	cd db && poetry run alembic upgrade head

setup_test_db:
	sh db/test/import_schema.sh
	sh db/test/insert_seeds.sh

test:
	poetry run pytest --cov --cov-report term-missing -n 2

clear_pycache:
	find . | grep -E __pycache__ | xargs rm -rf

lint:
	poetry run isort . && poetry run black . && poetry run flake8
