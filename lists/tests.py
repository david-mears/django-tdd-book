import time

from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item, List

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/only-list/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_list_items(self):
        my_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=my_list)
        Item.objects.create(text='itemey 2', list=my_list)

        response = self.client.get('/lists/only-list/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

class NewListTest(TestCase):

    def test_POST_request_data_can_be_saved(self):
        response = self.client.post('/lists/new', data={'item_text': 'Test to-do'})

        self.assertEqual(Item.objects.count(), 1)  
        new_item = Item.objects.first()  
        self.assertEqual(new_item.text, 'Test to-do')  
    
    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertRedirects(response, '/lists/only-list/')

class ItemAndListModelsTest(TestCase):

    def test_saving_and_retrieving_items(self):
        my_list = List()
        my_list.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = my_list
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = my_list
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, my_list)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, my_list)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, my_list)

