from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    desc = models.TextField(default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # I don't understand this
    def get_absolute_url(self):
        return reverse('task-create')