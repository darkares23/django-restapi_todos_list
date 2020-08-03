from django.test import TestCase

"""
Contains the Todos tests class
"""


from django.test import TestCase
from .models import Todo
import inspect
import pep8
import unittest


class TodoModelTestCase(TestCase):
    """Tests to check the documentation and style of Todo class"""

    def test_title_attr(self):
        """Test Todo has attribute title"""
        todo = Todo()
        self.assertTrue(hasattr(todo, 'title'))

    def test_description_attr(self):
        """Test Todo has attribute description"""
        todo = Todo()
        self.assertTrue(hasattr(todo, 'description'))

    def test_done_attr(self):
        """Test Todo has attribute done"""
        todo = Todo()
        self.assertTrue(hasattr(todo, 'done'))

    def test_created_at_attr(self):
        """Test Todo has attribute created_at"""
        todo = Todo()
        self.assertTrue(hasattr(todo, 'created_at'))
