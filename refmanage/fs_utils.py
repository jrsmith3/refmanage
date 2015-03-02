# -*- coding: utf-8 -*-
import os
import glob
import pathlib2 as pathlib
from pybtex.database.input import bibtex
from pybtex.exceptions import PybtexError


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
    List of dicts for use in refmanage

    For each argument passed to this method, a dictionary of relevant information is built. These dicts are assembled into a list and returned.

    :param pathlib.Path *paths: Path to BibTeX file.
    :rtype list:
    """
    bibs = [construct_bib_dict(path) for path in paths]
    return bibs


def construct_bib_dict(path):
    """
    Create dict containing data for use in refmanage

    This method creates dicts containing information for use in refmanage corresponding to the file indicated by `path`. Each dictionary contains the following data:

    * path: The `pathlib.Path` object passed as the argument to this method.
    * bib: BibTeX data, stored as a `pybtex.database.BibliographyData` object, parsed from the file indicated by the `path` key. If the file was unparseable, the exception raised during parsing is stored in this variable.
    * terse_msg: Message corresponding to the file to be printed to STDOUT when the "--verbose" flag is absent from the command line.
    * verbose_msg: Message corresponding to the file to be printed to STDOUT when the "--verbose" flag is passed on the command line.

    :param pathlib.Path path: Path to BibTeX file.
    """
    bib = parse_bib_file(path)
    terse_msg = generate_terse_output_message(path)
    verbose_msg = generate_verbose_err_output_message(bib)

    bib_dict = {"path": path,
        "bib": bib,
        "terse_msg": terse_msg,
        "verbose_msg": verbose_msg,}

    return bib_dict


def parse_bib_file(path):
    """
    Parse BibTeX file located at `path`

    This method attempts to parse the BibTeX file located at `path`. If the file is parseable, a `pybtex.database.BibliographyData` object is returned, containing the bibliography data contained in the file. If the file is unparseable, the exception raised by the parser is returned.

    :param pathlib.Path path: Path to BibTeX file.
    """
    parser = bibtex.Parser()
    try:
        bib = parser.parse_file(str(path.resolve()))
    except PybtexError, e:
        bib = e

    return bib


def bib_subdict(bibs, val_type):
    """
    Subdict with keys of instance `val_type`

    :param dict bibs:
    :param type val_type:
    :rtype dict:
    """
    subdict = {key: val for (key, val) in bibs.iteritems() if isinstance(val, val_type)}
    return subdict


def generate_terse_output_message(path):
    """
    Generate non-verbose output message
    """
    terse_msg = str(path.resolve())
    return terse_msg


def generate_verbose_err_output_message(err):
    """
    Generate output message for an error
    """
    msg = ""
    try:
        msg += val.error_type + "\n"
        msg += val.message + "\n"
        msg += val.linno + "\n"
        msg += get_context()
    except:
        pass

    return msg
