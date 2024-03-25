from rest_framework import serializers
from .models import Professor ,Assistant, User


class ProfessorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'



class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'
