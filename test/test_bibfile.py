# -*- coding: utf-8 -*-
import unittest
import pathlib2 as pathlib
from refmanage import BibFile
from refmanage.exceptions import UnparseableBibtexError
from pybtex.database import BibliographyData


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
        refmanage.BibFile should raise TypeError if instantiated with no input
        """
        self.assertRaises(TypeError, BibFile)

    def test_invalid_bibtex(self):
        """
        refmanage.BibFile should raise UnparseableBibtexError if instantiated with a path to an unparseable file.
        """
        self.assertRaises(UnparseableBibtexError, BibFile, self.invalid)

    def test_one_valid_one_invalid_bib_type(self):
        """
        refmanage.BibFile should raise UnparseableBibtexError if instantiated with a path to a file containing both valid and invalid BibTeX
        """
        self.assertRaises(UnparseableBibtexError, BibFile, self.one_valid_one_invalid)


class Attributes(Base):
    """
    Test attributes of BibFile

    These tests include type checks, setting immutable attributes, etc.
    """
    # Type checking
    # =============
    def test_path_type(self):
        """
        refmanage.BibFile.path should be of type `pathlib.Path`
        """
        b = BibFile(self.empty)
        self.assertIsInstance(b.path, pathlib.Path)

    def test_src_txt_type(self):
        """
        refmanage.BibFile.src_txt should be of type unicode
        """
        b = BibFile(self.empty)
        self.assertIsInstance(b.src_txt, unicode)

    def test_bib_type(self):
        """
        refmanage.BibFile.bib should be of type `pybtex.database.BibliographyData`
        """
        b = BibFile(self.two)
        self.assertIsInstance(b.bib, BibliographyData)

    # Immutability
    # ============
    # The `path`, `bib`, and `src_txt` should be immutable once the `BibFile` object has been created. In other words, these attributes should not be changeable after the fact.
    def test_path_immutability(self):
        """
        Attempting to set `refmanage.BibFile.path` should raise AttributeError
        """
        b = BibFile(self.one)
        try:
            b.path = self.empty
        except AttributeError:
            # Attempting to set `path` attribute raises an error; test passed!
            pass
        else:
            self.fail("BibFile.path can be set after instantiation")

    def test_bib_immutability(self):
        """
        Attempting to set `refmanage.BibFile.bib` should raise AttributeError
        """
        b = BibFile(self.one)
        bib = b.bib
        try:
            b.bib = bib
        except AttributeError:
            # Attempting to set `path` attribute raises an error; test passed!
            pass
        else:
            self.fail("BibFile.bib can be set after instantiation")

    def test_src_txt_immutability(self):
        """
        Attempting to set `refmanage.BibFile.src_txt` should raise AttributeError
        """
        b = BibFile(self.one)
        try:
            b.src_txt = "legitimate text string"
        except AttributeError:
            # Attempting to set `path` attribute raises an error; test passed!
            pass
        else:
            self.fail("BibFile.src_txt can be set after instantiation")

    # Value checking
    # ==============
    def test_empty_file_bib_length(self):
        """
        refmanage.BibFile.bib should contain zero entries if instantiated with an empty file
        """
        b = BibFile(self.empty)
        self.assertEqual(len(b.bib.entries), 0)

    def test_one_entry_bibtex_file_bib_length(self):
        """
        refmanage.BibFile.bib should contain one entry if instantiated with a file containing valid BibTeX with a single entry
        """
        b = BibFile(self.one)
        self.assertEqual(len(b.bib.entries), 1)

    def test_two_entries_bibtex_file_bib_length(self):
        """
        refmanage.BibFile.bib should contain two entries if instantiated with a file containing valid BibTeX with two entries
        """
        b = BibFile(self.two)
        self.assertEqual(len(b.bib.entries), 2)


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
    def test_terse_msg(self):
        """
        refmanage.BibFile.terse_msg() should return a unicode
        """
        b = BibFile(self.empty)
        self.assertIsInstance(b.terse_msg(), unicode)

    def test_verbose_msg(self):
        """
        refmanage.BibFile.verbose_msg() should return a unicode
        """
        b = BibFile(self.empty)
        self.assertIsInstance(b.verbose_msg(), unicode)

    def test_test_msg_verbose_false(self):
        """
        refmanage.BibFile.test_msg(verbose=False) should return a unicode
        """
        b = BibFile(self.empty)
        self.assertIsInstance(b.test_msg(False), unicode)

    def test_test_msg_verbose_true(self):
        """
        refmanage.BibFile.test_msg(verbose=True) should return a unicode
        """
        b = BibFile(self.empty)
        self.assertIsInstance(b.test_msg(True), unicode)


class MethodsReturnValues(Base):
    """
    Tests values of methods against known values
    """
    def test_verbose_msg_valid_bibtex(self):
        """
        refmanage.BibFile.verbose_msg() should return a str of zero length for an argument pointing to valid BibTeX.
        """
        b = BibFile(self.two)
        self.assertEqual(len(b.verbose_msg()), 0)
