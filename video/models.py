from django.db import models
from course.models import Lesson
from user.models import SchoolUser

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'tag'

class Video(models.Model):
    details = models.CharField(max_length=2048)
    title = models.CharField(max_length=256)
    lessons = models.ManyToManyField(Lesson)
    tags = models.ManyToManyField(Tag)
    link = models.CharField(max_length=2048)
    total_views = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'video'
