from django.urls import path
from .views.account_views import CreateAssistantAPIView, AssistantAPIView

app_name = 'api_v1'

urlpatterns = [
    path('assistant/', CreateAssistantAPIView.as_view(), name='create_assistant'),
    path('assistant/<uuid:pk>/', AssistantAPIView.as_view(), name='assistant'),
]
