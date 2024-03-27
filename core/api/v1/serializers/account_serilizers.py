from rest_framework import serializers
from account.models import Assistant


class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'
