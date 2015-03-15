# -*- coding: utf-8 -*-
import unittest
import pathlib2 as pathlib
from refmanage import NonbibFile
from refmanage.exceptions import UnparseableBibtexError, ParseableBibtexError
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
        refmanage.NonbibFile should raise TypeError if instantiated with no input
        """
        with self.assertRaises(TypeError):
            NonbibFile()

    def test_valid_bibtex(self):
        """
        refmanage.NonbibFile should raise ParseableBibtexError if instantiated with a path to a parseable file.
        """
        with self.assertRaises(ParseableBibtexError):
            NonbibFile(self.two)

    def test_one_valid_one_invalid_bib_type(self):
        """
        refmanage.NonbibFile can successfully be instantiated with files containing both valid and invalid BibTeX
        """
        try:
            b = NonbibFile(self.one_valid_one_invalid)
        except UnparseableBibtexError:
            self.fail("Instantiation failed though input was valid")


class Attributes(Base):
    """
    Test attributes of NonbibFile

    These tests include type checks, setting immutable attributes, etc.
    """
    # Type checking
    # =============
    def test_path_type(self):
        """
        refmanage.NonbibFile.path should be of type `pathlib.Path`
        """
        b = NonbibFile(self.invalid)
        self.assertIsInstance(b.path, pathlib.Path)

    def test_src_txt_type(self):
        """
        refmanage.NonbibFile.src_txt should be of type unicode
        """
        b = NonbibFile(self.invalid)
        self.assertIsInstance(b.src_txt, unicode)

    def test_bib_type(self):
        """
        refmanage.NonbibFile.bib should be of type `pybtex.exceptions.PybtexError`
        """
        b = NonbibFile(self.invalid)
        self.assertIsInstance(b.bib, PybtexError)

    # Immutability
    # ============
    # The `path`, `bib`, and `src_txt` should be immutable once the `NonbibFile` object has been created. In other words, these attributes should not be changeable after the fact.
    def test_path_immutability(self):
        """
        Attempting to set `refmanage.NonbibFile.path` should raise AttributeError
        """
        b = NonbibFile(self.invalid)
        try:
            b.path = self.empty
        except AttributeError:
            # Attempting to set `path` attribute raises an error; test passed!
            pass
        else:
            self.fail("NonbibFile.path can be set after instantiation")

    def test_bib_immutability(self):
        """
        Attempting to set `refmanage.NonbibFile.bib` should raise AttributeError
        """
        b = NonbibFile(self.invalid)
        bib = b.bib
        try:
            b.bib = bib
        except AttributeError:
            # Attempting to set `path` attribute raises an error; test passed!
            pass
        else:
            self.fail("NonbibFile.bib can be set after instantiation")

    def test_src_txt_immutability(self):
        """
        Attempting to set `refmanage.NonbibFile.src_txt` should raise AttributeError
        """
        b = NonbibFile(self.invalid)
        try:
            b.src_txt = "legitimate text string"
        except AttributeError:
            # Attempting to set `path` attribute raises an error; test passed!
            pass
        else:
            self.fail("NonbibFile.src_txt can be set after instantiation")


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
        refmanage.NonbibFile.terse_msg() should return a unicode
        """
        b = NonbibFile(self.invalid)
        self.assertIsInstance(b.terse_msg(), unicode)

    def test_verbose_msg(self):
        """
        refmanage.NonbibFile.verbose_msg() should return a unicode
        """
        b = NonbibFile(self.invalid)
        self.assertIsInstance(b.verbose_msg(), unicode)

    def test_test_msg_verbose_false(self):
        """
        refmanage.NonbibFile.test_msg(verbose=False) should return unicode
        """
        b = NonbibFile(self.invalid)
        self.assertIsInstance(b.test_msg(False), unicode)

    def test_test_msg_verbose_true(self):
        """
        refmanage.NonbibFile.test_msg(verbose=True) should return unicode
        """
        b = NonbibFile(self.invalid)
        self.assertIsInstance(b.test_msg(True), unicode)


class MethodsReturnValues(Base):
    """
    Tests values of methods against known values
    """
    def test_verbose_msg_invalid_bibtex(self):
        """
        refmanage.NonbibFile.verbose_msg() should return a str of >0 length for an argument pointing to invalid BibTeX.
        """
        b = NonbibFile(self.invalid)
        self.assertGreater(len(b.verbose_msg()), 0)

    def test_verbose_msg_i44(self):
        """
        Test bug from issue #44
        """
        p = pathlib.Path("test/controls/10.1371__journal.pone.0115069.bib")
        b = NonbibFile(p)
        target = u'Invalid name format: Knauff, , Markus AND Nejasmic, , Jelica'
        self.assertEqual(target, b.verbose_msg())
