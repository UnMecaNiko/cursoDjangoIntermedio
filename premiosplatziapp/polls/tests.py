import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here


class QuestionModelTests(TestCase):

    def test_was_publish_recently_with_future_questions(self):
        """was_published_recently returns False for question whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(
            question_text="¿Quien es el mejor Couse Director de platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_publish_recently_with_present_questions(self):
        """was_published_recently returns Ture for a quiestion whose pub_date
            is in the present
        """
        time = timezone.now()
        present_question = Question(
            question_text="¿Quien es el mejor Couse Director de platzi?", pub_date=time)
        self.assertIs(present_question.was_published_recently(), True)
