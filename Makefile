test:
	poetry run pytest */tests -vv

lint:
	poetry run flake8 simpletodo

devserver:
	poetry run ./manage.py runserver

migrate:
	poetry run ./manage.py makemigrations && poetry run ./manage.py migrate

requirements.txt:
	poetry export -o requirements.txt

.PHONY:
	test lint devserver migrate