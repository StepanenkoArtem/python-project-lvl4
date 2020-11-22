test:
	poetry run pytest simpletodo/tests -vv

lint:
	poetry run flake8 simpletodo

devserver:
	poetry run simpletodo/manage.py runserver

.PHONY:
	test lint devserver