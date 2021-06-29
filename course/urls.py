from django.urls import include, path
from django.contrib.auth.decorators import login_required


from . import views

urlpatterns = [
    path('example/', login_required(views.ExampleView.as_view()), name='example_view'),
    path('courses/', views.CourseViewSet.as_view(), name='course_view'),

    
]