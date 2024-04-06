from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, serializers
from django.contrib.auth import get_user_model
from django.conf import settings
import redis

from ..serializers.account_serilizers import AssistantSerializer
from ..tasks import send_password_reset_email
from account.models import Assistant

User = get_user_model()


class CreateAssistantAPIView(ListCreateAPIView):
    """
    Make the user as an Assistant
    """
    serializer_class = AssistantSerializer
    permission_classes = [IsAdminUser]
    queryset = Assistant.objects.all()


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

    def delete(self, request, *args, **kwargs):
        user_id = Assistant.objects.get(pk=kwargs['pk']).user_id
        super().delete(request, *args, **kwargs)
        user = User.objects.filter(id=user_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordRequest(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email:
            user = User.objects.get(email=email)
            if user:
                send_password_reset_email.delay(email)
                return Response("Password reset email has been sent.", status=status.HTTP_200_OK)
            else:
                return Response("User with this email not found.", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Email is required.", status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordAction(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        new_password = request.data.get('new_password')
        if token and new_password:
            r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_PASSWORD, db=0)
            email = r.get(token)
            if email:
                user = User.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                return Response("Password has been updated successfully.", status=status.HTTP_200_OK)
            else:
                return Response("Invalid or expired token.", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Token and new password are required.", status=status.HTTP_400_BAD_REQUEST)
