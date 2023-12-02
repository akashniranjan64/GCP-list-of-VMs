from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.

class VirtualMachine(models.Model):

    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    vm_name = models.CharField(max_length=255)
    vm_schedule_temp = models.CharField(max_length=255)
    vm_sch_start = models.TimeField()
    vm_sch_stop = models.TimeField()
    vm_status = models.BooleanField()

    def __str__(self):
        return self.vm_name