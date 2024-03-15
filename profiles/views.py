from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import WordsmithUser
from .forms import ProfileForm
# From Git
# from django.contrib.auth import logout
# from django.contrib.auth.models import User
# from .forms import DeleteUser

# def delete_user_view(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = DeleteUser(request.POST)

#             if form.is_valid():
#                 if request.POST["delete_checkbox"]:
#                     rem = User.objects.get(username=request.user)
#                     if rem is not None:
#                         rem.delete()
#                         logout(request)
#                         messages.info(request, "Your account has been deleted.")
#                         return redirect(reverse("app:url_name"))
#                     else:
#                         messages.info(request, "There was an error.")
#         else:
#             form = DeleteUser()
#         context = {'form': form}
#         return render(request, 'file.html', context)
#         if request.user.is_anonymous:
#             return HttpResponse(render(request, "401.html"), status=401)

# Create your views here.

def edit_profile(request, profile_id):
    profile_edit = WordsmithUser.objects.get(pk=profile_id)
    form = ProfileForm(request.POST or None, instance=profile_edit)
    if form.is_valid():
            form.save()
            return redirect('view-profile')
    return render(request, 'profiles/edit_profile.html', 
    {'form': form,
    'profile_edit': profile_edit})



def user_profile(request):
    profile = WordsmithUser.objects.all()
    return render(request, 'profiles/profiles.html',
    {'profiles': profile})


def my_profile(request):
    return render(request, 'profiles.html')

def delete_profile(request):
    return render(request, 'delete_profile.html')
