# -*- coding: utf-8 -*-
import StringIO
import pathlib2 as pathlib
from pybtex.database.input import bibtex
from pybtex.exceptions import PybtexError
from pybtex.scanner import TokenRequired
from exceptions import UnparseableBibtexError, ParseableBibtexError


class RefFile(object):
    """
    Base class of BibTeX file model classes
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
        raise NotImplementedError()


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
        raise NotImplementedError()


    def terse_msg(self):
        """
        Component of STDOUT message listing `self.path`

        :rtype: unicode
        """
        msg = unicode(self.path.resolve())
        return msg


    def verbose_msg(self):
        raise NotImplementedError()


    def test_msg(self, verbose=False):
        """
        STDOUT message for "test" command-line functionality

        :param bool verbose: Switch to [in|ex]clude verbose message
        :rtype: unicode
        """
        msg = self.terse_msg()
        if verbose:
            msg += "\n" + self.verbose_msg()

        return msg


class BibFile(RefFile):
    """
    Common functionality for a file containing BibTeX

    :param pathlib.Path path: Path to file containing BibTeX data.
    :raises UnparseableBibtexError: if the `pathlib.Path` points to an unparseable BibTeX file.
    """
    @property
    def bib(self):
        """
        Bibliography data (read-only)

        :type: `pybtex.database.BibliographyData`
        """
        return self._bib


    def _parse_bib_file(self):
        """
        Parse BibTeX located at `self.path`, set `self.bib`
        """
        parser = bibtex.Parser()
        try:
            bib = parser.parse_stream(StringIO.StringIO(self.src_txt))
        except PybtexError:
            raise UnparseableBibtexError()

        self._bib = bib


    def verbose_msg(self):
        """
        Component of STDOUT message when "--verbose" flag set

        :rtype: unicode
        """
        return u""


class NonbibFile(RefFile):
    """
    Common functionality for a file containing unparseable BibTeX

    :param pathlib.Path path: Path to file containing BibTeX data.
    :raises ParseableBibtexError: if the `pathlib.Path` points to a parseable BibTeX file.
    """
    @property
    def bib(self):
        """
        Bibliography data (read-only)

        :type: `pybtex.exceptions.PybtexError`
        """
        return self._bib


    def _parse_bib_file(self):
        """
        Attempt to parse BibTeX located at `self.path`

        Set `self.bib` with the exception raised upon parsing.
        """
        parser = bibtex.Parser()
        try:
            bib = parser.parse_stream(StringIO.StringIO(self.src_txt))
        except PybtexError, e:
            bib = e
        else:
            raise ParseableBibtexError()

        self._bib = bib


    def verbose_msg(self):
        """
        Component of STDOUT message when "--verbose" flag set

        :rtype: unicode
        """
        msg = u""
        if isinstance(self.bib, TokenRequired):
            msg += self.bib.error_type + ": "
            msg += self.bib.message + "\n"
            msg += str(self.bib.lineno) + " "
            msg += self.bib.get_context()
        elif isinstance(self.bib, PybtexError):
            msg += self.bib.message

        return msg

