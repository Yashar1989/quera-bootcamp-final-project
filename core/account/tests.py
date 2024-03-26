from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from lesson.models import Term
from .serializers import TermSerializer
from .models import User

class TestUserModel(TestCase):

    def test_create_it_manager_with_valid_data(self):
        user = User.objects.create_superuser(
            password='admin',
            first_name='yashar',
            last_name='amirabedin',
            national_code='0010688765',
            gender='آقا',
            birth_date='1989-09-14'
        )
        self.assertEqual(user.first_name, 'yashar')
        self.assertTrue(user.is_staff)
        self.assertEqual(user.national_code, '0010688765')



class TermAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_term_url = reverse('account:create_term')
        self.detail_term_url = reverse('account:detail_term', kwargs={'pk': '903c0425-5501-4939-9186-1f12ffeb2d3d'})

    def test_create_term(self):
        """
        Ensure we can create a new term object.
        """
        data = {
            "name": "Test Term",
            "select_unit_start_time": "2024-03-26T10:00:00Z",
            "select_unit_end_time": "2024-03-26T11:00:00Z",
            "class_start_time": "2024-03-26",
            "class_end_time": "2024-03-27",
            "amendment_start_time": "2024-03-26T10:00:00Z",
            "amendment_end_time": "2024-03-27T10:00:00Z",
            "emergency_removal_end_time": "2024-03-28T10:00:00Z",
            "exams_start_time": "2024-03-29",
            "term_end_time": "2024-03-30"
        }
        response = self.client.post(self.create_term_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_duplicate_term(self):
        """
        Ensure we cannot create a term with a duplicate name.
        """
        # Create a term
        data = {
            "name": "Test Term",
            "select_unit_start_time": "2024-03-26T10:00:00Z",
            "select_unit_end_time": "2024-03-26T11:00:00Z",
            "class_start_time": "2024-03-26",
            "class_end_time": "2024-03-27",
            "amendment_start_time": "2024-03-26T10:00:00Z",
            "amendment_end_time": "2024-03-27T10:00:00Z",
            "emergency_removal_end_time": "2024-03-28T10:00:00Z",
            "exams_start_time": "2024-03-29",
            "term_end_time": "2024-03-30"
        }
        response = self.client.post(self.create_term_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Try to create a term with the same name
        response = self.client.post(self.create_term_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_retrieve_term(self):
        """
        Ensure we can retrieve a term object.
        """
        term = Term.objects.create(
            name="Test Term",
            select_unit_start_time="2024-03-26T10:00:00Z",
            select_unit_end_time="2024-03-26T11:00:00Z",
            class_start_time="2024-03-26",
            class_end_time="2024-03-27",
            amendment_start_time="2024-03-26T10:00:00Z",
            amendment_end_time="2024-03-27T10:00:00Z",
            emergency_removal_end_time="2024-03-28T10:00:00Z",
            exams_start_time="2024-03-29",
            term_end_time="2024-03-30"
        )
        response = self.client.get(reverse('account:detail_term', kwargs={'pk': term.id}))
        term_serializer = TermSerializer(term)
        self.assertEqual(response.data, term_serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_term(self):
        """
        Ensure we can update a term object.
        """
        term = Term.objects.create(
            name="Test Term",
            select_unit_start_time="2024-03-26T10:00:00Z",
            select_unit_end_time="2024-03-26T11:00:00Z",
            class_start_time="2024-03-26",
            class_end_time="2024-03-27",
            amendment_start_time="2024-03-26T10:00:00Z",
            amendment_end_time="2024-03-27T10:00:00Z",
            emergency_removal_end_time="2024-03-28T10:00:00Z",
            exams_start_time="2024-03-29",
            term_end_time="2024-03-30"
        )
        updated_data = {
            "name": "Updated Test Term"
        }
        response = self.client.put(reverse('account:detail_term', kwargs={'pk': term.id}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        term.refresh_from_db()
        self.assertEqual(term.name, updated_data['name'])

    def test_delete_term(self):
        """
        Ensure we can delete a term object.
        """
        term = Term.objects.create(
            name="Test Term",
            select_unit_start_time="2024-03-26T10:00:00Z",
            select_unit_end_time="2024-03-26T11:00:00Z",
            class_start_time="2024-03-26",
            class_end_time="2024-03-27",
            amendment_start_time="2024-03-26T10:00:00Z",
            amendment_end_time="2024-03-27T10:00:00Z",
            emergency_removal_end_time="2024-03-28T10:00:00Z",
            exams_start_time="2024-03-29",
            term_end_time="2024-03-30"
        )
        response = self.client.delete(reverse('account:detail_term', kwargs={'pk': term.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
