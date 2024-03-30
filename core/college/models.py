from django.db import models
from base_files.models import BaseModel


# Create your models here.

class Faculty(BaseModel):
    name = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.name


class Department(BaseModel):
    faculty = models.ForeignKey(to='Faculty', on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255, null=False, blank=False)
    manager = models.ForeignKey(to='account.Professor', on_delete=models.CASCADE)
    professors = models.ManyToManyField(to='account.Professor', related_name='departments')

    def __str__(self):
        return self.name + self.faculty.name


class Field(BaseModel):
    DEGREES_CHOICES = [
        ('advanced_diploma', 'Advanced Diploma'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctorate', 'Doctorate'),
        ('post_doctorate', 'Post Doctorate'),
    ]
    name = models.CharField(max_length=255, null=False, blank=False)
    department = models.ForeignKey(to='Department', on_delete=models.CASCADE, related_name='fields')
    unit_number = models.PositiveIntegerField()
    degree = models.CharField(max_length=50, choices=DEGREES_CHOICES)

    def __str__(self):
        return self.name + ' ' + self.degree


class SelectUnit(BaseModel):
    applicant_student = models.ForeignKey(to='account.Student', on_delete=models.CASCADE)
    on_demand_courses = models.ForeignKey(to='lesson.Lesson', on_delete=models.CASCADE)
    apporoval_student = models.BooleanField(default=False)

    def __str__(self):
        return self.name
