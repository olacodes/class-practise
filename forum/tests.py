# from django.test import TestCase

# Create your tests here.

from unittest import TestCase


class SampleTest(TestCase):
    def test_add(self):
        self.assertEqual(5 + 1, 6)
