from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import  ScheduleSerializer
from schedule.models import Schedule
from rest_framework import filters
from datetime import datetime, date


class ScheduleViewSet(ReadOnlyModelViewSet):
    """Doctor ViewSet

    Notes:
        inherits from ReadOnlyModelViewSet because the API should
        only be consumed with GET, not allowing the user to create,
        alter, or delete any database data.
    """
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filter_fields = ['medico']

    def get_queryset(self):
        now = datetime.now()
        queryset =  Schedule.objects.order_by(
            'dia').exclude(dia__lt=now).exclude(
                horarios__horario__lt=now, dia=date.today())
        start_data = self.request.query_params.get('data_inicio', None)
        end_data = self.request.query_params.get('data_final', None)
        if start_data and end_data:
            queryset = queryset.filter(dia__range=(start_data, end_data))
        return queryset
