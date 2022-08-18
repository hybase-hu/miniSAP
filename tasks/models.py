from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    is_assigned = models.BooleanField(default=False)
    assigned_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    deadline = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    finished_date = models.DateTimeField(null=True,blank=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name




class TaskDetails(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,related_name="all_task_details")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(auto_created=True,auto_now_add=True)
    modify_desc = models.TextField()

    def __str__(self):
        return self.task.task_name + " [ " + str(self.modify_date) + " ]"



