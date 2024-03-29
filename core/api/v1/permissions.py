from rest_framework.permissions import BasePermission, SAFE_METHODS
from lesson.models import Lesson
from account.models import Assistant


class IsFacultyAssistant(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            lesson_faculty = ''
            if 'pk' in view.kwargs:

                lesson_faculty = Lesson.objects.filter(pk=view.kwargs['pk']).values_list('faculty', flat=True).first()

            return bool(request.method in SAFE_METHODS or
                        request.user.is_superuser or
                        Assistant.objects.filter(user=request.user, faculty=request.data.get('faculty')).exists() or
                        Assistant.objects.filter(user=request.user).values_list('faculty',
                                                                                flat=True).first() == lesson_faculty)

        return False

    def has_object_permission(self, request, view, obj):
        lesson_faculty = ''
        if 'pk' in view.kwargs:
            lesson_faculty = Lesson.objects.filter(pk=view.kwargs['pk']).values_list('faculty', flat=True).first()

        return bool(request.method in SAFE_METHODS or
                    request.user.is_superuser or
                    Assistant.objects.filter(user=request.user).values_list('faculty',
                                                                            flat=True).first() == lesson_faculty)
