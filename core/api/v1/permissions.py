from rest_framework.permissions import BasePermission
from lesson.models import Lesson
from account.models import Assistant


class IsFacultyAssistant(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(request.user.is_superuser or
                        Assistant.objects.filter(user=request.user, faculty=request.data.get('faculty')).exists())

        return False

    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_superuser or
                    Assistant.objects.filter(user=request.user).faculty == obj.faculty
                    )
