import datetime

from django.test import TestCase
from django.utils import timezone

# Create your tests here.

class QuestionModelTests(TestCase):

    def test_was_publish_recently_with_future_questions(self):
        """was_published_recently return False for question whose pub_date is in the future"""
        time = timezone.now()+datetime.timedelta(days=30)
