from django.shortcuts import render
from .models import Services
from courses.models import Course,Trainer
from courses.models import Category
from django.contrib.auth.models import User


# Create your views here.



def home (request):
    service_count = Services.objects.filter(status = True).count()
    course_count = Services.objects.filter(status = True).count()
    trainer_count = Services.objects.filter(status = True).count()
    user_count = Services.objects.filter(status = True).count()
    category = Category.objects.all()
    services = Services.objects.filter(status=True)
    last_three_course = Course.objects.filter(status=True)[:3]
    last_three_trainer = Trainer.objects.filter(status=True)[:3]
    context = {
        'service':services,
        'course':last_three_course,
        'trainer':last_three_trainer,
        'category':category,
        'sc':service_count,
        'cc':course_count,
        'tc':trainer_count,
        'uc':user_count,
    }
    return render(request,"root/index.html" , context=context)



def about (request):
    category = Category.objects.all()
    context = {
        'category':category,
    }
    return render(request,"root/about.html", context=context)


def contact(request):
    category = Category.objects.all()
    context = {
        'category':category,
    }
    return render(request,"root/contact.html", context=context)



def trainer(request):
    category = Category.objects.all()
    context = {
        'category':category,
    }
    return render(request,"root/trainers.html", context=context)



def course_detail(request,id):
    try:
        course = Course.objects.get(id=id)
        id_list = []
        courses = Course.objects.filter(status=True)
        for cr in courses:
            id_list.append(cr.id)

        id_list.reverse()
        
        if id_list[0] == id :
            next_course = Course.objects.get(id = id_list[1])
            previous_course = None

        elif id_list[-1] == id :
            next_course = None
            previous_course = Course.objects.get(id = id_list[-2])

        else:
            next_course = Course.objects.get(id=id_list[id_list.index(id)+1])
            previous_course = Course.objects.get(id=id_list[id_list.index(id)-1])




        course.counted_views +=1
        course.save()
    
        context ={"course": course,
                'next_course': next_course,
                'previous_course': previous_course,
        }
        return render(request,'course/course-details.html',context=context)
    except:
        return render(request,'course/404.html')
