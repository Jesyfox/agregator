### site agregator

### docs:

tags - https://django-tagging.readthedocs.io/en/develop/#tagging-views-taggedobjectlist

writen with Python 3.6.7

### you will need:

docker

redis

postgresql

### Instalation:

### virtualenv:

`python3 -m venv venv`

`. venv/bin/activate`

`pip install -r requirements.txt`

### database:

`sudo su - postgres`

`psql`

`CREATE DATABASE agregator;`

`CREATE USER scraper WITH PASSWORD 'scraper123';`

`GRANT ALL PRIVILEGES ON DATABASE agregator TO scraper;`

run migrations: ./manage.py migrate

### run:

open 2 teminals: at first terminal:
 
 `celery -A site_parser worker --loglevel=info` 
 
at second terminal: 

`./manage.py runserver`

### docker run:

`docker-compose up`

`docker-compose exec agregator bash`
 
 `python3 site_agregator/manage.py migrate`