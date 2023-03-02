from rest_framework import generics

from apps.security.models import User
from apps.security.serializers.user_serializer import UserSerializer


class UserCreateApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"
