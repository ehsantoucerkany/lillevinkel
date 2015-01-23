.PHONY: all
all: update migrate

.PHONY: run
run:
	python manage.py runserver

.PHONY: run-ext
run-ext:
	python manage.py runserver 0.0.0.0:8000

.PHONY: update
update:
	pip install -r requirements.txt

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: shell
shell:
	python manage.py shell

.PHONY: test
test:
	python manage.py test
