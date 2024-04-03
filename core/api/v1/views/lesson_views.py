from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from ..serializers.lesson_serializers import (
    LessonCreateSerializer,
    LessonListSerializer
)
from lesson.models import Lesson
from ..permissions import IsFacultyAssistant


class LessonCreateAPIView(ListCreateAPIView):
    permission_classes = [IsFacultyAssistant]
    serializer_class = LessonCreateSerializer
    queryset = Lesson.objects.all()

    # search_fields = ['name', 'faculty__name']
    # filter_backends = [filters.SearchFilter]
    def list(self, request, *args, **kwargs):
        self.serializer_class = LessonListSerializer
        return super().list(self, request, *args, **kwargs)


class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsFacultyAssistant]
    serializer_class = LessonListSerializer
    queryset = Lesson.objects.all()

