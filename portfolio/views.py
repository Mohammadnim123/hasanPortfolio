from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Hello

# Create your views here.

def index(req):
    
    return render(req,'portfolio/index.html',{
        "hello": Hello.objects.get().post
    })