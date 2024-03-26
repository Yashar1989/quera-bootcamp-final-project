from django.test import TestCase
from .models import EmploymentEducationRequest, EmergencySemesterDeleteRequest, RequestResult
from account.models import Student, User, Professor
from lesson.models import Term
from college.models import College

# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(user=User.objects.first(), college=College.objects.first(), supervisor=Professor.objects.first(), seniority=1)
        self.term = Term.objects.create(name='Test Term', select_unit_start_time='2024-03-26 10:43:17', select_unit_end_time='2024-03-26 10:43:15',
                                            class_start_time='2024-03-26', class_end_time='2024-03-26', amendment_start_time='2024-03-26 10:43:08', 
                                            amendment_end_time='2024-03-26 10:43:03', emergency_removal_end_time='2024-03-26 10:43:00', 
                                            exams_start_time='2024-03-26', term_end_time='2024-03-26'
                                        )
        
    def test_employment_education_request_creation(self):
        employment_education_request = EmploymentEducationRequest.objects.create(
            student=self.student,
            term=self.term,
            employment_education_file='path/to/file.jpg',
            certificate_place='Test Place'
        )
        self.assertEqual(employment_education_request.student, self.student)
        self.assertEqual(employment_education_request.term, self.term)
        self.assertEqual(employment_education_request.certificate_place, 'Test Place')

    def test_emergency_semester_delete_request_creation(self):
        emergency_semester_delete_request = EmergencySemesterDeleteRequest.objects.create(
            student=self.student,
            term=self.term,
            request_result=RequestResult.with_years,
            student_comment='Test Comment',
            superviser_comment='Test Comment'
        )
        self.assertEqual(emergency_semester_delete_request.student, self.student)
        self.assertEqual(emergency_semester_delete_request.term, self.term)
        self.assertEqual(emergency_semester_delete_request.request_result, RequestResult.with_years)
        self.assertEqual(emergency_semester_delete_request.student_comment, 'Test Comment')
        self.assertEqual(emergency_semester_delete_request.superviser_comment, 'Test Comment')

