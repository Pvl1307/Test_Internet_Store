from django.contrib.auth.hashers import make_password
from rest_framework import generics

from users.serializers import UserSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    """Регистрация пользователя"""
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Сохранение созданного пользователя с хешированным паролем"""
        hashed_password = make_password(serializer.validated_data['password'])
        serializer.save(password=hashed_password)
