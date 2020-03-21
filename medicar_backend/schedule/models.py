from doctor.models import Doctor
from django.db import models


class AppointmentTime(models.Model):
    """Appointment Time model"""

    horario = models.TimeField()

    def __str__(self):
        return str(self.horario)

    class Meta:
        verbose_name = 'Horário'
        verbose_name_plural = 'Horários'
        db_table = 'appointment_times'


class Schedule(models.Model):
    """Schedule model"""

    dia = models.DateField()
    medico = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='doctor_name')
    horarios = models.ManyToManyField(
        AppointmentTime, related_name='appointment_time')

    def this_medico(self):
        return self.medico.nome

    def __str__(self):
        return f'{self.dia} - {self.this_medico()}'

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'
        db_table = 'schedules'
