from django.db import models
from django.core.validators import FileExtensionValidator

from base_files.models import BaseModel

# Create your models here.

class EmploymentEducationRequest(BaseModel):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_employment_education')
    # term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='term_semester_delete')
    employment_education_file = models.ImageField(upload_to='employment_education_file/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg'])])
    certificate_place = models.CharField(max_length=64)

class RequestResult(models.TextChoices):
    without_years = '1', 'Without years'
    with_years = '0', 'With years'

class EmergencySemesterDeleteRequest(BaseModel):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_semester_delete')
    # term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='term_semester_delete')
    request_result = models.CharField(max_length=64, choices=RequestResult.choices, default=RequestResult.with_years)
    student_comment = models.TextField(blank=True, null=True)
    superviser_comment = models.TextField(blank=True, null=True)
