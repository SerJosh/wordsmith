from django.contrib.auth.models import User
from django.db import models
# from django_summernote.widgets import SummernoteWidget


# Create your models here.
# class WordsmithUser (models.Model):
#     name = models.CharField(max_length=20)
#     email = models.EmailField('User Email', max_length=40)

#     def __str__(self):
#         return self.name

class Story(models.Model):
    Title = models.CharField('Title', max_length=20)
    Story_Cover = models.ImageField(null=True, blank=True, upload_to="images/")
    Auther = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Blurb = models.CharField('Blurb', max_length=200, blank=True)
    Content = models.TextField('Short Story', max_length=50000)


    def __str__(self):
        return self.Title
