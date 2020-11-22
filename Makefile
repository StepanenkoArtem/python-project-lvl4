test:
	poetry run pytest simpletodo/tests -vv

lint:
	poetry run flake8 simpletodo

devserver:
	poetry run python -m simpletodo/manage.py runserver

.PHONY:
	test lint devserver