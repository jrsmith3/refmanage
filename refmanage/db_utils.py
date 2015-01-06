# -*- coding: utf-8 -*-
"""
Management utils for bibTeX database objects
"""
import pybtex.database as db


def cat_db(*args):
    """
    Concatenate multiple bib databases, return result
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
