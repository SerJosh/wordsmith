from django.urls import path
from . import views
# from . import views

# app_name ='stories'

# urlpatterns = [
#     path('new/', views.CreateNewStory.as_view(), name='new_story'),
# ]

urlpatterns = [
    path('', views.create_story),
]
