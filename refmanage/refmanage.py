# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
refmanage - Manage a BibTeX database.
"""
import os
import glob
import argparse
import warnings
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


def list_bibtex_at_source(source):
    """
    List of bibTeX file(s) located at `source`.

    :param str source: Path to bibTeX file(s). `source` can be relative or absolute, and it can contain a wildcard ("*"), it can correspond to a directory, or it can indicate a file. If `source` indicates a directory, this method returns a list of all files ending in extension ".bib".
    """
    fqpn = os.path.abspath(source)
    bib_filenames = []
    if "*" in fqpn:
        bib_filenames = glob.glob(fqpn)
    elif os.path.exists(fqpn):
        if os.path.isdir(fqpn):
            bib_filenames = glob.glob(os.path.join(fqpn, "*.bib"))
        elif os.path.isfile(fqpn):
            bib_filenames = [fqpn]
        else:
            raise IOError("Path %s appears to exist, but is neither a directory nor a file. Aborting." % fqpn)
    else:
        warnings.warn("Path %s not found, skipping." % source)


def list_bibtex_at_sources(sources):
    """
    List of bibTeX file(s) located at every path in `sources`.

    :param list sources: List containing paths to bibTeX file(s). Each element must conform to the input of `list_bibtex_at_source`.
    """
    bib_filenames = []
    for source in sources:
        bib_filenames += list_bibtex_at_source(source)

    return bib_filenames


def import_target(target_fqpn, overwrite = False):
    """
    Returns pybtex database of target bibTeX database.

    If the path to `target_fqpn`, an exception will be raised. If the path to `target_fqpn` exists, but the file does not, the `overwrite` flag is moot and an empty pybtex database will be returned.

    :param str target_fqpn: Fully-qualified pathname to target bibTeX database. This path must be absolute, but it must point to a file. The filename can have an arbitrary (or no) extension.
    :param bool overwrite: Switch to append source bibTeX to target or overwrite target with source bibTeX. Default = False.
    """
    target_parent_dir = os.path.dirname(target_fqpn)

    if not os.path.isdir(target_parent_dir):
        # Parent directory does not exist. Raise exception.
        error_message = "Path %s does not exist. Exiting." % target_parent_dir
        raise IOError(error_message)

    if os.path.isdir(target_fqpn):
        # Target is a directory and not a file. Raise exception.
        error_message = "Target %s is a directory and not a file. Exiting." % target_parent_dir
        raise IOError(error_message)

    if os.path.isfile(target_fqpn):
        if not overwrite:
            # Read file as pybtex database.
            # Note that no additional `else` or `elif` statement is necessary here because the end result will be the same if the user wants to overwrite an existing target or if no target exists. An empty pybtex database is returned in both cases.
            parser = bibtex.Parser()
            target_bib = parser.parse_file(target_fqpn)
    else:
        # Create an empty pybtex database.
        target_bib = db.BibliographyData()

    return target_bib


def cl_merge(cl_args):
    """
    Handles the case "merge" was called on the command line.

    :param argparse.Namespace cl_args: Command-line arguments.
    """
    bib_filenames = list_bibtex_at_sources(cl_args.source)
    source_bib_filenames_files = import_bib_files(bib_filenames)

    # Note the following merges everything without regards to duplicates or changing bibTeX keys to UIDs.
    sources_bib = merge_pybdb(source_bib_filenames_files.values())

    # Import the target according to the `overwrite` flag, but first get the target's fully-qualified path name.
    target_fqpn = os.path.abspath(cl_args.target)
    target_bib = import_target(target_fqpn, cl_args.overwrite)

    # Combine the target and sources
    combined_bib = merge_pybdb(target_bib, sources_bib)

    # Write combined_bib to the specified file.
    w = Writer()
    w.write_file(combined_bib, target_fqpn)


def main():
    """
    Command line interface.
    """
    parser = argparse.ArgumentParser(description = "Manage bibTeX files.")

    append_overwrite_grp = parser.add_mutually_exclusive_group()

    append_overwrite_grp.add_argument("-a", "--append",
        help = "Append contents of merged source bibTeX files to target.",
        default = True,
        action = "store_true",)

    append_overwrite_grp.add_argument("-o", "--overwrite",
        help = "Overwrite target with merged source bibTeX files.",
        default = False,
        action = "store_true",)

    parser.add_argument("-i", "--include-dups",
        help = "Include duplicates to target in soure bibTeX files if they exist.",
        default = False,
        action = "store_true",)

    parser.add_argument("target",
        help = "File into which bibTeX source(s) will be merged. If the file does not exist, it will be created.",
        type = str,)

    parser.add_argument("-d", "--delete",
        help = "Delete successfully merged source bibTeX files.",
        default = False,
        action = "store_true",)

    parser.add_argument("-k", "--key-with-uid",
        help = "Change bibTeX keys in source files to UID (DOI, ISBN, etc.).",
        default = True,
        action = "store_true",)

    parser.add_argument("source",
        help = "File(s) containing bibTeX to be merged. If no argument is given, \"*.bib\" in the current directory is assumed. If a directory is given, \"*.bib\" in the specified directory is assumed.",
        nargs = "*",
        default = "*.bib",
        type = str,)

    cl_args = parser.parse_args()
    cl_merge(cl_args)



    # pwd = os.getcwd()
    # target_fqpn = os.path.join(pwd, args.target)
    # if os.path.exists(target_fqpn):
    #     raise OSError("%s already exists." % target_fqpn)

    # bib_filenames = list_bib_filenames(pwd)
    # filenames_failed_imports = []
    # combined_bib = db.BibliographyData()

    # for filename in bib_filenames:
    #     try:
    #         parser = bibtex.Parser()
    #         bib = parser.parse_file(filename)
    #         del parser
    #     except:
    #         filenames_failed_imports.append(filename)

    #     combined_bib = merge_pybdb(combined_bib, bib)

    # # Write combined_bib to the specified file.
    # w = Writer()
    # w.write_file(combined_bib, target_fqpn)


    # if len(filenames_failed_imports) > 0:
    #     print "Could not parse the following files:"
    #     print filenames_failed_imports
