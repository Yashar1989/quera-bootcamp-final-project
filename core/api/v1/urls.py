from django.urls import path
from .views.main_views import (
    CreateStudent,
    ListStudents,
    FilterStudents,
    UpdateStudent,
    RetrieveStudent,
    DeleteStudent,
    TermListAPIView,
)
from .views.account_views import CreateAssistantAPIView, AssistantAPIView
from .views.lesson_views import LessonCreateAPIView, LessonRetrieveUpdateDestroyAPIView

app_name = 'api_v1'

urlpatterns = [
    path('create-student/', CreateStudent.as_view(), name='create-student'),
    path('list-students/', ListStudents.as_view(), name='list-students'),
    path('filter-students/', FilterStudents.as_view(), name='filter-students'),
    path('student/<slug:user_code>/', RetrieveStudent.as_view(), name='retrieve-student'),
    path('student/<slug:user_code>/update/', UpdateStudent.as_view(), name='update-student'),
    path('student/<slug:user_code>/delete/', DeleteStudent.as_view(), name='delete-student'),
    path('assistant/', CreateAssistantAPIView.as_view(), name='create_assistant'),
    path('assistant/<uuid:pk>/', AssistantAPIView.as_view(), name='assistant'),
    path('subjects/', LessonCreateAPIView.as_view(), name='lesson'),
    path('subjects/<slug:pk>/', LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson_update_delete'),


    # section 'e' urls
    path('terms/', TermListAPIView.as_view(), name='term_list_view'),
    # path('term/<int:pk>/', TermDetailAPIView.as_view(), name='term_detail_view'),
    # path('student/<int:pk>/my-cources', CourseSelectAPIView.as_view(), name='course_select'),
    # path('/student/<int:pk>/pass-courses-report', PassCoursesAPIView.as_view(), name='pass_courses'),
    # path('/student/<int:pk>/term-courses/', PassingCoursesAPIView.as_view(), name='passing_course'),
    # path('/student/<int:pk>/remaining-terms/', RemaininTermsAPIView.as_view(), name='remaining_terms'),


]
