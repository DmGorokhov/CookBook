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

run-celery:
	 poetry run celery -A cook_book worker --loglevel=info & celery -A cook_book flower --port=5555

run-redis:
	 redis-server --daemonize yes

start-server:
	poetry run python manage.py runserver 0.0.0.0:8000

start-dev: run-redis start-server

lint:
		poetry run flake8 cook_book

test:
		poetry run ./manage.py test

shell:
		poetry run ./manage.py shell