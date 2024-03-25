from django.urls import path, include
from .views import CreateAssistantAPIView, AssistantAPIView, RegisterProfessorView, UpdateDeleteProfessorView


app_name = 'account'
urlpatterns = [
    path('assistant/', CreateAssistantAPIView.as_view(), name='create_assistant'),
    path('assistant/<uuid:pk>/', AssistantAPIView.as_view(), name='assistant'),
    path('professors/', RegisterProfessorView.as_view() , name='register_profesor'),
    path('professors/<uuid:pk>', UpdateDeleteProfessorView.as_view() , name='edit_profesor'),
    
]
