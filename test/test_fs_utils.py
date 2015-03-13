# -*- coding: utf-8 -*-
import unittest
import pathlib2 as pathlib
from refmanage import fs_utils
from pybtex.database import BibliographyData
from pybtex.exceptions import PybtexError


# Base classes
# ============
class Base(unittest.TestCase):
    """
    Base class for tests

    This class is intended to be subclassed so that the same `setUp` method does not have to be rewritten for each class containing tests.
    """
    def setUp(self):
        """
        Create `Path`s to various control data
        """
        self.empty = pathlib.Path("test/controls/empty.bib")
        self.one = pathlib.Path("test/controls/one.bib")
        self.two = pathlib.Path("test/controls/two.bib")
        self.invalid = pathlib.Path("test/controls/invalid.bib")
        self.one_valid_one_invalid = pathlib.Path("test/controls/one_valid_one_invalid.bib")

class MethodsInput(unittest.TestCase):
    """
    Tests methods which take input parameters

    Tests include: passing invalid input, etc.
    """
    pass


class MethodsReturnType(Base):
    """
    Tests methods' output types
    """
    def test_handle_files_args(self):
        """
        refmanage.fs_utils.handle_files_args should return a list
        """
        self.assertIsInstance(fs_utils.handle_files_args(""), list)

    def test_construct_bibfile_data(self):
        """
        refmanage.fs_utils.construct_bibfile_data should return a list
        """
        self.assertIsInstance(fs_utils.construct_bibfile_data(self.empty), list)

    def test_bib_sublist(self):
        """
        refmanage.fs_utils.bib_sublist should return a list
        """
        bibfile_data = fs_utils.construct_bibfile_data(self.empty, self.invalid)
        self.assertIsInstance(fs_utils.bib_sublist(bibfile_data, BibliographyData), list)

    def test_gen_stdout_test_msg(self):
        """
        refmanage.fs_utils.gen_stdout_test_msg should return a str
        """
        bibfile_data = fs_utils.construct_bibfile_data(self.empty)
        self.assertIsInstance(fs_utils.gen_stdout_test_msg(bibfile_data), unicode)


class MethodsReturnValues(Base):
    """
    Tests values of methods against known values
    """
    def test_construct_bibfile_data(self):
        """
        """
        pass
