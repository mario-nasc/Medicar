from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
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
def mylogin(request):
    user = authenticate(
        request,
        **request.data)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({
            'text':'login efetuado com sucesso',
            'token': str(token),
            'user_id': user.id,
            'username': user.username},
            status=200)
    else:
        return Response(
            {'response': 'usuário não existente'}, status=400)
