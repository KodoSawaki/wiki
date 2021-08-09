import re
from wiki.settings import SECRET_KEY
from django.test import TestCase
from django.urls import reverse

from encyclopedia.util import list_entries

class IndexViewTests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('encyclopedia:index'))
    def test_index_default_response(self):
       '''Default index response should be 200''' 
       self.assertEqual(self.response.status_code, 200)
    def test_index_entries_list(self):   
        '''Entries list displayed on the index page'''
        self.assertListEqual(self.response.context['entries'],list_entries())