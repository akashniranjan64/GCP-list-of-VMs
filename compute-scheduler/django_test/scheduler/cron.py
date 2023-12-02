import logging
from .models import VirtualMachine
from django.db.models import F
import datetime

logger = logging.getLogger(__name__)

def startapp():
    get_active_schedules()
    logger.info("running cron")

def get_active_schedules():
    open('project-list-db.txt', 'w')
    items = VirtualMachine.objects.annotate(('vm_name'))
    for item in items:
        logger.info(item[0])
#    logger.info(datetime_value)
#    db_time = datetime.datetime.strptime(str(datetime_value), '%H:%M:%S')
#    if (db_time.time().hour >= datetime.datetime.now().time().hour-1 or db_time.time().hour < datetime.datetime.now().time().hour):
#        logger.info(project_name)
        #get_list.get_project_list(item[1])

