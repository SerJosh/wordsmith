from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Story(models.Model):
    Title = models.CharField(max_length=20)
    Blurb = models.CharField(max_length=200)
    Content = models.TextField(max_length=50000)
