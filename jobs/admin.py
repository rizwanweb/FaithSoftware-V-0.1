from django.contrib import admin

from .models import Job, PID
# Register your models here.


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('jobNo', 'client', 'item', 'lc','vessel', 'bl', 'created')

@admin.register(PID)
class PIDAdmin(admin.ModelAdmin):
    list_display = ('PIDNo', 'client', 'item', 'lc','vessel', 'bl', 'created')