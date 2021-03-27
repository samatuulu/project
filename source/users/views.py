import jwt
from django.conf import settings
from django.contrib import auth
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from users.serializers import RegistrationSerializer, UserSerializer


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "New user registered."
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)


class LoginView(GenericAPIView):

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY)
            serializer = UserSerializer(user)
            data = {
                "user": serializer.data,
                "token": auth_token
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
