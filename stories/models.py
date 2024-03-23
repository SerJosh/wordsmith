from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


class Story(models.Model):
    title = models.CharField('Title', max_length=20)
    story_cover = CloudinaryField('Story Cover', default='placeholder')
    auther = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    blurb = models.TextField('Blurb', max_length=200, blank=True)
    content = models.TextField('Short Story', max_length=50000)
## lowercase##

    def __str__(self):
        return self.Title
