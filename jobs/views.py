from django.shortcuts import render

from .models import Job

# Create your views here.
def HomePageHandler(request):

    jobs = Job.objects
    return render(request,'jobs/HomePage.html',{"jobs":jobs})
