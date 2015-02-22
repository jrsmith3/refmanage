# -*- coding: utf-8 -*-
import unittest
from refmanage import fs_utils


class MethodsInput(unittest.TestCase):
    """
    Tests methods which take input parameters

    Tests include: passing invalid input, etc.
    """
    pass


class MethodsReturnType(unittest.TestCase):
    """
    Tests methods' output types
    """
    def test_handle_files_args(self):
        """
        refmanage.fs_utils.handle_files_args should return a list
        """
        self.assertIsInstance(fs_utils.handle_files_args(""), list)


class MethodsReturnValues(unittest.TestCase):
    """
    Tests values of methods against known values
    """
    pass
