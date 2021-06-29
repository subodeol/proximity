from django.contrib import admin

# Register your models here.

from .models import Course, Lesson, Subject, CourseSubscription

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(CourseSubscription)


