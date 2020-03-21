from django.contrib.auth.models import Group, User
from .models import Doctor, Specialty
from django.contrib import admin

admin.site.site_header = 'Medicar - Gerência'
admin.site.site_title = "Administração do Medicar"
admin.site.index_title = ""


class SpecialtyAdmin(admin.ModelAdmin):
    """Doctor Admin"""
    list_display = ('nome',)


class DoctorAdmin(admin.ModelAdmin):
    """Doctor Admin"""
    list_display = ('nome', 'crm', 'minha_especialidade')
    list_filter = ('nome', 'crm')


admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
