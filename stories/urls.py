from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_stories, name = "index"),
    path('stories/', views.all_stories, name = 'story-list'),
    path('create_story', views.create_story, name = 'create-story'),
    path('view_story/<story_id>', views.view_story, name = 'view-story'),
    path('edit_story/<story_id>', views.edit_story, name = 'edit-story'),
    path('delete_story/<story_id>', views.delete_story, name = 'delete-story'),
    path('about', views.about, name = 'about'),
]

