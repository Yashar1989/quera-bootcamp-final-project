# Generated by Django 4.2.11 on 2024-03-28 11:21

import account.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255, verbose_name='نام')),
                ('last_name', models.CharField(max_length=255, verbose_name='نام خانوادگی')),
                ('user_code', models.CharField(max_length=11, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='عکس پروفایل')),
                ('phone_number', models.BigIntegerField(blank=True, null=True, unique=True, validators=[account.validators.is_valid_mobile], verbose_name='تلفن همراه')),
                ('national_code', models.CharField(max_length=10, unique=True, validators=[account.validators.is_valid_national_code], verbose_name='کد ملی')),
                ('gender', models.CharField(choices=[('آقا', 'آقا'), ('خانم', 'خانم')], max_length=4, verbose_name='جنسیت')),
                ('birth_date', models.DateField(verbose_name='تاریخ تولد')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('proficiency', models.CharField(max_length=255, verbose_name='تخصص')),
                ('order', models.CharField(max_length=255, verbose_name='مرتبه')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('seniority', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=1, null=True)),
            ],
        ),
    ]
