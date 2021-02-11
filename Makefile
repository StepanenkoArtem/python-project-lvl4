test:
	poetry run python -m pytest tests -vv

lint:
	poetry run flake8 simpletodo

devserver:
	poetry run ./manage.py runserver

migrate:
	poetry run ./manage.py makemigrations && poetry run ./manage.py migrate
.PHONY:
	test lint devserver migrate