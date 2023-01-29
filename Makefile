setup_test_db:
	sh db/test/import_schema.sh
	sh db/test/insert_seeds.sh

test:
	pytest --cov --cov-report term-missing -n 2
