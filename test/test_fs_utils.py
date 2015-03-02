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

    def test_import_bib_files(self):
        """
        refmanage.fs_utils.import_bib_files should return a list
        """
        path = pathlib.Path("test/controls/empty.bib")
        self.assertIsInstance(fs_utils.import_bib_files(path), list)

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

    def test_bib_sublist(self):
        """
        refmanage.fs_utils.bib_subdict should return a list
        """
        pass


class MethodsReturnValues(unittest.TestCase):
    """
    Tests values of methods against known values
    """
    # Type check output of import_bib_files
    def test_import_bib_files_one_valid_entry_type(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict with a `pybtex.database.bibtex` value if the method argument points to a file containing valid BibTeX
        """
        path = pathlib.Path("test/controls/one.bib")
        bibs = fs_utils.import_bib_files(path)
        self.assertIsInstance(bibs[path], pybtex.database.BibliographyData)

    def test_import_bib_files_two_valid_entry_type(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict with a `pybtex.database.bibtex` value if the method argument points to a file containing valid BibTeX
        """
        path = pathlib.Path("test/controls/two.bib")
        bibs = fs_utils.import_bib_files(path)
        self.assertIsInstance(bibs[path], pybtex.database.BibliographyData)

    def test_import_bib_files_one_invalid_entry_type(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict with a `pybtex.exceptions.PybtexError` value if the method argument points to a file containing invalid BibTeX
        """
        path = pathlib.Path("test/controls/invalid.bib")
        bibs = fs_utils.import_bib_files(path)
        self.assertIsInstance(bibs[path], pybtex.exceptions.PybtexError)

    def test_import_bib_files_one_valid_one_invalid_entry_type(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict with a `pybtex.exceptions.PybtexError` value if the method argument points to a file containing one valid and one invalid BibTeX entry
        """
        path = pathlib.Path("test/controls/one_valid_one_invalid.bib")
        bibs = fs_utils.import_bib_files(path)
        self.assertIsInstance(bibs[path], pybtex.exceptions.PybtexError)


    # Test number of entries in output of import_bib_files
    def test_import_bib_files_one_valid_entry_number(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict with a `pybtex.database.bibtex` value with the same number of entries as the file.
        """
        path = pathlib.Path("test/controls/one.bib")
        bibs = fs_utils.import_bib_files(path)
        self.assertEqual(len(bibs[path].entries), 1)

    def test_import_bib_files_two_valid_entry_number(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict with a `pybtex.database.bibtex` value if the method argument points to a file containing valid BibTeX
        """
        path = pathlib.Path("test/controls/two.bib")
        bibs = fs_utils.import_bib_files(path)
        self.assertEqual(len(bibs[path].entries), 2)



    def test_construct_bib_dict_path(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict with key "path" of type `pathlib.Path`
        """
        path = pathlib.Path("test/controls/empty.bib")
        bib_dict = fs_utils.construct_bib_dict(path)
        self.assertIsInstance(bib_dict["path"], pathlib.Path)

    def test_construct_bib_dict_bib_valid_bibtex(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict with key "bib" of type `pybtex.database.BibliographyData` if argument points to file containing valid BibTeX
        """
        path = pathlib.Path("test/controls/empty.bib")
        bib_dict = fs_utils.construct_bib_dict(path)
        self.assertIsInstance(bib_dict["bib"], BibliographyData)

    def test_construct_bib_dict_bib_invalid_bibtex(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict with key "bib" of type `pybtex.exceptions.PybtexError` if argument points to file containing invalid BibTeX
        """
        path = pathlib.Path("test/controls/invalid.bib")
        bib_dict = fs_utils.construct_bib_dict(path)
        self.assertIsInstance(bib_dict["bib"], PybtexError)

    def test_construct_bib_dict_terse_msg(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict with key "terse_msg" of type str
        """
        path = pathlib.Path("test/controls/empty.bib")
        bib_dict = fs_utils.construct_bib_dict(path)
        self.assertIsInstance(bib_dict["terse_msg"], str)

    def test_construct_bib_dict_verbose_msg(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict with key "verbose_msg" of type str
        """
        path = pathlib.Path("test/controls/empty.bib")
        bib_dict = fs_utils.construct_bib_dict(path)
        self.assertIsInstance(bib_dict["verbose_msg"], str)
