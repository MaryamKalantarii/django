from django.urls import path
from .views import *


app_name = 'courses'

urlpatterns = [
    path("", courses,name='courses'),
]