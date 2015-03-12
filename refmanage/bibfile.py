# -*- coding: utf-8 -*-
import pathlib2 as pathlib
from pybtex.database.input import bibtex
from pybtex.exceptions import PybtexError
from pybtex.scanner import TokenRequired


class BibFile(object):
    """
    `BibFile` objects are immutable.

    :param pathlib.Path path: Path to file possibly containing BibTeX data.
    """
    def __init__(self, path):
        self.path = path
        self._parse_bib_file()


    def _parse_bib_file(self):
        """
        Parse BibTeX file located at `self.path`

        This method attempts to parse the BibTeX file located at `self.path`. If the file is parseable, `self.bib` is set to a `pybtex.database.BibliographyData` object, containing the bibliography data contained in the file. If the file is unparseable, `self.bib` is set to the exception raised by the parser.
        """
        parser = bibtex.Parser()
        try:
            bib = parser.parse_file(str(self.path.resolve()))
        except PybtexError, e:
            bib = e

        self.bib = bib


    def terse_msg(self):
        """
        STDOUT message listing `self.path`

        This method generates and returns the message to be returned to STDOUT which corresponds to `self.path`.
        """
        terse_msg = str(self.path.resolve())
        return terse_msg


def gen_verbose_msg(bib):
    """
    STDOUT message corresponding to `path` when --verbose set

    This method generates and returns the message to be returned to STDOUT which corresponds to the `path` argument to this method in the event the "--verbose" flag was passed on the command-line. This method can accept an arguent of two different types: a `pybtex.database.BibliographyData` or `pybtex.exceptions.PybtexError`. If `bib` is of type `BibliographyData`, this method will return an empty string. If `bib` is of type `PybtexError`, this method will gather data from the exception into a string which is returned.

    :param bib: Output of `parse_bib_file`; can be either a `pybtex.database.BibliographyData` or `pybtex.exceptions.PybtexError`.
    :rtype: str
    """
    msg = ""
    if isinstance(bib, TokenRequired):
        msg += bib.error_type + ": "
        msg += bib.message + "\n"
        msg += str(bib.lineno) + " "
        msg += bib.get_context()
    elif isinstance(bib, PybtexError):
        msg += bib.message

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

