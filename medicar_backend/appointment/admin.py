from rest_framework.authtoken.models import Token
from django.contrib import admin
from .models import Appointment

admin.site.register(Appointment)
admin.site.unregister(Token)
