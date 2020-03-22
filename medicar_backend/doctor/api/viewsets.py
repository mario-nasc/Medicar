from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import SpecialtySerializer
from doctor.models import Specialty
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