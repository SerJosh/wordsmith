from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_profile(request):
    return render(request, 'profiles.html')