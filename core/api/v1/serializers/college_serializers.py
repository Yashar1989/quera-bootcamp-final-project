from rest_framework import serializers

from college.models import College


class CollegeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(write_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = College
        fields = ['name', 'id']
