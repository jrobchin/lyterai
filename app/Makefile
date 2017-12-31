clean:
	find . -name '*.pyc' -delete

# Backend
production:
	gunicorn lyterai.wsgi --bind 0.0.0.0:8000 

server:
	python manage.py runserver 0.0.0.0:8000

shell:
	python manage.py shell

seed:
	# Add each seeder command here
	python manage.py hub_seed

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

makemigrate:
	python manage.py makemigrations
	python manage.py migrate

# Front-End
front:
	gulp

# Docker
pybash:
	sudo docker-compose run python bash

dbuild:
	sudo docker-compose build

dup:
	sudo docker-compose up

dupd:
	sudo docker-compose up -d
	
ddown:
	sudo docker-compose down

dlogs:
	docker-compose logs -f

python-bash:
	sudo docker-compose run python bash

