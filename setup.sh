#!/bin/bash

docker-compose -f docker-compose.yml build

# create django api project
#docker-compose run django django-admin.py startproject api .
#docker-compose run django python manage.py migrate
docker-compose run django python manage.py createsuperuser
