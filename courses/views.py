from django.shortcuts import render
from .models import Course

# Create your views here.
def courses(request):
    course = Course.objects.filter(status=True)
    context ={"courses": course
    }
    return render(request,'course/courses.html',context=context)

