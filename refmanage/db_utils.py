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

    This method merges an arbitrary number of bib databases together and returns the result. Bib entries are added from each bib database in the order in which they are passed to the method. Bib databases which are passed to this method are not modified. 

    This method also returns a list of all the duplicate bib entry objects, i.e. those with identical keys. Bib entries are added in the order bib database objects are passed to this method; therefore, duplicate bib entries in later bib database objects are not included in the returned bib database object. The list of duplicate bib entries contains *all* duplicates, including the entry in the returned bib database.
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
