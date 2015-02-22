# -*- coding: utf-8 -*-
import os
import glob
import pathlib2 as pathlib
from pybtex.database.input import bibtex


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


def import_bib_files(*paths):
    """
    Create dictionary of path and corresponding BibTeX

    For each argument passed to this method, the corresponding BibTeX file is parsed. This method constructs a dictionary with each `pathlib.Path` argument as a key and the corresponding parsed BibTeX as the value. If the file specified by an argument to this method cannot be parsed, a value of `None` is recorded in the dictionary.

    :param patlib.Path *paths: Path to BibTeX file.    
    :rtype dict:
    """
    bib_filenames_files = {}
    for path in paths:
        parser = bibtex.Parser()
        fqpn = str(path.resolve())
        try:
            bib = parser.parse_file(fqpn)
            del parser
        except:
            bib = None
        bib_filenames_files[fqpn] = bib

    return bib_filenames_files

