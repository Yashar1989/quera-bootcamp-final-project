from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from .resource import ProfessorResource, StudentResource
from .models import User, Student, Professor, Assistant


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['national_code', 'first_name', 'last_name', 'user_code', 'phone_number', 'gender', 'email']
    list_filter = ['gender']
    ordering = ['national_code']


class StudentAdmin(ImportExportModelAdmin):
    list_display = ['user', 'field', 'supervisor', 'seniority', 'get_user_code']
    list_filter = ['seniority', 'supervisor', 'field']
    resource_class = StudentResource


class ProfessorAdmin(ImportExportModelAdmin):
    list_display = ['user', 'faculty', 'proficiency', 'order', 'get_user_code']
    list_filter = ['faculty', 'order', 'proficiency']
    resource_class = ProfessorResource


class AssistantAdmin(admin.ModelAdmin):
    list_display = ['user', 'faculty']
    list_filter = ['faculty']


admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Assistant, AssistantAdmin)
