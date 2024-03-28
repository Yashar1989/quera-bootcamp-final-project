from django.contrib import admin
from .models import Faculty, Field, SelectUnit, Department

# Register your models here.


admin.site.register(Faculty)
admin.site.register(Field)
admin.site.register(SelectUnit)
admin.site.register(Department)
