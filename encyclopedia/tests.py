# Create your tests here.
from random import choice, seed
import string

from django.test import TestCase
from encyclopedia.util import get_entry
from encyclopedia.util import list_entries
from encyclopedia.util import save_entry
from encyclopedia.util import delete_entry

def random_string(len, s = None) -> str:
    """
    returns pseudorandom l/ucase alphanumerical string of specified length
    """
    seed(s)
    return ''.join(choice(string.ascii_letters + string.digits) for x in range(len))

class InternalTest(TestCase):
    """
    includes tests for tests.py
    """
    def test_random_string_returns_string(self):
        """
        random_string(len) returns string
        """
        self.assertIsInstance(random_string(10), str)

    def test_random_string_returns_random(self):
        """
        random_string(len) returns random string when seed 's' is unspecified
        """
        self.assertNotEqual(random_string(10), random_string(10))
        

class UtilTest(TestCase):

    def test_get_entry_no_title(self):
        """
        get_entry(title) returns None if title with given name doesn't exist
        """
        self.assertIsNone(get_entry(''))

    def test_get_entry_title_exists(self):
        """ 
        get_entry(title) returns file content as a string
        """
        self.assertIsInstance(get_entry('HTML'), str)
    
    def test_list_entries_is_list(self):
        """
        list_entries() returns a list
        """
        self.assertIsInstance(list_entries(), list)

    def test_save_entry_create_file(self):
        """
        save_entry creates new file with given content
        """ 
        title = 'test_' + random_string(10)
        save_entry(title, '**TEST**')
        self.assertEqual(get_entry(title), '**TEST**')
        delete_entry(title)

    def test_delete_entry(self):
        """
        delete_entry(title) deletes entry file given title
        """
        title = 'test_' + random_string(10)
        save_entry(title, '**TEST**')
        delete_entry(title)
        self.assertIsNone(get_entry(title))
