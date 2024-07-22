from django.urls import path
from . import views

urlpatterns = [
    path('demo/',views.demo,name='demo'),
    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('appointment/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    path('booked_appointments/',views.booked_appointments,name='booked')
]
