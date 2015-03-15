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
        pass

    def test_version(self):
        """
        `ref --version` should return version string
        """
        pass

class TestFunctionality(unittest.TestCase):
    """
    Test "test" functionality
    """
    def test_no_args(self):
        """
        `ref test` without additonal arguments should print the help text
        """
        pass

    def test_default(self):
        """
        `ref test *.bib` without flags should default to --unparseable and print list of unparseable files
        """
        pass

    def test_unparseable(self):

        """
        `ref test -u *.bib` should print list of unparseable files
        """
        pass

    def test_unparseable_verbose(self):
        """
        `ref test -uv *.bib` should print list of unparseable files with information about corresponding parsing message
        """
        pass

    def test_parseable(self):
        """
        `ref test -p *.bib` should print list of parseable files
        """
        pass

    def test_parseable_verbose(self):
        """
        `ref test -pv *.bib` should print list of parseable files and nothing more
        """
        pass

    def test_parseable_unparseable(self):
        """
        `ref test -up *.bib` should exit with an error
        """
        pass
