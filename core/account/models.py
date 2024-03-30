from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager, Group
from django.db import models
from .validators import is_valid_national_code, is_valid_mobile
import uuid
from college.models import Faculty, Field


# Create your models here.


class CustomUserManager(BaseUserManager):

    def __create_user(self, password, user_code, **kwargs):
        self.model = User
        user = self.model(
            user_code=user_code,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_student(self, password, **kwargs):
        user_code = f's{kwargs.get("national_code")}'
        field = Field.objects.get(id=kwargs.pop('field'))
        supervisor = Professor.objects.get(id=kwargs.pop('supervisor'))
        seniority = kwargs.pop('seniority')
        user = self.__create_user(password, user_code, **kwargs)
        student = Student.objects.create(
            user=user,
            field=field,
            supervisor=supervisor,
            seniority=seniority,
        )
        student.save()
        return user

    def create_assistant(self, password, **kwargs):
        user_code = f'a{kwargs.get("national_code")}'
        faculty = Faculty.objects.get(pk=kwargs.pop('faculty')['id'])
        kwargs.setdefault("is_staff", True)
        user = self.__create_user(password, user_code, **kwargs)
        group = Group.objects.get(name='assistant')
        user.groups.add(group)
        assistant = Assistant.objects.create(
            user=user,
            faculty=faculty,
        )
        assistant.save()
        return assistant

    def create_professor(self, password, **kwargs):
        user_code = f'p{kwargs.get("national_code")}'
        faculty = Faculty.objects.get(name=kwargs.pop('faculty'))
        proficiency = kwargs.pop('proficiency'),
        order = kwargs.pop('order')
        user = self.__create_user(password, user_code, **kwargs)
        professor = Professor.objects.create(
            user=user,
            faculty=faculty,
            proficiency=proficiency,
            order=order
        )

        professor.save()
        return user

    def create_superuser(self, password, **kwargs):
        """
        Create and save it manager
        """
        user_code = f'i{kwargs.get("national_code")}'
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        return self.__create_user(password, user_code, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, verbose_name='نام')
    last_name = models.CharField(max_length=255, verbose_name='نام خانوادگی')
    user_code = models.CharField(max_length=11, unique=True)
    image = models.ImageField(upload_to='profile', null=True, blank=True, verbose_name='عکس پروفایل')
    phone_number = models.BigIntegerField(unique=True, validators=[is_valid_mobile], verbose_name='تلفن همراه',
                                          null=True, blank=True)
    national_code = models.CharField(max_length=10, validators=[is_valid_national_code],
                                     verbose_name='کد ملی')
    gender = models.CharField(max_length=4, choices=(('آقا', 'آقا'), ('خانم', 'خانم')), verbose_name='جنسیت')
    birth_date = models.DateField(verbose_name='تاریخ تولد')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'user_code'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'birth_date']

    class Meta:
        unique_together = ['user_code', 'national_code']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='student')
    field = models.ForeignKey(to='college.Field', on_delete=models.PROTECT, related_name='field_students')
    supervisor = models.ForeignKey(to='Professor',
                                   related_name='supervisor',
                                   on_delete=models.PROTECT,
                                   default='cf1df455-e983-49a9-96df-8bf7c3fd4b7c'
                                   )
    seniority = models.CharField(max_length=1, blank=True, null=True, choices=(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    ))

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Assistant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='assistant')
    faculty = models.ForeignKey(to='college.Faculty', on_delete=models.CASCADE, verbose_name='دانشکده',
                                related_name='assistant')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Professor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(to='college.Faculty', on_delete=models.CASCADE, verbose_name='دانشکده',
                                related_name='professors')
    proficiency = models.CharField(max_length=255, verbose_name='تخصص')
    order = models.CharField(max_length=255, verbose_name='مرتبه')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
