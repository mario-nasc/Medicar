from rest_framework.serializers import ModelSerializer
from doctor.models import Specialty, Doctor


class SpecialtySerializer(ModelSerializer):
    """Specialty Serializer
    Notes:
        Model is Specialty.
        Take all the fields.
    """
    class Meta:
        model = Specialty
        fields = '__all__'


class DoctorSerializer(ModelSerializer):
    """Doctor Serializer
    Notes:
        Model is Doctor.
        Take all the fields.
    """
    class Meta:
        model = Doctor
        fields = '__all__'