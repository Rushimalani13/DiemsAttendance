from django.urls import path
from . import views

urlpatterns = [
    path('takeattendance/', views.Takeattendance, name="attendance-portal"),
    path('markattendance/', views.Markattendance, name="mark-attendance"),

]
