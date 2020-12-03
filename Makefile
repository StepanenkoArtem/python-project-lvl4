test:
	poetry run pytest simpletodo/tests -vv

lint:
	poetry run flake8 simpletodo

devserver:
	poetry run simpletodo/manage.py runserver

migrate:
	poetry run simpletodo/manage.py makemigrations && poetry run simpletodo/manage.py migrate
.PHONY:
	test lint devserver migrate