from rest_framework import routers
from course.views import *
from video.views import VideoViewSet, TagViewSet
from user.views import AnalyticsViewSet

router = routers.DefaultRouter()
router.register(r'subject', SubjectViewSet)
router.register(r'course', CourseViewSet, basename='Courses')
router.register(r'course_subscription', CourseSubscriptionViewSet)
router.register(r'lesson', LessonViewSet)
router.register(r'video', VideoViewSet)
router.register(r'tag', TagViewSet)
router.register(r'analytics', AnalyticsViewSet, basename='Analytics')
router.register('^filter_course_by_subject/(?P<subject_name>.+)', FilterCourseBySubjectViewSet, basename='Filter Course By Subject')
router.register('^active_courses', ActiveCoursesViewSet, basename='Active Courses')
router.register('^filter_lesson_by_course/(?P<course_name>.+)', FilterLessonByCourseViewSet, basename='Filter Lesson By Course')





