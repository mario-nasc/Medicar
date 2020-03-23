from schedule.api.serializers import ScheduleSerializer
from appointment.models import Appointment
from rest_framework import serializers

class AppointmentSerializer(serializers.ModelSerializer):
    """Appointment Serializer
    Notes:
        Model is Appointment.
        Take all the fields.
    """
    agenda = ScheduleSerializer()
    class Meta:
        model = Appointment
        fields = '__all__'

class CreateAppointmentSerializer(serializers.ModelSerializer):
    """Appointment Serializer
    Notes:
        Model is Appointment.
        Take all the fields.
    """
    agenda_id = serializers.CharField()
    horario = serializers.TimeField()
    class Meta:
        model = Appointment
        fields = ('horario', 'agenda_id')