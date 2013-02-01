from celery import Celery

#celery = Celery('tasks', broker='amqp://guest@localhost//')
celery = Celery('tasks', broker='amqp://root:qRd6ZOBl7QwmMowdpWN2@hellopython-dhrp.azva.dotcloud.net:43034')


@celery.task
def add(x, y):
    return x + y


print add.delay(4, 4)