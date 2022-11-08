from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    status = models.BinaryField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)