# -*- coding: utf-8 -*-
import unittest
import pathlib2 as pathlib
from refmanage import fs_utils
from pybtex.database import BibliographyData
from pybtex.exceptions import PybtexError


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

    def test_construct_bib_dict_valid_bibtex(self):
        """
        refmanage.fs_utils.construct_bib_dict should return a dict when called with argument pointing to a file containing valid BibTeX
        """
        path = pathlib.Path("test/controls/empty.bib")
        bib_dict = fs_utils.construct_bib_dict(path)
        self.assertIsInstance(bib_dict, dict)

    def test_construct_bib_dict_invalid_bibtex(self):
        """
        refmanage.fs_utils.construct_bib_dict should return a dict when called with argument pointing to a file containing invalid BibTeX
        """
        path = pathlib.Path("test/controls/invalid.bib")
        bib_dict = fs_utils.construct_bib_dict(path)
        self.assertIsInstance(bib_dict, dict)

    def test_parse_bib_file_valid_bibtex(self):
        """
        refmanage.fs_utils.parse_bib_file should return a `pybtex.database.BibliographyData` if given a path that points to valid BibTeX
        """
        path = pathlib.Path("test/controls/empty.bib")
        bib = fs_utils.parse_bib_file(path)
        self.assertIsInstance(bib, BibliographyData)

    def test_parse_bib_file_invalid_bibtex(self):
        """
        refmanage.fs_utils.parse_bib_file should return a `pybtex.exceptions.PybtexError` if given a path that points to invalid BibTeX
        """
        path = pathlib.Path("test/controls/invalid.bib")
        bib = fs_utils.parse_bib_file(path)
        self.assertIsInstance(bib, PybtexError)

    def test_parse_bib_file_one_valid_one_invalid(self):
        """
        refmanage.fs_utils.parse_bib_file should return a `pybtex.exceptions.PybtexError` if given a path that points to a file containing both valid and invalid BibTeX
        """
        path = pathlib.Path("test/controls/one_valid_one_invalid.bib")
        bib = fs_utils.parse_bib_file(path)
        self.assertIsInstance(bib, PybtexError)

    def test_generate_terse_output_message(self):
        """
        refmanage.fs_utils.generate_terse_output_message should return a str
        """
        path = pathlib.Path("test/controls/empty.bib")
        terse_msg = fs_utils.generate_terse_output_message(path)
        self.assertIsInstance(terse_msg, str)

    def test_generate_verbose_err_output_message(self):
        """
        refmanage.fs_utils.generate_verbose_err_output_message should return a str
        """
        path = pathlib.Path("test/controls/empty.bib")
        bib = fs_utils.parse_bib_file(path)
        verbose_msg = fs_utils.generate_verbose_err_output_message(bib)
        self.assertIsInstance(verbose_msg, str)

    def test_import_bib_files(self):
        """
        refmanage.fs_utils.import_bib_files should return a list
        """
        path = pathlib.Path("test/controls/empty.bib")
        self.assertIsInstance(fs_utils.import_bib_files(path), list)

    def test_bib_sublist(self):
        """
        refmanage.fs_utils.bib_subdict should return a list
        """
        pass


class MethodsReturnValues(unittest.TestCase):
    """
    Tests values of methods against known values
    """
    def test_import_bib_files(self):
        """
        """
        pass

    def test_construct_bib_dict_structure(self):
        """
        refmanage.fs_utils.construct_bib_dict should return a dict with the following keys: ["path", "bib", "terse_msg", "verbose_msg"]
        """
        keys = ["path", "bib", "terse_msg", "verbose_msg"]
        path = pathlib.Path("test/controls/empty.bib")
        bib_dict = fs_utils.construct_bib_dict(path)
        [self.assertIn(key, keys) for key in bib_dict.keys()]

    def test_parse_bib_file_one_entry(self):
        """
        refmanage.fs_utils.parse_bib_file should return a `pybtex.database.BibliographyData` with one entry when a `Path` pointing at such a BibTeX file is passed to it
        """
        path = pathlib.Path("test/controls/one.bib")
        bib = fs_utils.parse_bib_file(path)
        self.assertEqual(len(bib.entries), 1)

    def test_parse_bib_file_two_entries(self):
        """
        refmanage.fs_utils.parse_bib_file should return a `pybtex.database.BibliographyData` with two entries when a `Path` pointing at such a BibTeX file is passed to it
        """
        path = pathlib.Path("test/controls/two.bib")
        bib = fs_utils.parse_bib_file(path)
        self.assertEqual(len(bib.entries), 2)
