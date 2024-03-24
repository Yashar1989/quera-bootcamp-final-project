from django.shortcuts import render
from .models import Professor
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from .serializers import ProfessorSerializers



# Create your views here.

class RegisterProfessorView(ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializers
    permission_classes = (IsAdminUser ,)