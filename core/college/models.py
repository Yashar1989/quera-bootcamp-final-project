from django.db import models
from base_files.models import BaseModel


# Create your models here.


class College(BaseModel):
    name = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.name


class LearnGroup(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    college = models.ForeignKey(to='College', on_delete=models.CASCADE, related_name='learn_groups')

    def __str__(self):
        return self.name + self.college.name


class Field(BaseModel):
    DEGREES_CHOICES = [
        ('advanced_diploma', 'Advanced Diploma'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctorate', 'Doctorate'),
        ('post_doctorate', 'Post Doctorate'),
    ]
    name = models.CharField(max_length=255, null=False, blank=False)
    learn_group = models.ForeignKey(to='LearnGroup', on_delete=models.CASCADE, related_name='fields')
    unit_number = models.PositiveIntegerField()
    degrees = models.CharField(max_length=50, choices=DEGREES_CHOICES)

    def __str__(self):
        return self.name


class SelectUnit(BaseModel):
    applicant_student = models.ForeignKey(to='account.Student', on_delete=models.CASCADE)
    on_demand_courses = models.ForeignKey(to='lesson.Lesson', on_delete=models.CASCADE)
    apporoval_student = models.BooleanField(default=False)

    def __str__(self):
        return self.name
