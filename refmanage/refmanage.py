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
    Implement "test" command-line functionality
    """
    paths = fs_utils.handle_files_args(*args.paths_args)
    bibs_paths_dict = fs_utils.import_bib_files(*paths)

    parseables = []
    unparseables = []

    for key in bibs_paths_dict.keys():
        if bibs_paths_dict[key] is None:
            unparseables.append(key)
        else:
            parseables.append(key)

    print("The following files are unparseable:")
    for unparseable in unparseables:
        print("\t" + str(unparseable.resolve()))


if __name__ == '__main__':
    main()
