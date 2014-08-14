# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
refmanage - Manage a BibTeX database.
"""
import os
import glob
import argparse
import pybtex.database as db
from pybtex.database.input import bibtex
from pybtex.database.output.bibtex import Writer


def merge_pybdb(*args):
    """
    Merge multiple pybtex databases, return the result.
    """
    new_bib = db.BibliographyData()

    for arg in args:
        for entry in arg.entries.itervalues():
            new_bib.add_entry(entry.key, entry)

    return new_bib


def list_bib_filenames(fqpn):
    """
    List of fully-qualified pathnames of only bibTeX files (.bib extension).

    Note that this method only finds files with a .bib extension and does no checking that these files are valid bibTeX.

    :param str fqpn: Fully-qualified path name of directory in which to find bibTeX files.
    """
    fqpn_glob = os.path.join(fqpn, "*.bib")
    bib_filenames = glob.glob(fqpn_glob)

    return bib_filenames


def import_bib_files(bib_filenames):
    """
    Returns dict with fully-qualified path as key, corresponding bibTeX database as entry.

    This method iterates over the filenames specified in `bib_filenames` and attempts to parse the file found at that path using pybtex. Each path is assigned to the key of a dict. If the parse is successful, the resulting object is assigned to the corresponding value in the dict. If the file cannot be parsed, a value of `None` is assigned to the value of the dict.

    :param list bib_filenames: List of fully-qualified path names of candidate bibTeX files to import.
    """
    bib_filenames_files = {}
    for filename in bib_filenames:
        try:
            parser = bibtex.Parser()
            bib = parser.parse_file(filename)
            del parser
        except:
            bib = None
        bib_filenames_files[filename] = bib

    return bib_filenames_files

def merge():
    """
    Handles the case "merge" was called on the command line.
    """
    pass


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

    bib_filenames = list_bib_filenames(pwd)
    filenames_failed_imports = []
    combined_bib = db.BibliographyData()

    for filename in bib_filenames:
        try:
            parser = bibtex.Parser()
            bib = parser.parse_file(filename)
            del parser
        except:
            filenames_failed_imports.append(filename)

        combined_bib = merge_pybdb(combined_bib, bib)

    # Write combined_bib to the specified file.
    w = Writer()
    w.write_file(combined_bib, target_fqpn)


    if len(filenames_failed_imports) > 0:
        print "Could not parse the following files:"
        print filenames_failed_imports
