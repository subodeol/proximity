from django.db import models
from user.models import SchoolUser

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=512)

    class Meta:
        db_table = 'subject'

class Course(models.Model):
    name = models.CharField(max_length=512)
    subjects = models.ManyToManyField(Subject)
    total_views = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'course'

class Lesson(models.Model):
    name = models.CharField(max_length=512)
    courses = models.ManyToManyField(Course)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'lesson'

class CourseSubscription(models.Model):
    student = models.ForeignKey(SchoolUser,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=True)

    class Meta:
        db_table = 'course_subscription'

