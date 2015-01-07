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
    def test_merge_single_arg(self):
        """
        merge can take a single argument
        """
        pass

    def test_merge_two_args(self):
        """
        merge can take two arguments
        """
        pass

    def test_merge_three_args(self):
        """
        merge can take multiple arguments

        This method tests three input args and assumes an arbitrary number of input args will work.
        """
        pass

    def test_merge_duplicate_entry_key(self):
        """
        What happens when each database contains an entry with the same key?
        """
        pass
