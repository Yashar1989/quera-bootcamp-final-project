from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth import get_user_model
from . models import EmploymentEducationRequest, EmergencySemesterDeleteRequest, TermModificationRequest, ReviewRequest, EmergencyRemovalRequest
from account.models import Student, Professor


User = get_user_model()

# Define an inline admin descriptor for Student model
class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'students'

# Define an inline admin descriptor for Professor model
class ProfessorInline(admin.StackedInline):
    model = Professor
    can_delete = False
    verbose_name_plural = 'professors'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline, ProfessorInline, )
    list_display = ['first_name', 'last_name', 'national_code',]
    ordering = ['national_code',]
    list_filter = ['national_code',]
# Re-register UserAdmin
# admin.site.unregister(DjangoUser)
admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(EmploymentEducationRequest)
admin.site.register(EmergencySemesterDeleteRequest)
admin.site.register(TermModificationRequest)
admin.site.register(ReviewRequest)
admin.site.register(EmergencyRemovalRequest)

# Define Groups and their permissions
admin.site.unregister(Group)  # Unregister existing Group model

class CustomGroupAdmin(admin.ModelAdmin):
    pass

admin.site.register(Group, CustomGroupAdmin)

# Customize admin URLs
admin.site.site_header = 'Custom Admin Panel'  # Change the header text
admin.site.index_title = 'Welcome to the Custom Admin Panel'  # Change the index title
admin.site.site_title = 'Admin Panel'  # Change the browser tab title
