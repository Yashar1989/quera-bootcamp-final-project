from django.urls import path
from .views import RegisterProfessorView

urlpatterns = [
    path('professors/', RegisterProfessorView.as_view() , name='registerprofesorview'),
]
