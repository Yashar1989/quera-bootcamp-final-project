from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from account.models import Student
from lesson.models import TermLesson, Term, Lesson
from ..serializers.main_serializers import StudentSerializer
from django.db.models import Q
from ..serializers.main_serializers import FilteredStudentSerializer, DetailedStudentSerializer
from ..serializers.lesson_serializers import TermViewSerializer, LessonListSerializer
from rest_framework import generics
from ..permissions import IsStudentOrProfessor
from datetime import datetime


class CreateStudent(APIView):
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListStudents(APIView):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FilterStudents(APIView):
    def get(self, request, *args, **kwargs):
        name = request.query_params.get('name', None)
        student_id = request.query_params.get('student_id', None)
        national_code = request.query_params.get('national_code', None)
        college = request.query_params.get('college', None)
        seniority = request.query_params.get('seniority', None)

        query = Q()
        if name:
            query &= Q(user__first_name__icontains=name) | Q(user__last_name__icontains=name)
        if student_id:
            query &= Q(user__user_code=student_id)
        if national_code:
            query &= Q(user__national_code=national_code)
        if college:
            query &= Q(college__name=college)
        if seniority:
            query &= Q(seniority=seniority)

        students = Student.objects.filter(query)
        serializer = FilteredStudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveStudent(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = DetailedStudentSerializer
    lookup_field = 'user__user_code'


class UpdateStudent(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'user__user_code'


class DeleteStudent(generics.DestroyAPIView):
    queryset = Student.objects.all()
    lookup_field = 'user__user_code'


class TermListAPIView(generics.ListAPIView):
    permission_classes = [IsStudentOrProfessor]
    queryset = Term.objects.filter(term_end_time__gte=datetime.now())
    serializer_class = TermViewSerializer


class TermDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsStudentOrProfessor]
    queryset = Term.objects.filter(term_end_time__gte=datetime.now())
    serializer_class = TermViewSerializer


class CourseSelectAPIView(generics.ListAPIView):
    serializer_class = LessonListSerializer
    queryset = Lesson.objects.all()
