from django.urls import path, include
from .views import CreateAssistantAPIView, AssistantAPIView, RegisterProfessorView,UpdateDeleteProfessorView, CreateTermAPIView, DetailTermAPIView
from .views import RegisterProfessorView, CreateTermAPIView, DetailTermAPIView

app_name = 'account'

urlpatterns = [
    path('professors/', RegisterProfessorView.as_view(), name='register_profesor'),
    path('term/', CreateTermAPIView.as_view(), name='create_term'),
    path('term/<uuid:pk>/', DetailTermAPIView.as_view(), name='detail_term'),
]
