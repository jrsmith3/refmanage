# -*- coding: utf-8 -*-
import unittest
import pathlib2 as pathlib
from refmanage import fs_utils
from pybtex.database import BibliographyData
from pybtex.exceptions import PybtexError


class Instantiation(unittest.TestCase):
    """
    Test all aspects of instantiating an object

    Includes input of wrong type, input outside of a bound, etc.
    """
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

    def test_gen_verbose_msg_i44(self):
        """
        Test bug from issue #44
        """
        p = pathlib.Path("test/controls/10.1371__journal.pone.0115069.bib")
        bib = fs_utils.parse_bib_file(p)
        target = u'Invalid name format: Knauff, , Markus AND Nejasmic, , Jelica'
        self.assertEqual(target, fs_utils.gen_verbose_msg(bib))
