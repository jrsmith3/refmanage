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
        self.old_stderr = sys.stderr

        self.stdout = StringIO.StringIO()
        self.stderr = StringIO.StringIO()

        sys.stdout = self.stdout
        sys.stderr = self.stderr

        self.parser = refmanage.define_parser()

    def tearDown(self):
        """
        Reset STDOUT
        """
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr


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

        self.assertEqual(refmanage.__version__, self.stdout.getvalue())

class TestFunctionality(Base):
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
        args = self.parser.parse_args(["-t", "test/controls/*.bib"])
        refmanage.cli_args_dispatcher(args)
        output_text = "test/controls/10.1371__journal.pone.0115069.bib\n test/controls/invalid.bib\n test/controls/one_valid_one_invalid.bib\n"

        self.assertEqual(output_text, self.stdout.getvalue())

    def test_unparseable(self):

        """
        `ref test -u *.bib` should print list of unparseable files
        """
        args = self.parser.parse_args(["-t", "-u", "test/controls/*.bib"])
        refmanage.cli_args_dispatcher(args)
        output_text = "test/controls/10.1371__journal.pone.0115069.bib\n test/controls/invalid.bib\n test/controls/one_valid_one_invalid.bib\n"

        self.assertEqual(output_text, self.stdout.getvalue())

    def test_unparseable_verbose(self):
        """
        `ref test -uv *.bib` should print list of unparseable files with information about corresponding parsing message
        """
        self.fail()

    def test_parseable(self):
        """
        `ref test -p *.bib` should print list of parseable files
        """
        args = self.parser.parse_args(["-t", "-p", "test/controls/*.bib"])
        refmanage.cli_args_dispatcher(args)
        output_text = "test/controls/empty.bib\n test/controls/one.bib\n test/controls/two.bib\n"

        self.assertEqual(output_text, self.stdout.getvalue())

    def test_parseable_verbose(self):
        """
        `ref test -pv *.bib` should print list of parseable files and nothing more
        """
        args = self.parser.parse_args(["-t", "-p", "-v", "test/controls/*.bib"])
        refmanage.cli_args_dispatcher(args)
        output_text = "test/controls/empty.bib\n test/controls/one.bib\n test/controls/two.bib\n"

        self.assertEqual(output_text, self.stdout.getvalue())

    def test_unparseable_with_parseable_file(self):
        """
        `ref test -u parseable.bib` should return nothing
        """
        args = self.parser.parse_args(["-t", "-u", "test/controls/one.bib"])
        refmanage.cli_args_dispatcher(args)
        output_text = ""

        self.assertEqual(output_text, self.stdout.getvalue())

    def test_parseable_with_unparseable_file(self):
        """
        `ref test -p unparseable.bib` should return nothing
        """
        args = self.parser.parse_args(["-t", "-p", "test/controls/invalid.bib"])
        refmanage.cli_args_dispatcher(args)
        output_text = ""

        self.assertEqual(output_text, self.stdout.getvalue())

    def test_parseable_unparseable(self):
        """
        `ref test -up *.bib` should exit with an error
        """
        with self.assertRaises(SystemExit):
            args = self.parser.parse_args(["-t", "-p", "-u", "test/controls/*.bib"])
