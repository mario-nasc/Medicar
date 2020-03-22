from rest_framework.serializers import ModelSerializer
from doctor.models import Specialty


class SpecialtySerializer(ModelSerializer):
    """Specialty Serializer
    Notes:
        Model is Specialty.
        Take all the fields.
    """
    class Meta:
        model = Specialty
        fields = '__all__'