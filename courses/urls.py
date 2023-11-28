from django.urls import path , include
from .views import *


app_name = 'courses'

urlpatterns = [
    path("", CourseListView.as_view(),name='courses'),
    path("category/<str:cat>",CourseListView.as_view(),name="course_cat"),
    path("teacher/<str:teacher>",CourseListView.as_view(),name="course_teacher"),
    path("search/",CourseListView.as_view(),name="course_search"),
    path("course-detail/<int:pk>",CourseDetailView.as_view(),name="course_detail"),
    path("payment",PaymentView.as_view(),name="cart"),
    path("api-test/",api_test,name="cart"),
    # path("", courses,name='courses'),
    # path("category/<str:cat>",courses,name ="course_cat"),
    # path("teacher/<str:teacher>",courses,name ="course_teacher"),
    # path("search/",courses,name ="course_search"),
    # path("course-detail/<int:id>",course_detail,name="course_detail"),
    path("<int:id>",delete_comment,name="delete"),
    path("edit/comment/<int:id>",edit,name="edit"),
    path("comment/reply/<int:id>",reply,name="reply"),
    path("api/V1/",include('courses.api.V1.urls')),
]