from .models import AppointmentTime, Schedule
from django.contrib import admin


class appointmentTimeAdmin(admin.ModelAdmin):
    """Appointment Time Admin"""
    list_display = ('horario',)
    list_filter = ('horario',)


class scheduleAdmin(admin.ModelAdmin):
    """Appointment Time Admin"""
    list_display = ('dia', 'this_medico')
    list_filter = ('dia', 'medico')


admin.site.register(AppointmentTime, appointmentTimeAdmin)
admin.site.register(Schedule, scheduleAdmin)
