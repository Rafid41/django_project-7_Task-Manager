# tasks\admin.py
from django.contrib import admin
from tasks.models import Task, Images

# Register your models here.
admin.site.register(Task)
admin.site.register(Images)