from django.urls import path
from . import views

urlpatterns = [
    path("subject_attendance/", views.subject_Attendance, name='subjec_wise_record'),
    path("subwise_attendance/", views.subject_Attendance_table, name='attendance_record_table'),
  
]
