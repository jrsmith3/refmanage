# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
refmanage - Manage a BibTeX database.
"""
import os
import argparse
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

def get_bib_filenames(fqpn):
    """
    Returns a list of fully-qualified paths of only bibTeX files.
    """
    filenames = [f for f in os.listdir(fqpn) if os.path.isfile(os.path.join(fqpn,f))]

    bib_filenames = [f for f in filenames if f.endswith(".bib")]

    return bib_filenames


def main():
    """
    Command line interface.
    """
    parser = argparse.ArgumentParser(description = "Manage bibTeX files.")

    parser.add_argument("target",
        help = "File to contain combined bibTeX.")

    args = parser.parse_args()

    pwd = os.getcwd()
    target_fqpn = os.path.join(pwd, args.target)
    if os.path.exists(target_fqpn):
        raise OSError("%s already exists." % target_fqpn)

    bib_filenames = get_bib_filenames(pwd)
    filenames_failed_imports = []
    combined_bib = db.BibliographyData()

    for filename in bib_filenames:
        try:
            parser = bibtex.Parser()
            bib = parser.parse_file(filename)
            del parser
        except:
            filenames_failed_imports.append(filename)

        combined_bib = merge_bib(combined_bib, bib)

    # Write combined_bib to the specified file.
    w = Writer()
    w.write_file(combined_bib, target_fqpn)


    if len(filenames_failed_imports) > 0:
        print "Could not parse the following files:"
        print filenames_failed_imports
