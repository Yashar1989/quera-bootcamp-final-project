from django.urls import path
from .views.main_views import CreateStudent, ListStudents, FilterStudents, UpdateStudent, RetrieveStudent, DeleteStudent
from .views.account_views import CreateAssistantAPIView, AssistantAPIView

app_name = 'api_v1'

urlpatterns = [
    path('create-student/', CreateStudent.as_view(), name='create-student'),
    path('list-students/', ListStudents.as_view(), name='list-students'),
    path('filter-students/', FilterStudents.as_view(), name='filter-students'),
    path('student/<slug:user_code>/', RetrieveStudent.as_view(), name='retrieve-student'),
    path('student/<slug:user_code>/update/', UpdateStudent.as_view(), name='update-student'),
    path('student/<slug:user_code>/delete/', DeleteStudent.as_view(), name='delete-student')
    path('assistant/', CreateAssistantAPIView.as_view(), name='create_assistant'),
    path('assistant/<uuid:pk>/', AssistantAPIView.as_view(), name='assistant'),
]

