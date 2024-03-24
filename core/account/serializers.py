from rest_framework import serializers
from .models import Professor


class ProfessorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'