from rest_framework.serializers import ModelSerializer, SerializerMethodField
from doctor.api.serializers import DoctorSerializer
from schedule.models import AppointmentTime, Schedule


class AppointmentTimeSerializer(ModelSerializer):
    """AppointmentTime Serializer
    Notes:
        Model is Specialty.
        Take all the fields.
    """

    class Meta:
        model = AppointmentTime
        fields = ('horario',)


class ScheduleSerializer(ModelSerializer):
    """Doctor Serializer
    Notes:
        Model is Doctor.
        Take all the fields.
    """

    horarios = AppointmentTimeSerializer(many=True)
    medico = DoctorSerializer()

    class Meta:
        model = Schedule
        fields = ('dia', 'id', 'horarios', 'medico')
        order_list = ['dia',]