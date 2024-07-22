from django.db import models
from datetime import datetime ,timedelta
from users.models import *
from blog.models import *

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def save(self,*args,**kwargs):
        self.end_time = (datetime.combine(self.date,self.start_time)+timedelta(minutes=45)).time()
        super().save(*args,**kwargs)
        
    def __str__(self):
        return f'{self.patient.username} with {self.doctor.username} on {self.date} at {self.start_time}'