from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from college.models import Faculty
from lesson.models import Lesson
from rest_framework.response import Response


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def create(self, validated_data):
        if validated_data['faculty'] != validated_data['field'].department.faculty:
            raise ValidationError("field and faculty don't match")
        return super().create(validated_data)
