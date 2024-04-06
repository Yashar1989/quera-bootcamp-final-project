from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
)

from ..serializers.lesson_serializers import (
    LessonCreateSerializer,
    LessonListSerializer,
    TermShowSerializer
)
from lesson.models import Lesson, Term
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


class TermListRetrieveAPIView(ListAPIView, RetrieveAPIView):
    serializer_class = TermShowSerializer
    queryset = Term.objects.all()
