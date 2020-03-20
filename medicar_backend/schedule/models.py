from doctor.models import Doctor
from django.db import models


class AppointmentTime(models.Model):
    """Appointment Time model"""

    horario = models.TimeField()

    class Meta:
        db_table = 'appointment_times'


class Schedule(models.Model):
    """Schedule model"""

    dia = models.DateField()
    medico = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='doctor_name')
    horarios = models.ManyToManyField(
        AppointmentTime, related_name='appointment_time')

    class Meta:
        db_table = 'schedules'
