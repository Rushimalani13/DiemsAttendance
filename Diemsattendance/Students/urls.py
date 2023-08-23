from django.urls import path
from . import views

urlpatterns = [
    path("student/", views.show_students, name='show_students'),
]
