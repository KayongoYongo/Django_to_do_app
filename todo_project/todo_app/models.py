from django.db import models

# Create your models here.

# A model for a todo list
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
