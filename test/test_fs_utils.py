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

    def test_construct_bib_dict_valid_bibtex(self):
        """
        refmanage.fs_utils.construct_bib_dict should return a dict when called with argument pointing to a file containing valid BibTeX
        """
        self.assertIsInstance(fs_utils.construct_bib_dict(self.empty), dict)

    def test_construct_bib_dict_invalid_bibtex(self):
        """
        refmanage.fs_utils.construct_bib_dict should return a dict when called with argument pointing to a file containing invalid BibTeX
        """
        self.assertIsInstance(fs_utils.construct_bib_dict(self.invalid), dict)

    def test_parse_bib_file_valid_bibtex(self):
        """
        refmanage.fs_utils.parse_bib_file should return a `pybtex.database.BibliographyData` if given a path that points to valid BibTeX
        """
        self.assertIsInstance(fs_utils.parse_bib_file(self.empty), BibliographyData)

    def test_parse_bib_file_invalid_bibtex(self):
        """
        refmanage.fs_utils.parse_bib_file should return a `pybtex.exceptions.PybtexError` if given a path that points to invalid BibTeX
        """
        self.assertIsInstance(fs_utils.parse_bib_file(self.invalid), PybtexError)

    def test_parse_bib_file_one_valid_one_invalid(self):
        """
        refmanage.fs_utils.parse_bib_file should return a `pybtex.exceptions.PybtexError` if given a path that points to a file containing both valid and invalid BibTeX
        """
        self.assertIsInstance(fs_utils.parse_bib_file(self.one_valid_one_invalid), PybtexError)

    def test_gen_terse_msg(self):
        """
        refmanage.fs_utils.gen_terse_msg should return a str
        """
        self.assertIsInstance(fs_utils.gen_terse_msg(self.empty), str)

    def test_gen_verbose_msg(self):
        """
        refmanage.fs_utils.gen_verbose_msg should return a str
        """
        bib = fs_utils.parse_bib_file(self.empty)
        self.assertIsInstance(fs_utils.gen_verbose_msg(bib), str)

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
        self.assertIsInstance(fs_utils.gen_stdout_test_msg(bibfile_data), str)

    def test_gen_bib_dict_test_msg(self):
        """
        refmanage.fs_utils.gen_bib_dict_test_msg should return a str
        """
        bib_dict = fs_utils.construct_bib_dict(self.empty)
        self.assertIsInstance(fs_utils.gen_bib_dict_test_msg(bib_dict), str)


class MethodsReturnValues(Base):
    """
    Tests values of methods against known values
    """
    def test_construct_bibfile_data(self):
        """
        """
        pass

    def test_construct_bib_dict_structure(self):
        """
        refmanage.fs_utils.construct_bib_dict should return a dict with the following keys: ["path", "bib", "terse_msg", "verbose_msg"]
        """
        keys = ["path", "bib", "terse_msg", "verbose_msg"]

        bib_dict = fs_utils.construct_bib_dict(self.empty)
        [self.assertIn(key, keys) for key in bib_dict.keys()]

    def test_parse_bib_file_one_entry(self):
        """
        refmanage.fs_utils.parse_bib_file should return a `pybtex.database.BibliographyData` with one entry when a `Path` pointing at such a BibTeX file is passed to it
        """
        bib = fs_utils.parse_bib_file(self.one)
        self.assertEqual(len(bib.entries), 1)

    def test_parse_bib_file_two_entries(self):
        """
        refmanage.fs_utils.parse_bib_file should return a `pybtex.database.BibliographyData` with two entries when a `Path` pointing at such a BibTeX file is passed to it
        """
        bib = fs_utils.parse_bib_file(self.two)
        self.assertEqual(len(bib.entries), 2)

    def test_gen_verbose_msg_valid_bibtex(self):
        """
        refmanage.fs_utils.gen_verbose_msg should return a str of zero length for an argument pointing to valid BibTeX.
        """
        bib = fs_utils.parse_bib_file(self.empty)
        self.assertEqual(len(fs_utils.gen_verbose_msg(bib)), 0)

    def test_gen_verbose_msg_invalid_bibtex(self):
        """
        refmanage.fs_utils.gen_verbose_msg should return a str of >0 length for an argument pointing to invalid BibTeX.
        """
        bib = fs_utils.parse_bib_file(self.invalid)
        self.assertGreater(len(fs_utils.gen_verbose_msg(bib)), 0)
