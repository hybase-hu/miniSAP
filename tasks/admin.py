from django.contrib import admin

# Register your models here.
from tasks.models import Task, TaskDetails

admin.site.register(Task)
admin.site.register(TaskDetails)