from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework import status, serializers
from rest_framework.response import Response

from .models import Assistant
from .serializers import AssistantSerializer


# Create your views here.


class CreateAssistantAPIView(CreateAPIView):
    serializer_class = AssistantSerializer
    permission_classes = [IsAdminUser]

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