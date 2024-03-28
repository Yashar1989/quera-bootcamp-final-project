# Generated by Django 4.2.11 on 2024-03-28 11:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('unit', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('type', models.SmallIntegerField(choices=[(1, 'specialized'), (2, 'general'), (3, 'base'), (4, 'optional')])),
                ('college', models.ForeignKey(default='0-0-0-0', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='lessons', to='college.faculty')),
                ('corequisite', models.ManyToManyField(to='lesson.lesson')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='field_lessons', to='college.field')),
                ('prerequisite', models.ManyToManyField(to='lesson.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='PresentationTime',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('day', models.SmallIntegerField(choices=[(1, 'Saturday'), (2, 'Sunday'), (3, 'Monday'), (4, 'Tuesday'), (5, 'Wednesday'), (6, 'Thursday'), (7, 'Friday')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('select_unit_start_time', models.DateTimeField()),
                ('select_unit_end_time', models.DateTimeField()),
                ('class_start_time', models.DateField()),
                ('class_end_time', models.DateField()),
                ('amendment_start_time', models.DateTimeField()),
                ('amendment_end_time', models.DateTimeField()),
                ('emergency_removal_end_time', models.DateTimeField()),
                ('exams_start_time', models.DateField()),
                ('term_end_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TermLesson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('exam_time', models.DateTimeField()),
                ('capacity', models.IntegerField(default=25)),
                ('lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teached_lessons', to='account.professor')),
                ('lesson', models.ForeignKey(default='0-0-0-0', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='presented', to='lesson.lesson')),
                ('presentation_time', models.ManyToManyField(related_name='lessons', to='lesson.presentationtime')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='term_lessons', to='lesson.term')),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredLesson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.SmallIntegerField(choices=[(1, 'Registered'), (2, 'Accepted'), (3, 'Removed'), (4, 'Locked')])),
                ('grade', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registered_students', to='lesson.termlesson')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registered_lessons', to='account.student')),
            ],
        ),
    ]
