import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

<<<<<<< HEAD
=======

# Create your models here.
class Term(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    select_unit_start_time = models.DateTimeField(null=False, blank=False)
    select_unit_end_time = models.DateTimeField(null=False, blank=False)
    class_start_time = models.DateField(null=False, blank=False)
    class_end_time = models.DateField(null=False, blank=False)
    amendment_start_time = models.DateTimeField(null=False, blank=False)
    amendment_end_time = models.DateTimeField(null=False, blank=False)
    emergency_removal_end_time = models.DateTimeField(null=False, blank=False)
    exams_start_time = models.DateField(null=False, blank=False)
    term_end_time = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.name


class PresentationTime(models.Model):
    day_choices = (
        (1, 'Saturday'),
        (2, 'Sunday'),
        (3, 'Monday'),
        (4, 'Tuesday'),
        (5, 'Wednesday'),
        (6, 'Thursday'),
        (7, 'Friday')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    day = models.SmallIntegerField(null=False, blank=False, choices=day_choices)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)

    def __str__(self):
        for day_num, day_name in self.day_choices:
            if day_num == self.day:
                return day_name
        return "Invalid Day"


class Lesson(models.Model):
    unit_type_choices = (
        (1, 'specialized'),
        (2, 'general'),
        (3, 'base'),
        (4, 'optional')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    college = models.ForeignKey(to='college.College', on_delete=models.SET_DEFAULT, default='0-0-0-0', related_name='lessons')
    prerequisite = models.ManyToManyField(to='self')
    corequisite = models.ManyToManyField(to='self')
    unit = models.SmallIntegerField(null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(4)])
    type = models.SmallIntegerField(null=False, blank=False, choices=unit_type_choices)

    def __str__(self):
        return self.name


class TermLesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson = models.ForeignKey(to='lesson.Lesson', on_delete=models.SET_DEFAULT, default='0-0-0-0',
                               related_name='presented')

    presentation_time = models.ManyToManyField(to='lesson.PresentationTime', related_name='lessons')
    exam_time = models.DateTimeField(null=False, blank=False)
    lecturer = models.ForeignKey(to='account.Professor', on_delete=models.SET_NULL, null=True, related_name='teached_lessons')
    capacity = models.IntegerField(default=25)
    term = models.ForeignKey(to='lesson.Term', on_delete=models.PROTECT, related_name='term_lessons')

    def __str__(self):
        return self.lesson.name + self.term.name

 
class RegisteredLesson(models.Model):
    status_choices = (
        (1, 'Registered'),
        (2, 'Accepted'),
        (3, 'Removed'),  # set this status when a Student remove a lesson in emergency removal
        (4, 'Locked')  # set this status when term is closed
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson = models.ForeignKey(to='lesson.TermLesson', on_delete=models.PROTECT, related_name='registered_students')
    student = models.ForeignKey(to='account.Student', on_delete=models.PROTECT, related_name='registered_lessons')
    status = models.SmallIntegerField(null=False, blank=False, choices=status_choices)
    grade = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])

    def __str__(self):
        return self.lesson.name  # todo add self.student.name

>>>>>>> 77c119ae1d8c4343f5ebf5b1d11afc2d725c3581
