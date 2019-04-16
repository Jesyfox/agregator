site agregator

docs:

tags - https://django-tagging.readthedocs.io/en/develop/#tagging-views-taggedobjectlist

writen with Python 3.6.7

you will need:

redis

postgresql

Instalation:

virtualenv:

`python3 -m venv venv`

`. venv/bin/activate`

`pip install -r requirements.txt`

database:

`sudo su - postgres`

`psql`

`CREATE DATABASE agregator;`

`CREATE USER scraper WITH PASSWORD 'scraper123';`

`GRANT ALL PRIVILEGES ON DATABASE agregator TO scraper;`

You must be here: *your folder*/olx_rem/olx_rem

run migrations: ./manage.py migrate

open 2 teminals: at first terminal:
 
 `celery -A site_parser worker --loglevel=info` 
 
at second terminal: 

`./manage.py runserver`