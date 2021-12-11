from django.shortcuts import render
from .models import Project

# Create your views here.

def about2(request):
    projects = Project.objects.all()
    return render(request, "portfolio/Portafolio.html", {'projects' : projects})
 