# -*- coding: utf-8 -*-
import os
import argparse
import fs_utils


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
    for path in paths:
        print(path.resolve())


if __name__ == '__main__':
    main()
