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

    Each dictionary contains several keys for use in the functionality of refmanage:

    * path: A `pathlib.Path` object pointing to a file indicated on the command-line.
    * bib: BibTeX data, stored as a `pybtex.database.BibliographyData` object, parsed from the file indicated by the `path` key. If the file was unparseable, the exception raised is stored in this variable.
    * terse_msg: Message corresponding to the file to be printed to STDOUT when the "--verbose" flag is absent from the command line.
    * verbose_msg: Message corresponding to the file to be printed to STDOUT when the "--verbose" flag is passed on the command line.

    :param patlib.Path *paths: Path to BibTeX file.
    :rtype list:
    """
    bibs = []

    for path in paths:
        parser = bibtex.Parser()
        try:
            bib = parser.parse_file(fqpn)
        except PybtexError, e:
            bib = e
        del parser

        terse_msg = path.resolve()
        verbose_msg = generate_verbose_err_output_message(bib)

        bib_dict = {"path": path,
            "bib": bib,
            "terse_msg": terse_msg,
            "verbose_msg": verbose_msg,}

        bibs.append(bib_dict)

    return bibs


def bib_subdict(bibs, val_type):
    """
    Subdict with keys of instance `val_type`

    :param dict bibs:
    :param type val_type:
    :rtype dict:
    """
    subdict = {key: val for (key, val) in bibs.iteritems() if isinstance(val, val_type)}
    return subdict


def generate_test_message(bibs, verbose):
    """
    Generate message for "test" functionality

    :param dict bibs:
    :param bool verbose:
    :rtype str:
    """
    terse_msgs = [key.resolve() for (key, val) in bibs.iteritems()]
    if verbose:
        verbose_msgs = [generate_verbose_err_output_message(val) for (key, val) in bibs.iteritems()]
    else:
        verbose_msgs = [""] * len(terse_msgs)

    msg = interleave_test_messages(terse_msgs, verbose_msgs)

    return msg


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


def interleave_test_messages(terse_msgs, verbose_msgs):
    """
    Interleave messages to create output text

    :param list terse_msgs:
    :param list verbose_msgs:
    :rtype str:
    """
    interleave_msgs = [x for t in zip(terse_msgs, verbose_msgs) for x in t]
    msg = "".join(interleave_msgs)

    return msg

