from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClientSerializer

@api_view(['POST'])
def signup(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(**request.data)
        user.save()
        return Response(
            {'response': "usuário cadastrado com sucesso"}, status=200)
    else:
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def login(request):
    pass
