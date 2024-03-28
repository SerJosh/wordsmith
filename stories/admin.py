from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Story

# Categorisation for admin
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'auther',)
    ordering = ('title',)
    search_fields = ('title',)
