from djoser.serializer import UserCreateSerializer, UserSerializer
from rest_framework import serializer
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = {'id','email','username','password','first_name','last_name','phone'}