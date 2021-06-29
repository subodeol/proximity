
from .models import Subject, Course, Lesson, CourseSubscription
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        exclude = ()


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ()

class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        exclude = ()
        fields = '__all__'
        read_only_fields = ('student',)

    

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ()
