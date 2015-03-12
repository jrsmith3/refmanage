# -*- coding: utf-8 -*-
import unittest
import pathlib2 as pathlib
from refmanage import BibFile
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


class Instantiation(Base):
    """
    Test all aspects of instantiating an object

    Includes input of wrong type, input outside of a bound, etc.
    """
    def test_no_input(self):
        """
        refmanage.BibFile should raise (SOME KIND OF ERROR) if instantiated with no input
        """
        pass


class Attributes(Base):
    """
    Test attributes of BibFile

    These tests include type checks, setting immutable attributes, etc.
    """
    # Type checking
    # =============
    def test_valid_bibtex_bib_type(self):
        """
        refmanage.BibFile.bib should be of type `pybtex.database.BibliographyData` if instantiated with an empty file
        """
        b = BibFile(self.two)
        self.assertIsInstance(b.bib, BibliographyData)

    def test_invalid_bibtex_bib_type(self):
        """
        refmanage.BibFile.bib should be of type `pybtex.exceptions.PybtexError` if instantiated with a file containing invalid BibTeX
        """
        b = BibFile(self.invalid)
        self.assertIsInstance(b.bib, PybtexError)

    def test_one_valid_one_invalid_bib_type(self):
        """
        refmanage.BibFile.bib should be of type `pybtex.exceptions.PybtexError` if instantiated with a file containing one valid and one invalid BibTeX entry
        """
        b = BibFile(self.one_valid_one_invalid)
        self.assertIsInstance(b.bib, PybtexError)


    def test_empty_file_bib_type(self):
        """
        refmanage.BibFile.bib should be of type `pybtex.database.BibliographyData` if instantiated with an empty file
        """
        b = BibFile(self.empty)
        self.assertIsInstance(b.bib, BibliographyData)

    def test_valid_bibtex_bib_type(self):
        """
        refmanage.BibFile.bib should be of type `pybtex.database.BibliographyData` if instantiated with a file containing valid BibTeX
        """
        b = BibFile(self.one)
        self.assertIsInstance(b.bib, BibliographyData)

    def test_two_entries_bib_type(self):
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
