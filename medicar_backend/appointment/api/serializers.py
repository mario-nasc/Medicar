from doctor.api.serializers import DoctorSerializer
from appointment.models import Appointment
from rest_framework import serializers

class AppointmentSerializer(serializers.ModelSerializer):
    """Appointment Serializer
    Notes:
        Model is Appointment.
        Take all the fields.
    """
    medico = DoctorSerializer()
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