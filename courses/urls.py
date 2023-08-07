from django.urls import path
from .views import *


app_name = 'courses'

urlpatterns = [
    path("", courses,name='courses'),
    path("category/<str:cat>",courses,name ="course_cat"),
    path("teacher/<str:teacher>",courses,name ="course_teacher"),

]