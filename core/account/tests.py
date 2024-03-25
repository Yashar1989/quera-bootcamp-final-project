from django.test import TestCase
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


