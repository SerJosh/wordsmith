from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_profile(request):
    return render(request, 'profiles.html')

def delete_profile(request):
    return render(request, 'delete_profile.html')
