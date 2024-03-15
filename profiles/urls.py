from django.urls import path
from . import views

urlpatterns = [
  path('profiles', views.user_profile, name='view-profile'),
  path('edit_profile/<profile_id>', views.edit_profile, name = 'edit-profile'),
]