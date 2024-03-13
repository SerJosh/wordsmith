from django.shortcuts import render
# from django.views.generic.edit import CreateView
from .models import Story
# from .forms import NameForm
from django.http import HttpResponseRedirect
from .forms import StoryForm



# Create your views here.

def view_story(request, story_id):
    story_view = Story.objects.get(pk=story_id)
    return render(request, 'stories/view_story.html', 
    {'story_view': story_view})

def all_stories(request):
    story_list = Story.objects.all()
    return render(request, 'stories/index.html', 
    {'story_list': story_list})


def index(request):
    return render(request, 'stories/index.html', {})


def create_story(request):
    submitted = False
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create_story?submitted=True')
    else:
        form = StoryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'stories/create_story.html', 
    {'form': form, 'submitted': submitted})





