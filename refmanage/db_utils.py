# -*- coding: utf-8 -*-
"""
Management utils for bibTeX database objects
"""
import pybtex.database as db


def cat_db(*args):
    """
    Concatenate multiple bib databases, return result
    """
    new_bib = db.BibliographyData()

    for arg in args:
        for entry in arg.entries.itervalues():
            new_bib.add_entry(entry.key, entry)

    return new_bib
