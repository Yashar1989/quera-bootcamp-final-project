from django.db import models
from base_files.models import BaseModel
import uuid
# Create your models here.



class College(BaseModel):
    name = models.CharField(max_length=250)


class Fields(BaseModel):
    DEGREES_CHOICES=[
        ('advanced_diploma' ,'Advanced Diploma'),
        ('bachelor' ,'Bachelor'),
        ('master' ,'Master'),
        ('doctorate' ,'Doctorate'),
        ('post_doctorate' ,'Post Doctorate'),
    ]
    name = models.CharField(max_length=250)
    leran_group = models.CharField(max_length=250)
    number_unit = models.IntegerField()
    degrees = models.CharField(max_length=50,choices=DEGREES_CHOICES)

class SelectUnits(BaseModel):
    applicant_student = models.ForeignKey(to='account.Student', on_delete=models.CASCADE)
    on_demand_courses = models.ForeignKey(to='lesson.Lesson', on_delete=models.CASCADE)
    apporoval_student = models.BooleanField(default=False)

class LeranGroup(BaseModel):
    name = models.CharField(max_length=250)
    # subgroup = models.UUIDField(primary_key=True , default=uuid.uuid4 ,editable=False)