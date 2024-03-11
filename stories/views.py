from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Story
# from .forms import NameForm
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create_story(request):
    return render(request, 'create_story.html')

class CreateNewStory(CreateView):
    model = Story
    template_name = 'create_story.html'
    fields = ['Title', 'Synopsis', 'Content']
