# -*- coding: utf-8 -*-
import unittest
import pathlib2 as pathlib
import refmanage

class NoSpecifiedFunctionality(unittest.TestCase):
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
        self.fail()

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
