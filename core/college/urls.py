from django.urls import path
from .views import FacultyListViews

urlpatterns =[
    path('faculties/' ,FacultyListViews.as_view() ,name='faculty_create'),
    # path('faculties/<uuid:pk>/' ,FacultyUpdateView.as_view() ,name='faculty_create'),
]