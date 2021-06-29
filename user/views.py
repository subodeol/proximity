from django.shortcuts import render
from course.models import Course
from video.models import Video
from rest_framework import viewsets
from .serializer import AnalyticsSerializers
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from course.serializers import CourseSerializer
from video.serializers import VideoSerializer

# Create your views here.

class AnalyticsViewSet(viewsets.ViewSet):
    serializer_class_course = CourseSerializer
    serializer_class_video = VideoSerializer

    def get_queryset_Course(self):
        return Course.objects.all().order_by("total_views")

    def get_queryset_Video(self):
        return Video.objects.all().order_by("total_views")

    def list(self, request, *args, **kwargs):
        courses = self.serializer_class_course(self.get_queryset_Course(), many=True)
        videos = self.serializer_class_video(self.get_queryset_Video(), many=True)
        return Response({
            "Most Viewed Courses": courses.data,
            "Most Viewed Videos": videos.data
        })
