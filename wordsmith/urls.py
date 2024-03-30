from django.contrib import admin
from django.urls import path, include
from stories.views import index
from stories.views import create_story
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler500

handler500 = 'stories.views.error_view500'
handler404 = 'stories.views.error_view404'


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('create_story/', create_story, name='create_story'),
    path('summernote/', include('django_summernote.urls')),
    path('', include('stories.urls'), name="stories-urls"),
]


