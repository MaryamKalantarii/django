from django.shortcuts import render
from .models import Course
from courses.models import Category


def courses(request ,cat = None,teacher = None):
    category = Category.objects.all()
    if cat:
        course = Course.objects.filter(category__name=cat)
    elif teacher:
        course = Course.objects.filter(teacher__info__username = teacher)
    else:
        course = Course.objects.filter(status=True)
    
    context ={
        "courses": course,
        'category':category,
    }
    return render(request,'course/courses.html',context=context)


