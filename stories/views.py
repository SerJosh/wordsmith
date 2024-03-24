from django.shortcuts import render, redirect
# from django.views.generic.edit import CreateView
from .models import Story
# from .forms import NameForm
from django.http import HttpResponseRedirect
from .forms import StoryForm
from django.core.paginator import Paginator



# Create your views here.

# Delete Story
def delete_story(request, story_id):
    story_delete = Story.objects.get(pk=story_id)
    story_delete.delete()
    return redirect('index')



def edit_story(request, story_id):
    story_edit = Story.objects.get(pk=story_id)
    form = StoryForm(request.POST or None,request.FILES or None, instance=story_edit)
    if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'stories/edit_story.html', 
    {'story_edit': story_edit,
    'form': form})


def view_story(request, story_id):
    story_view = Story.objects.get(pk=story_id)
    return render(request, 'stories/view_story.html', 
    {'story_view': story_view})

def all_stories(request):
    user_id = request.user.id
    story_list = Story.objects.all().order_by('title')
    p = Paginator(Story.objects.all(), 1)
    page = request.GET.get('page')
    stories = p.get_page(page)
    return render(request, 'stories/index.html', 
    {'story_list': story_list,
    'stories': stories,})


# def all_stories(request):
#     user_id = request.user.id
#     story_list = Story.objects.all().order_by('Title').filter(user_id.stories)
#     p = Paginator(story_list, 1)
#     page = request.GET.get('page')
#     stories = p.get_page(page)
#     # nums = "a" * venues.paginator.num_pages
#     return render(request, 'stories/index.html', 
#     {'story_list': story_list,
#     'stories': stories,})
# def all_stories(request):
#     user_id = request.user.id
#     story_list = Story.objects.filter(Auther_id=user_id).order_by('Title')
#     p = Paginator(Story.objects.all(), 1)
#     page = request.GET.get('page')
#     stories = p.get_page(page)
#     return render(request, 'stories/index.html', 
#     {'story_list': story_list,
#     'stories': stories,
#     'user_id':user_id,})


def index(request):
    return render(request, 'stories/index.html', {})


def create_story(request):
    submitted = False
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create_story?submitted=True')
    else:
        form = StoryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'stories/create_story.html', 
    {'form': form, 'submitted': submitted})





