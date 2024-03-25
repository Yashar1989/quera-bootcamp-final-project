from rest_framework import serializers

from .models import Assistant, User


class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'
