from django.contrib.auth.models import User
from django.db import models


class Story(models.Model):
    Title = models.CharField('Title', max_length=20)
    Story_Cover = models.ImageField(null=True, blank=True, upload_to="images/")
    Auther = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Blurb = models.TextField('Blurb', max_length=200, blank=True)
    Content = models.TextField('Short Story', max_length=50000)


    def __str__(self):
        return self.Title
