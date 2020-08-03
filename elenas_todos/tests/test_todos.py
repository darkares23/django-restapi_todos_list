"""
Contains the Todos tests class
"""


from django.test import TestCase
from todos.models import Todo
import inspect
import pep8
import unittest


class TodoModelTestCase(TestCase):
    """Tests to check the documentation and style of Todo class"""

    def test_name_attr(self):
        """Test Todo has attribute"""
        todo = Todo()
        self.assertTrue(hasattr(todo, 'id'))
        self.assertTrue(hasattr(todo, 'name'))
        self.assertTrue(hasattr(todo, 'description'))
        self.assertTrue(hasattr(todo, 'state'))
        self.assertTrue(hasattr(todo, 'created_at'))

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.todo_func = inspect.getmembers(Todo, inspect.isfunction)

    def testTodoDocs(self):
        """Test that todos/models.py conforms pep8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8.Checker(filename='todos/models.py')
        self.assertEqual(result, 0, "Found code style errors (and warnings).")