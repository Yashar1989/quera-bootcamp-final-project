from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

import uuid
# Create your models here.

User = get_user_model()

class EmploymentEducationRequest(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_semester_delete')
    employment_education_file = models.ImageField(upload_to='employment_education_file/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg'])])
    # term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='term_semester_delete')
    certificate_place = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RequestResult(models.TextChoices):
    without_years = '1', 'Without years'
    with_years = '0', 'With years'

class EmergencySemesterDeleteRequest(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_semester_delete')
    # term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='term_semester_delete')
    request_result = models.CharField(max_length=64, choices=RequestResult.choices, default=RequestResult.with_years)
    student_comment = models.TextField(blank=True, null=True)
    superviser_comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)