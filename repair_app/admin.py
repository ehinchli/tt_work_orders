from django.contrib import admin
from .models import WorkOrder, Client, Device
# Register your models here.

admin.site.register(WorkOrder)
admin.site.register(Client)
admin.site.register(Device)

