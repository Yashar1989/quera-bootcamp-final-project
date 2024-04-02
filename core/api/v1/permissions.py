from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from lesson.models import Lesson
from account.models import Assistant
import re


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


class IsStudentOrProfessor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if re.match("^[p]\d{10}$", request.user.user_code) or re.match("^[s]\d{10}$", request.user.user_code):
                return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if re.match("^[p]\d{10}$", request.user.user_code) or re.match("^[s]\d{10}$", request.user.user_code):
                return True

