from django.db import models
from base_files.models import BaseModel
import uuid
# Create your models here.



class College(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name





class Field(BaseModel):
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
    
    def __str__(self):
        return self.name

    

    

class SelectUnit(BaseModel):
    applicant_student = models.ForeignKey(to='account.Student', on_delete=models.CASCADE)
    on_demand_courses = models.ForeignKey(to='lesson.Lesson', on_delete=models.CASCADE)
    apporoval_student = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name





class LeranGroup(BaseModel):
    name = models.CharField(max_length=250)
    subgroup = models.ForeignKey(to='self', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name