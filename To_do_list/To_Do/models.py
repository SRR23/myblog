from django.db import models

# Create your models here.

class TaskModel(models.Model):
    taskTitel = models.CharField(primary_key = True, max_length = 30)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)