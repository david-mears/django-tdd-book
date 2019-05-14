from django.test import TestCase

# Create your tests here.

class TestTheTester(TestCase):

    def test_testing_itself(self):
        self.assertEqual(1, 2)