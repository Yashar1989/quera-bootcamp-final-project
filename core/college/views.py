from django.shortcuts import render
from .models import Faculty
from .serializers import FacultySerializers
from rest_framework.generics import ListCreateAPIView ,RetrieveDestroyAPIView
from rest_framework.permissions import IsAdminUser

# Create your views here.

class FacultyListViews(ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers
    permission_classes = (IsAdminUser ,)



class FacultyUpdateView(RetrieveDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers
    permission_classes = (IsAdminUser ,)