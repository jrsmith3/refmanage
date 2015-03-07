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


def construct_bib_dict(path):
    """
    Create dict containing data for use in refmanage

    This method creates dicts containing information for use in refmanage corresponding to the file indicated by `path`. Each dictionary contains the following data:

    * path: The `pathlib.Path` object passed as the argument to this method.
    * bib: BibTeX data, stored as a `pybtex.database.BibliographyData` object, parsed from the file indicated by the `path` key. If the file was unparseable, the exception raised during parsing is stored in this variable.
    * terse_msg: Message corresponding to the file to be printed to STDOUT when the "--verbose" flag is absent from the command line.
    * verbose_msg: Message corresponding to the file to be printed to STDOUT when the "--verbose" flag is passed on the command line.

    :param pathlib.Path path: Path to file possibly containing BibTeX data.
    :rtype dict:
    """
    bib = parse_bib_file(path)
    terse_msg = gen_terse_msg(path)
    verbose_msg = gen_verbose_msg(bib)

    bib_dict = {"path": path,
        "bib": bib,
        "terse_msg": terse_msg,
        "verbose_msg": verbose_msg, }

    return bib_dict


def parse_bib_file(path):
    """
    Parse BibTeX file located at `path`

    This method attempts to parse the BibTeX file located at `path`. If the file is parseable, a `pybtex.database.BibliographyData` object is returned, containing the bibliography data contained in the file. If the file is unparseable, the exception raised by the parser is returned.

    :param pathlib.Path path: Path to file possibly containing BibTeX data.
    """
    parser = bibtex.Parser()
    try:
        bib = parser.parse_file(str(path.resolve()))
    except PybtexError, e:
        bib = e

    return bib


def gen_terse_msg(path):
    """
    STDOUT message corresponding to `path`

    This method generates and returns the message to be returned to STDOUT which corresponds to the `path` argument to this method.

    :param pathlib.Path path: Path to file possibly containing BibTeX data.
    :rtype: str
    """
    terse_msg = str(path.resolve())
    return terse_msg


def gen_verbose_msg(bib):
    """
    STDOUT message corresponding to `path` when --verbose set

    This method generates and returns the message to be returned to STDOUT which corresponds to the `path` argument to this method in the event the "--verbose" flag was passed on the command-line. This method can accept an arguent of two different types: a `pybtex.database.BibliographyData` or `pybtex.exceptions.PybtexError`. If `bib` is of type `BibliographyData`, this method will return an empty string. If `bib` is of type `PybtexError`, this method will gather data from the exception into a string which is returned.

    :param bib: Output of `parse_bib_file`; can be either a `pybtex.database.BibliographyData` or `pybtex.exceptions.PybtexError`.
    :rtype: str
    """
    msg = ""
    try:
        msg += bib.error_type + ": "
        msg += bib.message + "\n"
        msg += str(bib.lineno) + " "
        msg += bib.get_context()
    except:
        pass

    return msg


def construct_bibfile_data(*paths):
    """
    List of data corresponding to individual bib files

    For each argument passed to this method, a dictionary of relevant information is built from `construct_bib_dict`. These dicts are assembled into a list which is returned.

    :param pathlib.Path *paths: Path to file possibly containing BibTeX data.
    :rtype list:
    """
    bibs = [construct_bib_dict(path) for path in paths]
    return bibs


def bib_sublist(bibfile_data, val_type):
    """
    Sublist of bibfile_data whos elements are val_type

    This method examines each bib_dict element of a bibfile_data list and returns the subset which can be classified according to val_type.

    :param dict bibfile_data:
    :param type val_type:
    :rtype list:
    """
    sublist = [bib_dict for bib_dict in bibfile_data if isinstance(bib_dict["bib"], val_type)]
    return sublist
    pass


def gen_stdout_test_msg(bibfile_data, verbose=False):
    """
    Generate appropriate message for STDOUT

    This method creates the string to be printed to STDOUT from the items of the `bibfile_data` list argument. It generates either a terse or verbose message based on the state of the `verbose` argument.

    :param list bibfile_data: List containing bib_dicts.
    :param bool verbose: Directive to construct verbose/terse STDOUT string.
    :rtype: str
    """
    msg_list = [gen_bib_dict_test_msg(bib_dict, verbose) for bib_dict in bibfile_data]
    msg = "\n\n".join(msg_list)
    return msg


def gen_bib_dict_test_msg(bib_dict, verbose=False):
    """
    Generate appropriate STDOUT message given bib_dict

    This method creates the string to be printed to STDOUT for a single bib_dict. It generates either a terse or verbose message based on the state of the `verbose` argument.

    :param dict bib_dict: Dictionary containing bib file information.
    :param bool verbose: Directive to construct verbose/terse STDOUT string.
    :rtype: str
    """
    msg = bib_dict["terse_msg"]
    if verbose:
        msg += "\n" + bib_dict["verbose_msg"]

    return msg
