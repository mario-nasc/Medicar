from .serializers import SpecialtySerializer, DoctorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from doctor.models import Specialty, Doctor
from rest_framework import filters


class SpecialtyViewSet(ReadOnlyModelViewSet):
    """Specialty ViewSet
    
    Notes:
        inherits from ReadOnlyModelViewSet because the API should
        only be consumed with GET, not allowing the user to create,
        alter, or delete any database data.
    """
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['^nome']


class DoctorViewSet(ReadOnlyModelViewSet):
    """Doctor ViewSet
    
    Notes:
        inherits from ReadOnlyModelViewSet because the API should
        only be consumed with GET, not allowing the user to create,
        alter, or delete any database data.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['^nome',]
    filter_fields = ['especialidade']
