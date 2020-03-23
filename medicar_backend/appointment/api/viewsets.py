from .serializers import AppointmentSerializer, CreateAppointmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from schedule.models import Schedule, AppointmentTime
from doctor.api.serializers import DoctorSerializer
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from django.forms.models import model_to_dict
from rest_framework.response import Response
from django.contrib.auth.models import User
from appointment.models import Appointment
from datetime import datetime

class AppointmentViewSet(ModelViewSet):
    """Specialty ViewSet

    Notes:
        inherits from ReadOnlyModelViewSet because the API should
        only be consumed with GET, not allowing the user to create,
        alter, or delete any database data.
    """
    queryset = Appointment.objects.order_by(
            'dia', 'horario').exclude(dia__lt=datetime.now()).exclude(
                horario__lt=datetime.now())

    serializer_class = AppointmentSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['client']
    create_serializer_class = CreateAppointmentSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return self.create_serializer_class
        return super().get_serializer_class()

    def get_user_id(self, request):
        if not request.GET._mutable:
            request.GET._mutable = True
        token = request.META.get('HTTP_AUTHORIZATION').split('Token ')[-1]
        mytoken = Token.objects.get(key=token)
        return mytoken.user_id

    def list(self, request, *args, **kwargs):
        user_id = self.get_user_id(request)
        request.GET['client'] = user_id
        return super(AppointmentViewSet, self).list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        hour_id = AppointmentTime.objects.get(horario=request.data['horario']).id
        schedule = Schedule.objects.get(id=request.data['agenda_id'])
        schedule.horarios.remove(hour_id)
        user_id = self.get_user_id(request)
        client = User.objects.get(id=user_id)
        doctor_esp = schedule.medico.especialidade
        doctor = model_to_dict(schedule.medico)
        doctor['especialidade'] = model_to_dict(doctor_esp)
        appointment = {
            'client': client,
            'dia': schedule.dia,
            'horario': request.data['horario'],
            'data_agendamento': datetime.now(),
            'medico': schedule.medico
        }
        new_appointment = Appointment(**appointment)
        new_appointment.save()
        del appointment['client']
        appointment['id'] = new_appointment.id
        appointment['medico'] = doctor
        return Response(appointment)

    def destroy(self, request, *args, **kwargs):
        appointment = Appointment.objects.get(id=kwargs['pk'])
        user_id = self.get_user_id(request)

        if user_id != appointment.client.id or appointment.dia < datetime.now():
            return Response({'text': "exclusão não permitida"}, status=403)

        appointment_time = AppointmentTime.objects.get(
            horario=appointment.horario)
        schedule = Schedule.objects.get(medico=appointment.medico, dia=appointment.dia)
        schedule.horarios.add(appointment_time)
        return super(AppointmentViewSet, self).destroy(request, *args, **kwargs)
