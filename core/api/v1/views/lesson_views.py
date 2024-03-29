from rest_framework.generics import ListAPIView, CreateAPIView
from ..serializers.lesson_serializers import LessonSerializer
from lesson.models import Lesson
from ..permissions import IsFacultyAssistant

class LessonListAPIView(CreateAPIView):
    permission_classes = [IsFacultyAssistant]
    serializer_class = LessonSerializer
