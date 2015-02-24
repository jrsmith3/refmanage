# -*- coding: utf-8 -*-
import unittest
import pathlib2 as pathlib
from refmanage import fs_utils
import pybtex


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

    def test_import_bib_files_key(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict with key `pathlib.Path`
        """
        path = pathlib.Path("test/controls/empty.bib")
        bibs = fs_utils.import_bib_files(path)
        for key in bibs.keys():
            self.assertIsInstance(key, pathlib.Path)


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
        refmanage.fs_utils.import_bib_files should return a dict with a `None` value if the method argument points to a file containing invalid BibTeX
        """
        path = pathlib.Path("test/controls/invalid.bib")
        bibs = fs_utils.import_bib_files(path)
        self.assertIsNone(bibs[path], None)

    def test_import_bib_files_one_valid_one_invalid_entry_type(self):
        """
        refmanage.fs_utils.import_bib_files should return a dict with a `pybtex.database.bibtex` value if the method argument points to a file containing one valid and one invalid BibTeX entry
        """
        path = pathlib.Path("test/controls/one_valid_one_invalid.bib")
        bibs = fs_utils.import_bib_files(path)
        self.assertIsNone(bibs[path], None)


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
