from rest_framework import serializers
from account.models import Assistant, User, CustomUserManager
from rest_framework.response import Response
from rest_framework import status

from .college_serializers import FacultySerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender', 'birth_date', 'national_code', 'password']


class AssistantSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    user = UserSerializer()
    faculty = FacultySerializer()

    class Meta:
        model = Assistant
        fields = ['id', 'user', 'faculty']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user_manager = CustomUserManager()
        assistant = user_manager.create_assistant(password=password, **user_data, **validated_data)
        return assistant
