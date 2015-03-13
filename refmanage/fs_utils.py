# -*- coding: utf-8 -*-
"""
Utility functions (:mod:`refmanage.fs_utils`)
=============================================

.. currentmodule:: fs_utils
"""

import os
import glob
import pathlib2 as pathlib
from pybtex.database.input import bibtex
from pybtex.exceptions import PybtexError
from pybtex.scanner import TokenRequired
from reffile import BibFile, NonbibFile
from exceptions import UnparseableBibtexError


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


def reffile_factory(path):
    """
    Factory method to return child of RefFile

    This method returns either a BibFile or NonbibFile object depending on which is appropriate based on if the `path` arg points to a file containing valid BibTeX or invalid BibTeX, respectively.

    :param pathlib.Path path: Path to file possibly containing BibTeX data.
    :rtype: BibFile or NonbibFile depending on input.
    """
    try:
        b = BibFile(path)
    except UnparseableBibtexError:
        b = NonbibFile(path)
    return b


def construct_bibfile_data(*paths):
    """
    List of data corresponding to individual bib files

    For each argument passed to this method, a dictionary of relevant information is built from `construct_bib_dict`. These dicts are assembled into a list which is returned.

    :param pathlib.Path *paths: Path to file possibly containing BibTeX data.
    :rtype: list
    """
    bibs = [reffile_factory(path) for path in paths]
    return bibs


def bib_sublist(bibfile_data, val_type):
    """
    Sublist of bibfile_data whos elements are val_type

    This method examines each bib_dict element of a bibfile_data list and returns the subset which can be classified according to val_type.

    :param list bibfile_data: List containing `BibFile`s.
    :param type val_type:
    :rtype: list
    """
    sublist = [bibfile for bibfile in bibfile_data if isinstance(bibfile.bib, val_type)]
    return sublist
    pass


def gen_stdout_test_msg(bibfile_data, verbose=False):
    """
    Generate appropriate message for STDOUT

    This method creates the string to be printed to STDOUT from the items of the `bibfile_data` list argument. It generates either a terse or verbose message based on the state of the `verbose` argument.

    :param list bibfile_data: List containing `BibFile`s.
    :param bool verbose: Directive to construct verbose/terse STDOUT string.
    :rtype: str
    """
    msg_list = [bibfile.test_msg(verbose) for bibfile in bibfile_data]
    msg = "\n\n".join(msg_list)
    return msg
