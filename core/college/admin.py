from django.contrib import admin
from .models import Faculty, Field, SelectUnit, Department

# Register your models here.
class FieldAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'unit_number', 'degree']


class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name' ,)

    
class SelectUnitAdmin(admin.ModelAdmin):
    list_display = ('applicant_student','on_demand_courses','apporoval_student')


class DepartementAdmin(admin.ModelAdmin):
    list_display = ('faculty' ,'name' ,'manager')



admin.site.register(Field ,FieldAdmin)
admin.site.register(Faculty ,FacultyAdmin)
admin.site.register(SelectUnit ,SelectUnitAdmin)
admin.site.register(Department ,DepartementAdmin)
