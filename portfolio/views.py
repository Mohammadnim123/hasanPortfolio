from django.shortcuts import render
from django.http.response import HttpResponse
from .models import FirstSection , About_Basic_Information , Skills , Projects , Experience , Education


# Create your views here.

def index(req):

    
        
    
    return render(req,'portfolio/index.html',{
        "first_section": FirstSection.objects.get(),
        "about": About_Basic_Information.objects.get(),
        "skills": Skills.objects.all(),
        "projects": Projects.objects.all(),
        "experience": Experience.objects.all(),
        "education": Education.objects.all(),
        
    })