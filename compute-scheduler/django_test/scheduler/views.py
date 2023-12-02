import logging
from . import cron
from django.shortcuts import render
from .models import VirtualMachine
from django_crontab import crontab
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def pulldata(request):
    all_virtual_machine = VirtualMachine.objects.all
    #logger.info("running inside pulldata")
    cron.startapp()
    return render(request, 'home.html', {'all': all_virtual_machine})

"""""
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    startapp()
"""""