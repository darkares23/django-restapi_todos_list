"""
Contains the Todos tests class

from django.test import TestCase
from api.models import Todo
import inspect
import pep8


class UserModelTestCase(TestCase):

    def test_name_attr(self):
        #Test User has attributes
        todo = User()
        self.assertTrue(hasattr(todo, 'id'))
        self.assertTrue(hasattr(todo, 'name'))
        self.assertTrue(hasattr(todo, 'description'))
        self.assertTrue(hasattr(todo, 'state'))
        self.assertTrue(hasattr(todo, 'created_at'))
"""