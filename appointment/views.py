from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from users.models import User
from .models import *
from .forms import AppointmentForm
# from .google_calendar import create_google_calendar_event
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
            # create_google_calendar_event(appointment)
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