from django.shortcuts import render
from .models import Course
from courses.models import Category
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def courses(request ,cat = None,teacher = None):
    category = Category.objects.all()
    if cat:
        course = Course.objects.filter(category__name=cat)
    elif teacher:
        course = Course.objects.filter(teacher__info__username = teacher)
    else:
        course = Course.objects.filter(status=True)

    
    course = Paginator(course,2)
    first_page = 1
    last_page = course.num_pages
    try:
        page_number = request.GET.get('page')
        course = course.get_page(page_number)
    except EmptyPage:
        course = course.get_page(1)
    except PageNotAnInteger:
        course = course.get_page(1)

    context ={
        "courses": course,
        'category':category,
        'first_page': first_page,
        'last_page': last_page,
        
    }
    return render(request,'course/courses.html',context=context)


