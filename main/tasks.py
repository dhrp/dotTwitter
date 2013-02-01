# minestrone/soup/tasks.py:

import time
from celery.task import task
from django.utils.log import logger

#celery = Celery('tasks', broker='amqp://root:qRd6ZOBl7QwmMowdpWN2@hellopython-dhrp.azva.dotcloud.net:43034')

#@task(ignore_result=True)
def lazy_job(name):
    print ("starting lazy job")

#    logger = lazy_job.get_logger()
#    logger.info('Starting the lazy job: {0}'.format(name))
#    time.sleep(5)
#    logger.info('Lazy job {0} completed'.format(name))

    print ("lazy job complete")
