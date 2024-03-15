from django.contrib.auth.models import User
from django.db import models
from stories.models import Story

# Create your models here.
class WordsmithUser (models.Model):
    Auther = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Name = models.CharField('Name', max_length=20)
    Bio = models.TextField('Bio', max_length=4000)
    Stories = models.ManyToManyField(Story, blank=True)

    def __str__(self):
        return self.Name