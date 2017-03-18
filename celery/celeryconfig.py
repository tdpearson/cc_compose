import os
import ssl
env = os.environ

rmq_pass = env['RABBITMQ_DEFAULT_USER']
rmq_user = env['RABBITMQ_DEFAULT_PASS']
rmq_vhost = env['RABBITMQ_DEFAULT_VHOST']

appname = "testing"
BROKER_URL = 'amqp://{0}:{1}@libmain_rabbitmq:5672/{2}'.format(rmq_user, rmq_pass, rmq_vhost)
CELERY_SEND_EVENTS = True
CELERY_TASK_RESULT_EXPIRES = None
CELERY_ACCEPT_CONTENT = ['pickle','json']
CELERY_RESULT_BACKEND = "mongodb://guest:guest@libmain_mongo:27017"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "database": "testing",
    "taskmeta_collection": "tombstone"
}
CELERY_IMPORTS = ("cybercomq",)
