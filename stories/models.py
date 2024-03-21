from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


class Story(models.Model):
    Title = models.CharField('Title', max_length=20)
    Story_Cover = CloudinaryField('image', default='placeholder')
    Auther = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Blurb = models.TextField('Blurb', max_length=200, blank=True)
    Content = models.TextField('Short Story', max_length=50000)
## lowercase##

    def __str__(self):
        return self.Title
