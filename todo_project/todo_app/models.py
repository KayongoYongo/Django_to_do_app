from django.db import models

# Create your models here.

# A model for a todo list
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
