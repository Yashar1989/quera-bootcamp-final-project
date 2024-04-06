from django.urls import path, include
from .views import CreateAssistantAPIView, AssistantAPIView, RegisterProfessorView,UpdateDeleteProfessorView
from .views import RegisterProfessorView

app_name = 'account'

urlpatterns = [
    path('professors/', RegisterProfessorView.as_view(), name='register_profesor'),
]
