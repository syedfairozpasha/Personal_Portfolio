from django.shortcuts import render

# Create your views here.
def HomePageHandler(request):
    return render(request,'jobs/HomePage.html')
