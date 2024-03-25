from django.contrib import admin
from .models import College, Field, SelectUnit, LeranGroup

# Register your models here.

admin.site.register(College)
admin.site.register(Field)
admin.site.register(SelectUnit)
admin.site.register(LeranGroup)
