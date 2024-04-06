from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from ..serializers.lesson_serializers import (
    LessonCreateSerializer,
    LessonListSerializer
)
from lesson.models import Lesson, Term
from ..permissions import IsFacultyAssistant

from rest_framework.permissions import IsAdminUser
from rest_framework import status, serializers
from rest_framework.response import Response

from ..serializers.lesson_serializers import TermSerializer

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


class ListCreateTermAPIView(ListCreateAPIView):
    """
    Create New Term By IT Admin
    """
    serializer_class = TermSerializer
    permission_classes = [IsAdminUser]
    queryset = Term.objects.all()

    def perform_create(self, serializer):
        data = serializer.validated_data
        existing_term = Term.objects.filter(name=data['name'])
        if existing_term.exists():
            raise serializers.ValidationError("a term with the same name already exists.")
        serializer.save()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except serializers.ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_409_CONFLICT)

        except Exception as e:
            return super().handle_exception(e)


class RetrieveUpdateDestroyTermAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, delete a term
    """
    serializer_class = TermSerializer
    permission_classes = [IsAdminUser]
    queryset = Term.objects.all()

    def perform_update(self, serializer):
        data = serializer.validated_data
        existing_term = Term.objects.filter(name=data['name'])
        if existing_term.exists():
            raise serializers.ValidationError("a term with the same name already exists.")
        serializer.save()

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except serializers.ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_409_CONFLICT)

        except Exception as e:
            return super().handle_exception(e)

