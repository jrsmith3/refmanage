# -*- coding: utf-8 -*-
import unittest
import pathlib2 as pathlib
import refmanage
import sys
import StringIO


class Base(unittest.TestCase):
    """
    Base class for tests

    This class is intended to be subclassed so that the same `setUp` method does not have to be rewritten for each class containing tests.
    """
    def setUp(self):
        """
        Define parser and set up StringIO to catch STDOUT
        """
        # Redirect STDOUT to a StringIO object.
        self.old_stdout = sys.stdout
        self.f = StringIO.StringIO()
        sys.stdout = self.f

        self.parser = refmanage.define_parser()

    def tearDown(self):
        """
        Reset STDOUT
        """
        sys.stdout = self.old_stdout


class NoSpecifiedFunctionality(Base):
    """
    Tests when no functionality has been specified on cli
    """
    def test_no_args(self):
        """
        `ref` without arguments should print the help text
        """
        self.fail()

    def test_version(self):
        """
        `ref --version` should return version string
        """
        args = self.parser.parse_args(["--version"])
        refmanage.cli_args_dispatcher(args)

        self.assertEqual(refmanage.__version__, self.f.getvalue())

class TestFunctionality(unittest.TestCase):
    """
    Test "test" functionality
    """
    def test_no_args(self):
        """
        `ref test` without additonal arguments should print the help text
        """
        self.fail()

    def test_default(self):
        """
        `ref test *.bib` without flags should default to --unparseable and print list of unparseable files
        """
        self.fail()

    def test_unparseable(self):

        """
        `ref test -u *.bib` should print list of unparseable files
        """
        self.fail()

    def test_unparseable_verbose(self):
        """
        `ref test -uv *.bib` should print list of unparseable files with information about corresponding parsing message
        """
        self.fail()

    def test_parseable(self):
        """
        `ref test -p *.bib` should print list of parseable files
        """
        self.fail()

    def test_parseable_verbose(self):
        """
        `ref test -pv *.bib` should print list of parseable files and nothing more
        """
        self.fail()

    def test_parseable_unparseable(self):
        """
        `ref test -up *.bib` should exit with an error
        """
        self.fail()
