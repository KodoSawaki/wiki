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

class WikiViewTests(TestCase):
    def test_wiki_entry_exists(self):
        '''Loads entry page from md file'''
        response = self.client.get(reverse('encyclopedia:wiki', args = ['Git']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Git')
    
    def test_wiki_no_entry(self):
        '''In case entry doesn't exist wiki loads notfound page'''
        response = self.client.get('/wiki/iow3jerf2/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Encyclopedia doesn't have an article with this exact name.")