from django.shortcuts import render
# from django.views.generic.edit import CreateView
from .models import Story
# from .forms import NameForm
from django.http import HttpResponse
# from .forms import StoryForm



# Create your views here.

def all_stories(request):
    story_list = Story.objects.all()
    return render(request, 'stories/index.html', 
    {'story_list': story_list})


def index(request):
    return render(request, 'stories/index.html', {})

def create_story(request):
    form = StoryForm
    return render(request, "create_story.html", {"form" : form})

