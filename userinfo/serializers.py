"""
@author: Michael
@version: 2022-01-04
"""

from django.contrib.auth.models import User, Group
from django.utils import timezone

from .models import UserInfo
from rest_framework import serializers


# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(required=True, max_length=150)
#     password = serializers.CharField(max_length=150)
#     email = serializers.EmailField()
#     register_time = serializers.DateTimeField(default=timezone.now())
#
#     def create(self, validated_data):
#         return UserInfo.object.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.password = validated_data.get('password', instance.password)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'password', 'email', 'register_time']