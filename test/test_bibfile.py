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
    def test_path_type(self):
        """
        refmanage.BibFile.path should be of type `pathlib.Path`
        """
        b = BibFile(self.empty)
        self.assertIsInstance(b.path, pathlib.Path)

    def test_src_txt_type(self):
        """
        refmanage.BibFile.src_txt should be of type str
        """
        b = BibFile(self.empty)
        self.assertIsInstance(b.src_txt, str)

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

    # Immutability
    # ============
    # The `path`, `bib`, and `src_txt` should be immutable once the `BibFile` object has been created. In other words, these attributes should not be changeable after the fact.
    def test_path_immutability(self):
        """
        Attempting to set `refmanage.BibFile.path` should raise (SOME KIND OF ERROR)
        """
        # b = BibFile(self.one)
        # self.assertRaises(xx, b.path)
        self.fail()

    def test_bib_immutability(self):
        """
        Attempting to set `refmanage.BibFile.bib` should raise (SOME KIND OF ERROR)
        """
        # b = BibFile(self.one)
        # self.assertRaises(xx, b.bib)
        self.fail()

    def test_src_txt_immutability(self):
        """
        Attempting to set `refmanage.BibFile.src_txt` should raise (SOME KIND OF ERROR)
        """
        # b = BibFile(self.one)
        # self.assertRaises(xx, b.src_txt)
        self.fail()

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
