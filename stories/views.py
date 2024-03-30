from django.shortcuts import render, redirect
from .models import Story
from django.http import HttpResponseRedirect
from .forms import StoryForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def error_view500(request, exception=None):
    return render(request, "stories/500.html", {})


def error_view404(request, exception):
    return render(request, "stories/404.html", {})


# Create Story
def create_story(request):
    submitted = False
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save(commit=False)
            story.auther = request.user
            story.save()
            return HttpResponseRedirect('/create_story?submitted=True')
    else:
        form = StoryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'stories/create_story.html',
                  {'form': form, 'submitted': submitted})


# Delete Story
def delete_story(request, story_id):
    story_delete = Story.objects.get(pk=story_id)
    story_delete.delete()
    return redirect('index')


# Edit Story
def edit_story(request, story_id):
    story_edit = Story.objects.get(pk=story_id)
    form = StoryForm(
        request.POST or None, request.FILES or None, instance=story_edit)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'stories/edit_story.html',
                  {'story_edit': story_edit,
                   'form': form})


# Read Story
def view_story(request, story_id):
    story_view = Story.objects.get(pk=story_id)
    print(story_view.auther)
    return render(request, 'stories/view_story.html',
                  {'story_view': story_view})


# See all Stories
def all_stories(request):
    user_id = request.user.id
    story_list = Story.objects.all().order_by('title')
    p = Paginator(Story.objects.all(), 1)
    page = request.GET.get('page')
    stories = p.get_page(page)
    return render(request, 'stories/index.html',
                  {'story_list': story_list,
                   'stories': stories, })


# Go to Stories page
def index(request):
    return render(request, 'stories/index.html', {})


# Go to About page
def about(request):
    return render(request, 'stories/about.html', {})






