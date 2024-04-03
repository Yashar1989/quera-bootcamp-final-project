from rest_framework import serializers
from college.models import Faculty


class FacultySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(write_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Faculty
        fields = ['name', 'id']
