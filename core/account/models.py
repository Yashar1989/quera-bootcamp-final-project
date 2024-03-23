from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .validators import is_valid_national_code, is_valid_mobile
import uuid
# Create your models here.


class CustomUserManager(BaseUserManager):
    def __create_user(self, password, user_code, **kwargs):
        user = self.model(
            user_code=user_code, **kwargs
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_student(self, password, **kwargs):
        user_code = f's{kwargs.get("national_code")}'
        user = self.__create_user(password, user_code, **kwargs)
        student = Student.objects.create(user=user)
        student.save()
        return user

    def create_assistant(self, password, **kwargs):
        user_code = f'a{kwargs.get("national_code")}'
        user = self.__create_user(password, user_code, **kwargs)
        assistant = Student.objects.create(
            user=user,
            faculty=kwargs.get('faculty'),
            field_of_study=kwargs.get('field_of_study'),
            )
        assistant.save()
        return user

    def create_professor(self, password, **kwargs):
        user_code = f'a{kwargs.get("national_code")}'
        user = self.__create_user(password, user_code, **kwargs)
        professor = Student.objects.create(
            user=user,
            faculty=kwargs.get('faculty'),
            field_of_study=kwargs.get('field_of_study'),
            proficiency=kwargs.get('proficiency')
            )

        professor.save()
        return user

    def create_superuser(self, password, **kwargs):
        """
        Create and save a it manager
        """
        user_code = f's{kwargs.get("national_code")}'
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        return self.__create_user(password, user_code, **kwargs)



class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, verbose_name='نام')
    last_name = models.CharField(max_length=255, verbose_name='نام خانوادگی')
    user_code = models.CharField(max_length=11, unique=True)
    image = models.ImageField(upload_to='profile', null=True, blank=True, verbose_name='عکس پروفایل')
    phone_number = models.BigIntegerField(unique=True, validators=[is_valid_mobile], verbose_name='تلفن همراه', null=True, blank=True)
    national_code = models.CharField(max_length=10, unique=True, validators=[is_valid_national_code],verbose_name='کد ملی')
    gender = models.CharField(max_length=4, choices=(('آقا', 'آقا'), ('خانم', 'خانم')), verbose_name='جنسیت')
    birth_date = models.DateField(verbose_name='تاریخ تولد')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'national_code'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'birth_date']

    class Meta:
        unique_together = ['user_code', 'national_code']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='student')
    # college = models.ForeignKey()
    supervisor = models.ManyToManyField(to='Professor', related_name='supervisor')
    # seniority = models.ManyToManyField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Assistant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    faculty = models.CharField(max_length=255, verbose_name='دانشکده')
    field_of_study = models.CharField(max_length=255, verbose_name='رشته')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Professor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    faculty = models.CharField(max_length=255, verbose_name='دانشکده')
    field_of_study = models.CharField(max_length=255, verbose_name='رشته')
    proficiency = models.CharField(max_length=255, verbose_name='تخصص')
    order = models.CharField(max_length=255, verbose_name='مرتبه')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

