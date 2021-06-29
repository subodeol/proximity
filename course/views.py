from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from .models import Lesson, Subject, Course, CourseSubscription
from .serializers import SubjectSerializer, CourseSerializer, LessonSerializer, CourseSubscriptionSerializer
from rest_framework import viewsets
from school.permissions import IsInstructer, IsStudent
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import filters

import logging
logger = logging.getLogger(__name__)


class SubjectViewSet(viewsets.ModelViewSet):
    # queryset
    queryset = Subject.objects.all()
    # serializer to be used
    serializer_class = SubjectSerializer

    def get_permissions(self):
        logger.info("Checking permissions for Subject view")
        """Set custom permissions for each action."""
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            self.permission_classes = [IsInstructer, ]
        elif self.action in ['list']:
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()


class CourseViewSet(viewsets.ModelViewSet):
    # permissions required
    permission_classes = [IsAuthenticated]      
    # queryset
    queryset = Course.objects.all()
    # serializer to be used
    serializer_class = CourseSerializer

    def get_permissions(self):
        logger.info("Checking permissions for Course view")
        """Set custom permissions for each action."""
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            self.permission_classes = [IsInstructer, ]
        elif self.action in ['list']:
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()

    def retrieve(self, request, pk=None):
        try:
            course_object = Course.objects.get(id=pk)
            course_object.total_views += 1
            course_object.save()
            serializer = self.get_serializer(course_object)
            logger.info("total_views for course "+course_object.name+" is increased by 1.")
            return Response(serializer.data)
        except Exception as e:
            logger.error(e)       
        
class CourseSubscriptionViewSet(viewsets.ModelViewSet):
    # permissions required
    permission_classes = [IsStudent]      
    # queryset
    queryset = CourseSubscription.objects.all()
    # serializer to be used
    serializer_class = CourseSubscriptionSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
        logger.info("Course Subscribed")


class LessonViewSet(viewsets.ModelViewSet):
    # permissions required
    permission_classes = [IsAuthenticated]      
    # queryset
    queryset = Lesson.objects.all()
    # serializer to be used
    serializer_class = LessonSerializer

    def get_permissions(self):
        logger.info("Checking permissions for Lesson view")
        """Set custom permissions for each action."""
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            self.permission_classes = [IsInstructer, ]
        elif self.action in ['list']:
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()


class FilterCourseBySubjectViewSet(viewsets.ViewSetMixin,ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsStudent,]
    
    def get_queryset(self):
        """
        This view should return a list of all the courses for
        the subject name entered by the user.
        """
        subject_name = self.kwargs['subject_name']
        return Course.objects.filter(subjects__name=subject_name)


class ActiveCoursesViewSet(viewsets.ViewSetMixin,ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsStudent,]
    
    def get_queryset(self):
        """
        This view should return a list of all active courses.
        """
        logger.info("Returning all active courses")
        return Course.objects.filter(active=True)


class FilterLessonByCourseViewSet(viewsets.ViewSetMixin,ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsStudent,]
    
    def get_queryset(self):
        """
        This view should return a list of all active lessons filtered by course name.
        """
        course_name = self.kwargs['course_name']
        logger.info("Returning filtered courses")
        return Lesson.objects.filter(courses__name=course_name,active=True)

    