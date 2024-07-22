from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('appointment/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    path('patient/booked_appointments/',views.booked_appointments,name='booked'),
    path('doctor/booked_appointments/',views.doctor_booked_appointments, name='doctor_booked_appointments'),
  
]
