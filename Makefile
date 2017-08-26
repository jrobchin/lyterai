server:
	python manage.py runserver 0.0.0.0:8000

env:
	source activate openaihub

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

makemigrate:
	python manage.py makemigrations
	python manage.py migrate

shell:
	python manage.py shell

