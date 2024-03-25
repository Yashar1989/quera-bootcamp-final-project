from django.contrib import admin
from .models import EmploymentEducationRequest, EmergencyRemovalRequest, TermModificationRequest, ReviewRequest, EmergencySemesterDeleteRequest

@admin.register(EmploymentEducationRequest)
class EmployeeEducationRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'term', 'certification_place')
    list_filter = ('term',)
    search_fields = ('student_name', 'certificate_place')

@admin.register(EmergencySemesterDeleteRequest)
class EmergencySemesterDeleteRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'term', 'request_results')
    list_filter = ('term', 'request_results')
    search_fields = ('student_name',)

@admin.register(TermModificationRequest)
class TermModificationRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'added_course', 'removed_course', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('student_name', 'added_course__title', 'removed_course__title')

@admin.register(ReviewRequest)
class ReviewRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'review_text', 'response')
    search_fields = ('student__name', 'course__title')

@admin.register(EmergencyRemovalRequest)
class EmergencyRemovalRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'request_result', 'student_comment', 'admin_comment')
    list_filter = ('request_result',)
    search_fields = ('student__name', 'course__title')
