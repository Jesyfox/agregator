from os import environ


REDIS_HOST = "localhost"  # TODO: 'redis' for docker (?)
REDIS_PORT = 6379
BROKER_URL = environ.get('REDIS_URL', "redis://{host}:{port}/0".format(
    host=REDIS_HOST, port=str(REDIS_PORT)))
CELERY_RESULT_BACKEND = BROKER_URL
