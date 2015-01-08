# -*- coding: utf-8 -*-
"""
Management utils for bibTeX database objects
"""
import pybtex.database as db


preferred_uris = {"article": "doi",
                  "book": "isbn",
                  "booklet": "",
                  "conference": "",
                  "inbook": "",
                  "incollection": "",
                  "inproceedings": "",
                  "manual": "",
                  "mastersthesis": "ocn",
                  "misc": "",
                  "phdthesis": "ocn",
                  "proceedings": "",
                  "techreport": "",
                  "unpublished": "",}

                  
def merge(*args):
    """
    Combine an arbitrary number of bib databases

    Description
    ===========
    This method takes an arbitrary number of bib databases and returns two objects: a merged bib database containing all unique entries in the set of input bib databases, and a list of all the duplicate bib entries.

    Bib entries are added to the merged bib database in the order in which bib database objects are passed to this method. Therefore, if  duplicate bib entries exist in the set of bib databases passed to this object, only the first unique entry is added to the resulting merged bib database.

    The bib databases passed to this method are not modified.

    This method also returns a list of all the duplicate bib entry objects, i.e. those with identical keys. This method constructs and returns a list of bib entries which contain duplicate keys along with the merged bib database object. This list is grouped according to key, so the first several items will have the same key, the next several will have the same key (differing from the first), and so on. The first bib entry in each sequence will be taken from the merged bib database, and each subsequent bib entry is taken from subsequent bib databases passed to this method.

    Note that multiple bib entries may have identical keys and yet have completely different metadata which populate the other fields of the entry. This method only checks for identical keys and nothing else.


    Example
    =======
    Say three bib databases are passed to this method, A, B, and C. Database A has entries a, b, and c; database B has entries d, b, and e; and database C has entries b, f, and a. This method will iterate over the entries in A, B, and C and generate a bib database with entries a, b, c, d, e, and f. It will also return a list of bib entries b (from database A), b (from B), b (from C), a (from A), and a (from C).
    """
    bib = db.BibliographyData()

    for arg in args:
        for entry in arg.entries.itervalues():
            bib.add_entry(entry.key, entry)

    return bib


def entries_missing_uris(bib):
    """
    Return keys of database entries missing a URI
    """
    pass


def set_keys_to_uris(bib):
    """
    Return database with each entry key set to its URI
    """
    pass
