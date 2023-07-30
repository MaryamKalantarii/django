from django.shortcuts import render
from .models import Services
from courses.models import Course,Trainer


# Create your views here.



def home (request):
    services = Services.objects.filter(status=True)
    last_three_course = Course.objects.filter(status=True)[:3]
    last_three_trainer = Trainer.objects.filter(status=True)[:3]
    context = {
        'service':services,
        'course':last_three_course,
        'trainer':last_three_trainer,
    }
    return render(request,"root/index.html" , context=context)

def about (request):
    return render(request,"root/about.html")

def contact(request):
    return render(request,"root/contact.html")