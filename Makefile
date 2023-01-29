setup_test_db:
	sh db/test/import_schema.sh
	sh db/test/insert_seeds.sh

pytest:
	pytest --cov --cov-report term-missing -n 2
