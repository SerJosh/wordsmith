from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_stories, name = "index"),
    path('', views.create_story),
    # path('stories', views.all_stories, name = 'story-list'),
    path('create_story', views.create_story, name = 'create-story'),
    path('view_story/<story_id>', views.view_story, name = 'view-story'),
    path('edit_story/<story_id>', views.edit_story, name = 'edit-story'),
]

