# -*- coding: utf-8 -*-
import os
import argparse
import fs_utils
from pybtex.database.input import bibtex


def main():
    """
    Command-line interface
    """
    parser = argparse.ArgumentParser(description="Manage BibTeX files")

    parser.add_argument("-t", "--test",
        action="store_true",
        help="Test parseability of BibTeX file(s)",)

    parser.add_argument("-v", "--verbose",
        action="store_true",
        help="Verbose output",)

    parser.add_argument("paths_args",
        nargs="*",
        default="*.bib",
        help="File(s) to test parseability",
        metavar="files")

    args = parser.parse_args()

    test(args)


def test(args):
    """
    Logic for "test" functionality
    """
    paths = fs_utils.handle_files_args(*args.paths_args)
    parseables = {}
    unparseables = {}

    for path in paths:
        try:
            parser = bibtex.Parser()
            bib = parser.parse_file(path.resolve())
            del parser
            parseables[path] = bib
        except:
            bib = None
            unparseables[path] = bib
        
    print [path.resolve() for path in unparseables.keys()]


if __name__ == '__main__':
    main()
