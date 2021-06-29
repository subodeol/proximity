from django.test import TestCase
from user.models import SchoolUser
from django.urls import reverse
from course.views import CourseViewSet
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework.test import APIClient
from rest_framework import status
from course.models import *
from video.models import *



# Create your tests here.

class InstructorTestCase(TestCase):
    def setUp(self) -> None:
        self.user = SchoolUser.objects.create(username="mark",password="Apple@159",is_instructor=True)
        return super().setUp()

    def test_instructor_post_action(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        
        subject_name = 'Physics'
        subject_response = client.post('/api/v1/subject/', {'name': 'Physics'}, format='json')
        self.assertEqual(subject_response.status_code, status.HTTP_201_CREATED)
        subject_data = subject_response.json()
        self.assertEqual(Subject.objects.get(id=subject_data["id"]).name,subject_name)

        course_name = 'M.Sc'
        course_response = client.post('/api/v1/course/', {'name': course_name,"subjects":[subject_data["id"]]}, format='json')
        self.assertEqual(course_response.status_code, status.HTTP_201_CREATED)
        course_data = course_response.json()
        self.assertEqual(Course.objects.get(id=course_data["id"]).name,course_name)
        
        # create lesson
        lesson_name = 'Introduction'
        lesson_response = client.post('/api/v1/lesson/', {'name': lesson_name,"courses":[course_data["id"]]}, format='json')
        self.assertEqual(lesson_response.status_code, status.HTTP_201_CREATED)
        lesson_data = lesson_response.json()
        self.assertEqual(Lesson.objects.get(id=lesson_data["id"]).name,lesson_name)

    def test_instructor_negative(self):
        self.user.is_instructor = False
        self.user.save()

        client = APIClient()
        client.force_authenticate(user=self.user)
        
        subject_name = 'Physics'
        subject_response = client.post('/api/v1/subject/', {'name': 'Physics'}, format='json')
        self.assertNotEqual(subject_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(subject_response.status_code, 403)


class StudentTestCase(TestCase):
    def setUp(self) -> None:
        self.user = SchoolUser.objects.create(username="steve",password="Apple@159",is_instructor=False)
        self.subject = Subject.objects.create(name="Chemistry")
        self.course = Course(name="B.Sc")
        self.course.save()
        self.course.subjects.add(self.subject)
        return super().setUp()

    def test_student_subscription(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        subscription_response = client.post('/api/v1/course_subscription/', {'course': self.course.id}, format='json')
        self.assertEqual(subscription_response.status_code, status.HTTP_201_CREATED)
        subscription_data = subscription_response.json()
        self.assertEqual(CourseSubscription.objects.get(id=subscription_data["id"]).student.username,"steve")

        
    def test_student_subscription_negative(self):
        self.user.is_instructor = True
        self.user.save()
        client = APIClient()
        client.force_authenticate(user=self.user)

        subscription_response = client.post('/api/v1/course_subscription/', {'course': self.course.id}, format='json')
        self.assertNotEqual(subscription_response.status_code, status.HTTP_201_CREATED)

