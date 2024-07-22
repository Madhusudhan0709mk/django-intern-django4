import os
print(os.getcwd())

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from users.models import User
from .models import *
from .forms import AppointmentForm


from google.oauth2 import service_account
from django.conf import settings
from googleapiclient.discovery import build




def demo(request):
    return render(request,'doctors/demo.html')

@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(User, id=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('appointment_detail', appointment_id=appointment.id)
    else:
        form = AppointmentForm(initial={'doctor': doctor})
    return render(request, 'appointment/book_appointment.html', {'form': form, 'doctor': doctor})

@login_required
def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'appointment/appointment_detail.html', {'appointment': appointment})

@login_required
def booked_appointments(request):
    patient = request.user
    booked = patient.patient_appointments.all()
    return render(request,'appointment/booked.html',{'booked':booked})

@login_required
def doctor_booked_appointments(request):
    doctor = request.user
    booked = doctor.doctor_appointments.all()  # Adjust the related name accordingly
    return render(request, 'appointment/doctor_booked.html', {'booked': booked})


