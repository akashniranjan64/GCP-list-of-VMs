import datetime
import logging

from get_list import get_project_list, get_vm_list, vm_scheduling_job
from current_time_impl import get_active_schedules
import time
import log_impl
import logging

logger = log_impl._init_logger()


"""""
def vm_start():
    current_time_impl.get_active_schedules("start")
    get_vm_list("start")

def vm_stop():
    current_time_impl.get_active_schedules("start")
    get_vm_list("stop")

while True:
    vm_start()
    time.sleep(1800)  # Sleep for 30 minutes (1800 seconds)
    vm_stop()
    time.sleep(1800)  # Sleep for 30 minutes (1800 seconds)
"""""


#current_time_impl.get_active_schedules()
#get_list.get_vm_list("stop")
def test():
    logger.info('getting active schedules for the hour')
    get_active_schedules("start")
    #get_vm_list("start")

test()