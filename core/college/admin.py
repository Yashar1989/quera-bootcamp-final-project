from django.contrib import admin
from .models import Faculty, Field, SelectUnit, Department

# Register your models here.
@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'unit_number', 'degree']


admin.site.register(Faculty)
admin.site.register(SelectUnit)
admin.site.register(Department)
