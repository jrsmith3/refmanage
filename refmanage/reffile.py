# -*- coding: utf-8 -*-
import StringIO
import pathlib2 as pathlib
from pybtex.database.input import bibtex
from pybtex.exceptions import PybtexError
from pybtex.scanner import TokenRequired


class BibFile(object):
    """
    Common functionality for a file containing BibTeX

    :param pathlib.Path path: Path to file containing BibTeX data.
    """
    @property
    def path(self):
        """
        Path to file containing BibTeX (read-only)

        :type: `pathlib.Path`
        """
        return self._path

    @property
    def bib(self):
        """
        Bibliography data (read-only)

        :type: `pybtex.database.BibliographyData`
        """
        return self._bib

    @property
    def src_txt(self):
        """
        String representation of source BibTeX data (read-only)

        :type: `str`
        """
        return self._src_txt

    def __init__(self, path):
        self._path = path
        with self.path.open() as f: self._src_txt = f.read()
        self._parse_bib_file()


    def _parse_bib_file(self):
        """
        Parse BibTeX file located at `self.path`

        This method attempts to parse the BibTeX file located at `self.path`. If the file is parseable, `self.bib` is set to a `pybtex.database.BibliographyData` object, containing the bibliography data contained in the file. If the file is unparseable, `self.bib` is set to the exception raised by the parser.
        """
        parser = bibtex.Parser()
        try:
            bib = parser.parse_stream(StringIO.StringIO(self.src_txt))
        except PybtexError, e:
            bib = e

        self._bib = bib


    def terse_msg(self):
        """
        Component of STDOUT message listing `self.path`

        :rtype: str
        """
        msg = str(self.path.resolve())
        return msg


    def verbose_msg(self):
        """
        Component of STDOUT message when "--verbose" flag set

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
        STDOUT message for "test" command-line functionality

        :param bool verbose: Switch to [in|ex]clude verbose message
        :rtype: str
        """
        msg = self.terse_msg()
        if verbose:
            msg += "\n" + self.verbose_msg()

        return msg

