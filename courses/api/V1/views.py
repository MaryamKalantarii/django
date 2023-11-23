
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import CourseApiSerializer
from ...models import Course
from django.shortcuts import get_object_or_404



@api_view()
def course_api_view(request):
    courses = Course.objects.filter(status=True)
    courses_serilize = CourseApiSerializer(courses, many=True)
    return Response(courses_serilize.data)

@api_view()
def course_api_detail_view(request, pk):
    course = get_object_or_404(Course, id=pk)
    course_serilize = CourseApiSerializer(course)
    return Response(course_serilize.data)