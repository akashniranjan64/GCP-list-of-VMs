from django.contrib import admin

# Register your models here.

from .models import VirtualMachine
admin.site.register(VirtualMachine)