from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import get_user_model,authenticate
from rest_framework.views import Response
from rest_framework.authtoken.models import Token


# Create your views here.
User = get_user_model()
class UserRegistration(CreateAPIView):
    serializer_class = UserRegistrationSerializer

class Login(APIView):
    def post(self, request, *args, **kwargs):

        username=request.data.get('username')
        password=request.data.get('password')
        
        if username is None:
            return Response(
                {
                    'username':'This field is required'
                })
        
        if password is None:
            return Response(
                {
                    'password':'This field is required'
                })

        user=authenticate(
            username=username,
            password=password,
        )
        if user:
            token,_ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "username":user.username,
                    "token":token.key
                    },
            )


        return Response(
            {
                "detail": "User credentials do not match"
            }
        )
    