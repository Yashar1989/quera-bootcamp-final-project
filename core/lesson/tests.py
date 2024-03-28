from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from .models import Term, PresentationTime, Lesson, TermLesson, RegisteredLesson
import uuid

from college.models import College

from account.models import Professor

from account.models import Student


class TermModelTests(TestCase):
    def test_create_term(self):
        term = Term.objects.create(
            name="Test Term",
            select_unit_start_time=timezone.now(),
            select_unit_end_time=timezone.now(),
            class_start_time=timezone.now().date(),
            class_end_time=timezone.now().date(),
            amendment_start_time=timezone.now(),
            amendment_end_time=timezone.now(),
            emergency_removal_end_time=timezone.now(),
            exams_start_time=timezone.now().date(),
            term_end_time=timezone.now().date()
        )

        saved_term = Term.objects.get(name="Test Term")

        self.assertEqual(saved_term, term)

    def test_term_str_representation(self):
        term = Term.objects.create(
            name="Test Term",
            select_unit_start_time=timezone.now(),
            select_unit_end_time=timezone.now(),
            class_start_time=timezone.now().date(),
            class_end_time=timezone.now().date(),
            amendment_start_time=timezone.now(),
            amendment_end_time=timezone.now(),
            emergency_removal_end_time=timezone.now(),
            exams_start_time=timezone.now().date(),
            term_end_time=timezone.now().date()
        )

        self.assertEqual(str(term), "Test Term")

    def test_term_fields_not_null(self):
        term = Term(
            name="Test Term",

        )

        # Try to save the term
        with self.assertRaises(Exception) as context:
            term.save()

        self.assertIn("null value in column", str(context.exception))


class PresentationTimeModelTests(TestCase):
    def test_create_presentation_time(self):
        presentation_time = PresentationTime.objects.create(
            day=1,
            start_time=timezone.now().time(),
            end_time=(timezone.now() + timezone.timedelta(hours=1)).time()
        )

        saved_presentation_time = PresentationTime.objects.get(day=1)

        self.assertEqual(saved_presentation_time, presentation_time)

    def test_presentation_time_str_representation(self):
        presentation_time = PresentationTime.objects.create(
            day=1,  # Saturday
            start_time="08:00:00",
            end_time="10:00:00"
        )

        self.assertEqual(str(presentation_time), "Saturday")

    def test_presentation_time_fields_not_null(self):
        presentation_time = PresentationTime(

        )

        with self.assertRaises(Exception) as context:
            presentation_time.save()

        self.assertIn("null value in column", str(context.exception))


class LessonModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.college = College.objects.create(name='Test Faculty')

    def test_create_lesson(self):
        lesson = Lesson.objects.create(
            name="Test Lesson",
            college=self.college,
            unit=1,
            type=1
        )

        saved_lesson = Lesson.objects.get(name="Test Lesson")

        self.assertEqual(saved_lesson, lesson)

    def test_lesson_str_representation(self):
        lesson = Lesson.objects.create(
            name="Test Lesson",
            college=self.college,
            unit=1,
            type=1
        )

        self.assertEqual(str(lesson), "Test Lesson")

    def test_lesson_fields_not_null(self):
        lesson = Lesson()

        with self.assertRaises(ValidationError) as context:
            lesson.full_clean()

            # Check if null constraint is enforced for required fields
        self.assertIn('name', context.exception.message_dict)
        self.assertIn('college', context.exception.message_dict)
        self.assertIn('unit', context.exception.message_dict)
        self.assertIn('type', context.exception.message_dict)

        # Check specific error messages for each field
        self.assertEqual(context.exception.message_dict['name'][0], 'This field cannot be blank.')
        self.assertEqual(context.exception.message_dict['college'][0], '“0-0-0-0” is not a valid UUID.')
        self.assertEqual(context.exception.message_dict['unit'][0], 'This field cannot be null.')
        self.assertEqual(context.exception.message_dict['type'][0], 'This field cannot be null.')

    def test_lesson_unit_range(self):
        with self.assertRaises(ValidationError) as context:
            lesson = Lesson(
                name="Invalid Lesson",
                college=self.college,
                unit=0,
                type=1
            )
            lesson.full_clean()

        self.assertIn('unit', context.exception.message_dict)
        self.assertEqual(context.exception.message_dict['unit'][0].rstrip('.'),
                         'Ensure this value is greater than or equal to 1')


class TermLessonModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create sample lesson, presentation time, professor, and term
        cls.lesson = Lesson.objects.create(name="Test Lesson", unit=1, type=1)
        cls.presentation_time = PresentationTime.objects.create(day=1, start_time=datetime.now().time(), end_time=datetime.now().time())
        cls.professor = Professor.objects.create(name="Test Professor")
        cls.term = Term.objects.create(name="Test Term")

    def test_create_term_lesson(self):
        # Create a new term lesson
        term_lesson = TermLesson.objects.create(
            lesson=self.lesson,
            exam_time=datetime.now(),
            lecturer=self.professor,
            term=self.term
        )

        # Retrieve the term lesson from the database
        saved_term_lesson = TermLesson.objects.get(lesson=self.lesson)

        # Check if the retrieved term lesson matches the created term lesson
        self.assertEqual(saved_term_lesson, term_lesson)

    def test_term_lesson_str_representation(self):
        # Create a term lesson instance
        term_lesson = TermLesson.objects.create(
            lesson=self.lesson,
            exam_time=datetime.now(),
            lecturer=self.professor,
            term=self.term
        )

        # Check if the string representation is correct
        expected_str = f"{self.lesson.name} {self.term.name}"
        self.assertEqual(str(term_lesson), expected_str)

    def test_term_lesson_fields_not_null(self):
        # Create a term lesson with null fields
        term_lesson = TermLesson()

        # Try to save the term lesson
        with self.assertRaises(Exception) as context:
            term_lesson.save()

        # Check if null constraint is enforced for required fields
        self.assertIn("null value in column", str(context.exception))

    def test_term_lesson_capacity_default_value(self):
        # Create a term lesson with default capacity
        term_lesson = TermLesson.objects.create(
            lesson=self.lesson,
            exam_time=datetime.now(),
            lecturer=self.professor,
            term=self.term
        )

        # Check if the capacity is set to the default value
        self.assertEqual(term_lesson.capacity, 25)



class RegisteredLessonModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create sample term lesson and student
        cls.term_lesson = TermLesson.objects.create(name="Test Lesson", exam_time=datetime.now(), lecturer=None, term=None)
        cls.student = Student.objects.create(name="Test Student")

    def test_create_registered_lesson(self):
        # Create a new registered lesson
        registered_lesson = RegisteredLesson.objects.create(
            lesson=self.term_lesson,
            student=self.student,
            status=1  # Registered status
        )

        # Retrieve the registered lesson from the database
        saved_registered_lesson = RegisteredLesson.objects.get(lesson=self.term_lesson)

        # Check if the retrieved registered lesson matches the created registered lesson
        self.assertEqual(saved_registered_lesson, registered_lesson)

    def test_registered_lesson_str_representation(self):
        # Create a registered lesson instance
        registered_lesson = RegisteredLesson.objects.create(
            lesson=self.term_lesson,
            student=self.student,
            status=1  # Registered status
        )

        # Check if the string representation is correct
        expected_str = f"{self.term_lesson.name}"
        self.assertEqual(str(registered_lesson), expected_str)

    def test_registered_lesson_fields_not_null(self):
        # Create a registered lesson with null fields
        registered_lesson = RegisteredLesson()

        # Try to save the registered lesson
        with self.assertRaises(Exception) as context:
            registered_lesson.save()

        # Check if null constraint is enforced for required fields
        self.assertIn("null value in column", str(context.exception))

    def test_registered_lesson_grade_validators(self):
        # Create a registered lesson with invalid grade
        with self.assertRaises(Exception) as context:
            registered_lesson = RegisteredLesson.objects.create(
                lesson=self.term_lesson,
                student=self.student,
                status=1,  # Registered status
                grade=25  # Invalid grade value
            )

        # Check if MinValueValidator and MaxValueValidator are enforced
        self.assertIn("Ensure this value is less than or equal to 20", str(context.exception))
        self.assertIn("Ensure this value is greater than or equal to 0", str(context.exception))
