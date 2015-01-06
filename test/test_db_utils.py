# -*- coding: utf-8 -*-
"""
Test `db_utils` submodule
"""
import unittest
from refmanage import db_utils

class MethodsInput(unittest.TestCase):
    """
    Tests behavior of methods which take input arguments
    """
    def test_cat_db_single_arg(self):
        """
        cat_db can take a single argument
        """
        pass

    def test_cat_db_two_args(self):
        """
        cat_db can take two arguments
        """
        pass

    def test_cat_db_three_args(self):
        """
        cat_db can take multiple arguments

        This method tests three input args and assumes an arbitrary number of input args will work.
        """
        pass

    def test_cat_db_duplicate_entry_key(self):
        """
        What happens when each database contains an entry with the same key?
        """
        pass
