from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework import status, serializers
from rest_framework.response import Response
from .models import Assistant, Professor
from lesson.models import Term
from .serializers import (
    AssistantSerializer,
    ProfessorSerializers,
    TermSerializer,
    UpdateDeleteProfessorSerializer
)
from .serializers import ProfessorSerializers, TermSerializer


class RegisterProfessorView(ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializers
    permission_classes = (IsAdminUser, )


class UpdateDeleteProfessorView(RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateDeleteProfessorSerializer
    queryset = Professor.objects.all()
    permission_classes = (IsAdminUser, )


class CreateAssistantAPIView(ListCreateAPIView):
    """
    Make the user as an Assistant
    """
    serializer_class = AssistantSerializer
    permission_classes = [IsAdminUser]
    queryset = Assistant.objects.all()

    def perform_create(self, serializer):
        data = serializer.validated_data
        existing_assistant = Assistant.objects.filter(user_id=data['user'])
        if existing_assistant.exists():
            raise serializers.ValidationError("An assistant with the same attributes already exists.")
        serializer.save()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except serializers.ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_409_CONFLICT)

        except Exception as e:
            return super().handle_exception(e)


class AssistantAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, delete an Assistant
    """
    serializer_class = AssistantSerializer
    permission_classes = [IsAdminUser]
    queryset = Assistant.objects.all()

    def perform_update(self, serializer):
        data = serializer.validated_data
        existing_assistant = Assistant.objects.filter(user_id=data['user'])
        if existing_assistant.exists():
            raise serializers.ValidationError("An assistant with the same attributes already exists.")
        serializer.save()

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except serializers.ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_409_CONFLICT)

        except Exception as e:
            return super().handle_exception(e)


class CreateTermAPIView(ListCreateAPIView):
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


class DetailTermAPIView(RetrieveUpdateDestroyAPIView):
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
