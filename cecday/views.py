import imp
from django.shortcuts import render

def home(request):
    return render(request,'cecday/home.html')

def all_event(request):
    return render(request,'cecday/events.html')
def tech_event(request):
    return render(request,'cecday/techevents.html')
def nont_tech_event(request):
    return render(request,'cecday/nontechevents.html')
def about(request):
    return render(request,"cecday/about.html")


