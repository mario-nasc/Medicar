from django.contrib import admin
from .views import signup, mylogin
from django.urls import path

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', mylogin, name='login')
]
