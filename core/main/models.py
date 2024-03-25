from django.db import models
from django.core.validators import FileExtensionValidator
from account.models import Student
from lesson.models import Term
from base_files.models import BaseModel

# Create your models here.

class EmploymentEducationRequest(BaseModel):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name='student_employment_education')
    term = models.ForeignKey(to=Term, on_delete=models.CASCADE, related_name='term_semester_delete')
    employment_education_file = models.ImageField(upload_to='employment_education_file/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg'])])
    certificate_place = models.CharField(max_length=64)

class RequestResult(models.TextChoices):
    without_years = '1', 'Without years'
    with_years = '0', 'With years'

class EmergencySemesterDeleteRequest(BaseModel):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name='student_delete')
    term = models.ForeignKey(to=Term, on_delete=models.CASCADE, related_name='term_delete')
    request_result = models.CharField(max_length=64, choices=RequestResult.choices, default=RequestResult.with_years)
    student_comment = models.TextField(blank=True, null=True)
    superviser_comment = models.TextField(blank=True, null=True)

class TermModificationRequest(models.Model):
    student = models.ForeignKey(to='account.Student', on_delete=models.CASCADE)
    added_course = models.ForeignKey(to='lesson.Lesson', related_name='added_courses', on_delete=models.CASCADE)
    removed_course = models.ForeignKey(to='lesson.Lesson', related_name='removed_courses', on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

class ReviewRequest(models.Model):
    student = models.ForeignKey(to='account.Student', on_delete=models.CASCADE)
    course = models.ForeignKey(to='lesson.Lesson', on_delete=models.CASCADE)
    review_text = models.TextField()
    response = models.TextField(blank=True, null=True)

class EmergencyRemovalRequest(models.Model):
    student = models.ForeignKey(to='account.Student', on_delete=models.CASCADE)
    course = models.ForeignKey(to='lesson.Lesson', on_delete=models.CASCADE)
    request_result = models.CharField(max_length=50)
    student_comment = models.TextField()
    admin_comment = models.TextField()
