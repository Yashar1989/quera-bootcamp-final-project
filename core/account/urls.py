from django.urls import path, include

from .views import CreateAssistantAPIView

app_name = 'account'
urlpatterns = [
    path('assistant/', CreateAssistantAPIView.as_view(), name='assistant'),
]
