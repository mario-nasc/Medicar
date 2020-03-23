from schedule.models import Schedule, AppointmentTime
from django.contrib.auth.models import User
from doctor.models import Doctor
from django.db import models


class Appointment(models.Model):
    """Appointment Model"""
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    dia = models.DateField()
    data_agendamento = models.DateField()
    medico = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    horario = models.TimeField()

    def __str__(self):
        return f'Médico: {self.medico.nome}, Dia: {self.dia}, horário: {self.horario}'

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        db_table = 'appointments'
    
