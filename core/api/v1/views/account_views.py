from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework import serializers, status
from rest_framework.response import Response

from ..serializers.account_serilizers import AssistantSerializer
from account.models import Assistant


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
