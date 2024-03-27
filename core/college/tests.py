from django.test import TestCase
from .models import College

# Create your tests here.
class CollegeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # ایجاد یک نمونه از مدل College برای تست
        College.objects.create(name='Test College')

    def test_name_label(self):
        # تست برچسب فیلد name
        college = College.objects.get(id=1)
        field_label = college._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        # تست حداکثر طول فیلد name
        college = College.objects.get(id=1)
        max_length = college._meta.get_field('name').max_length
        self.assertEquals(max_length, 250)

    def test_name_blank(self):
        # تست اینکه فیلد name آیا با مقدار خالی قابل ذخیره سازی است یا نه
        college = College.objects.get(id=1)
        field_blank = college._meta.get_field('name').blank
        self.assertFalse(field_blank)

    def test_name_null(self):
        # تست اینکه فیلد name آیا با مقدار Null قابل ذخیره سازی است یا نه
        college = College.objects.get(id=1)
        field_null = college._meta.get_field('name').null
        self.assertFalse(field_null)

    def test_object_name_is_name(self):
        # تست نام نمایشی مدل
        college = College.objects.get(id=1)
        expected_object_name = college.name
        self.assertEquals(expected_object_name, str(college))