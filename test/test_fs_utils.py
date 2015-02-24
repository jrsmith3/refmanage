# -*- coding: utf-8 -*-
import unittest
import pathlib2 as pathlib
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

    def test_import_bib_files(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict
        """
        path = pathlib.Path("test/controls/empty.bib")
        self.assertIsInstance(fs_utils.import_bib_files(path), dict)


class MethodsReturnValues(unittest.TestCase):
    """
    Tests values of methods against known values
    """
    pass
