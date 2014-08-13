# -*- coding: utf-8 -*-
import unittest
import os
import refmanage
import pybtex
from pybtex.database.input import bibtex

test_dir_root = os.path.dirname(os.path.realpath(__file__))

p2 = bibtex.Parser()
b2_path = os.path.join(test_dir_root, "bib2.bib")
bib2 = p2.parse_file(b2_path)

p3 = bibtex.Parser()
b3_path = os.path.join(test_dir_root, "bib3.bib")
bib3 = p3.parse_file(b3_path)

p4 = bibtex.Parser()
b4_path = os.path.join(test_dir_root, "bib4.bib")
bib4 = p4.parse_file(b4_path)


class MethodsReturnType(unittest.TestCase):
    """
    Tests output types of the methods.
    """
    def test_merge_bib(self):
        """
        merge_bib should return pybtex.database.BibliographyData.
        """
        merged = refmanage.merge_bib(bib2, bib3)
        self.assertIsInstance(merged, pybtex.database.BibliographyData)


class MethodsFunctionality(unittest.TestCase):
    """
    Tests proper functionality of the methods.
    """
    def test_merge_bib(self):
        """
        The number of items in the object merge_bib creates should equal the sum of the number of items in all the calling args.
        """
        merged = refmanage.merge_bib(bib2, bib3)
        len_merged = len(merged.entries)
        len_bib2 = len(bib2.entries)
        len_bib3 = len(bib3.entries)

        self.assertEqual(len_merged, len_bib2 + len_bib3)
        
