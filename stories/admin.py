from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Story
from .models import WordsmithUser

# Register your models here.
admin.site.register(Story)
admin.site.register(WordsmithUser)
