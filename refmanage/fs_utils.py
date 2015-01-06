# -*- coding: utf-8 -*-
"""
Management utils for filesystem
"""
import os
import glob
import warnings
import pybtex.database as db
from pybtex.database.input import bibtex


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

    Returns a list of fully-qualified pathnames at the specified source.

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

    return bib_filenames


def list_bibtex_at_sources(sources):
    """
    List of bibTeX file(s) located at every path in `sources`.

    Returns a list of fully-qualified pathnames for all files having a '.bib' extension at the specified sources. 

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
