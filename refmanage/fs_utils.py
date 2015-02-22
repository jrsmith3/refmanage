# -*- coding: utf-8 -*-
import os
import glob
import pathlib2 as pathlib


def handle_files_args(*paths_args):
    """
    Handle file(s) arguments from command line

    This method takes the string(s) which were passed to the cli which indicate the files on which to operate. It expands the path arguments and creates a list of `pathlib.Path` objects which unambiguously point to the files indicated by the cli arguments.

    :param str *paths_args: Paths to files.
    :rtype: list
    """
    paths = []

    for paths_arg in paths_args:
        # Handle paths implicitly rooted at user home dir
        paths_arg = os.path.expanduser(paths_arg)

        # Expand wildcards
        paths_arg = glob.glob(paths_arg)

        # Create list of pathlib.Path objects
        paths.extend([pathlib.Path(path_arg) for path_arg in paths_arg])

    return paths


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

