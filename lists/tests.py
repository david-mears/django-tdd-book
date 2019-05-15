from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_POST_request_data_can_be_saved(self):
        response = self.client.post('/', data={'item_text': 'Test to-do'})
        self.assertIn('Test to-do', response.content.decode())