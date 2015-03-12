# -*- coding: utf-8 -*-
import pathlib2 as pathlib
from pybtex.database.input import bibtex
from pybtex.exceptions import PybtexError
from pybtex.scanner import TokenRequired


class BibFile(object):
    """
    Class to handle files possibly containing BibTeX

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

        :rtype: str
        """
        msg = str(self.path.resolve())
        return msg


    def verbose_msg(self):
        """
        STDOUT message corresponding to `self.path` when --verbose set

        This method generates and returns the message to be returned to STDOUT which corresponds to `self.path` in the event the "--verbose" flag was passed on the command-line. If `self.bib` is of type `BibliographyData`, this method will return an empty string. If `self.bib` is of type `PybtexError`, this method will gather data from the exception into a string which is returned.
        :rtype: str
        """
        msg = ""
        if isinstance(self.bib, TokenRequired):
            msg += self.bib.error_type + ": "
            msg += self.bib.message + "\n"
            msg += str(self.bib.lineno) + " "
            msg += self.bib.get_context()
        elif isinstance(self.bib, PybtexError):
            msg += self.bib.message

        return msg


    def test_msg(self, verbose=False):
        """
        Generate appropriate STDOUT message

        This method creates the string to be printed to STDOUT for a single bib_dict. It generates either a terse or verbose message based on the state of the `verbose` argument.

        :rtype: str
        """
        msg = self.terse_msg()
        if verbose:
            msg += "\n" + self.verbose_msg()

        return msg

