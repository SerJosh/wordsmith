from django.urls import path
from . import views
# from . import views


urlpatterns = [
    path('', views.all_stories, name = "index"),
    path('', views.create_story),
    # path('stories', views.all_stories, name = 'story-list'),
]

