from django.urls import path, include

from .views import CreateAssistantAPIView, AssistantAPIView

app_name = 'account'
urlpatterns = [
    path('assistant/', CreateAssistantAPIView.as_view(), name='create_assistant'),
    path('assistant/<uuid:pk>/', AssistantAPIView.as_view(), name='assistant')
]
