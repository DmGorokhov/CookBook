MANAGE := poetry run python manage.py

install:
		@poetry install

make-migration:
		@$(MANAGE) makemigrations

migrate: make-migration
		@$(MANAGE) migrate

build: install migrate

setup: build
	echo Create a super user
	poetry run python manage.py createsuperuser

dev:
		poetry run python manage.py runserver

lint:
		poetry run flake8 cook_book

test:
		poetry run ./manage.py test

shell:
		poetry run ./manage.py shell