from django.shortcuts import render , redirect
from django.http.response import HttpResponse 
from .models import FirstSection , About_Basic_Information , Skills , Projects , Experience , Education
from django.urls import reverse
from mailer import Mailer

# Create your views here.

def index(req):

    if req.GET.get("name"):
        name = req.GET.get("name")
        subject = req.GET.get("Subject")
        replyto = req.GET.get("_replyto")
        message = req.GET.get("message")

        mail = Mailer(email='mohammadtest0000@gmail.com',password='Kaled.123')

        mail.send(receiver='Hnimrawi@gmail.com',  # Email From Any service Provider
                subject='Email From Your Portfolio',
                message=
                f"""
                Sender Name: {name},
                Subject: {subject},
                Sender Email: {replyto},

                Message content:
                {message}
  
                """
                )
        
        return redirect(reverse('index'))

    else:

    
        return render(req,'portfolio/index.html',{
            "first_section": FirstSection.objects.get(),
            "about": About_Basic_Information.objects.get(),
            "skills": Skills.objects.all(),
            "projects": Projects.objects.all(),
            "experience": Experience.objects.all(),
            "education": Education.objects.all(),
        
         })

def send_email(req):
    # body_unicode = req.body.decode('utf-8')
    # body = json.loads(body_unicode)
    # content = body['content']
    body = req.GET
    print('jjjjj',body)
    return redirect(reverse('index'))
