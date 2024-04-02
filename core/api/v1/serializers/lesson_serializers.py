from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from college.models import Faculty
from lesson.models import Lesson, Term
from rest_framework.response import Response
from .college_serializers import FacultySerializer


class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    def create(self, validated_data):
        if validated_data['faculty'] != validated_data['field'].department.faculty:
            raise ValidationError("field and faculty don't match")
        return super().create(validated_data)


class LessonListSerializer(serializers.ModelSerializer):
    faculty = serializers.StringRelatedField(read_only=True)
    field = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class TermViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'
