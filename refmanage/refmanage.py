# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
refmanage - Manage a BibTeX database.
"""

import pybtex.database as db
from pybtex.database.input import bibtex
from pybtex.database.output.bibtex import Writer


def merge_bib(*args):
    """
    Merge two bibtex databases, return the result.
    """
    new_bib = db.BibliographyData()

    for arg in args:
        for entry in arg.entries.itervalues():
            new_bib.add_entry(entry.key, entry)

    return new_bib
