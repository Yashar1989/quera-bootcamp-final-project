from django.test import TestCase
from .models import EmploymentEducationRequest, EmergencySemesterDeleteRequest, RequestResult
from account.models import Student
from lesson.models import Term
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.contrib import admin
from .models import EmploymentEducationRequest, EmergencySemesterDeleteRequest, TermModificationRequest, ReviewRequest, EmergencyRemovalRequest
from account.models import Student, Professor
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .admin import UserAdmin, CustomGroupAdmin

# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name='Test Student')
        self.term = Term.objects.create(name='Test Term')
        
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


class AdminTestCase(TestCase):
    def setUp(self):
        # Create a regular user
        self.user = User.objects.create_user(national_code='0020764685', last_name='test', first_name='test', gender= 'آقا', birth_date='2015-02-02', password='test')

    def test_models_in_admin_panel(self):
        # Log in to the admin panel
        self.client.force_login(self.user)

        # Get the admin panel URL
        admin_url = reverse('admin:index')

        # Access the page for EmploymentEducationRequest model
        response = self.client.get(admin_url + 'app_name/employmenteducationrequest/')

        # Check if the EmploymentEducationRequest model is displayed in the admin panel
        self.assertEqual(response.status_code, 200)

        # Check for the presence of content related to the EmploymentEducationRequest model on the page
        self.assertContains(response, 'Employment Education Requests')

    def test_user_admin_inline_student(self):
        # Test for the addition of the Student inline to the User admin panel
        self.assertIn(Student, UserAdmin.inlines)

    def test_user_admin_inline_professor(self):
        # Test for the addition of the Professor inline to the User admin panel
        self.assertIn(Professor, UserAdmin.inlines)

    def test_custom_group_admin(self):
        # Test for registering the custom Group model in the admin panel
        self.assertTrue(Group in admin.site._registry)
        self.assertIsInstance(admin.site._registry[Group], CustomGroupAdmin)

    def test_user_model_admin(self):
        # Test for registering the User model in the admin panel
        self.assertTrue(User in admin.site._registry)
        self.assertIsInstance(admin.site._registry[User], UserAdmin)

    def test_admin_panel_headers(self):
        # Test for the settings of admin panel headers
        self.assertEqual(admin.site.site_header, 'Custom Admin Panel')
        self.assertEqual(admin.site.index_title, 'Welcome to the Custom Admin Panel')
        self.assertEqual(admin.site.site_title, 'Admin Panel')

    def test_model_registration(self):
        # Test for registering models in the admin panel
        self.assertTrue(EmploymentEducationRequest in admin.site._registry)
        self.assertTrue(EmergencySemesterDeleteRequest in admin.site._registry)
        self.assertTrue(TermModificationRequest in admin.site._registry)
        self.assertTrue(ReviewRequest in admin.site._registry)
        self.assertTrue(EmergencyRemovalRequest in admin.site._registry)