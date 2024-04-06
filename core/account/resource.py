from import_export import resources 
from .models import Student, Professor

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student

class ProfessorResource(resources.ModelResource):
    class Meta:
        model = Professor