# -*- coding: utf-8 -*-
import os
import sys
import argparse
import version
import utils
from pybtex.database import BibliographyData
from pybtex.exceptions import PybtexError


def define_parser():
    """
    Command-line interface
    """
    parser = argparse.ArgumentParser(description="Manage BibTeX files")

    parser.add_argument("--version",
        action="store_true",
        help="Print version information")

    parser.add_argument("-t", "--test",
        action="store_true",
        help="Test parseability of BibTeX file(s)",)

    parser.add_argument("-v", "--verbose",
        action="store_true",
        help="Verbose output",)

    parseability = parser.add_mutually_exclusive_group()

    parseability.add_argument("-u", "--unparseable",
        action="store_true",
        default=True,
        help="Print only list of parseable files",)

    parseability.add_argument("-p", "--parseable",
        action="store_true",
        help="Print only list of parseable files",)

    parser.add_argument("paths_args",
        nargs="*",
        default=["*.bib"],
        help="File(s) to test parseability",
        metavar="files")

    return parser


def cli_args_dispatcher(args):
    """
    Dispatch functionality based on command-line args
    """
    if args.version:
        ver(args)
    elif args.test:
        test(args)


def main():
    """
    Method called via command-line
    """
    parser = define_parser()
    args = parser.parse_args()
    cli_args_dispatcher(args)


def ver(args):
    """
    Implement "version" command-line functionality
    """
    sys.stdout.write(version.__version__ + "\n")


def test(args):
    """
    Implement "test" command-line functionality
    """
    paths = utils.handle_files_args(*args.paths_args)
    bibfile_data = utils.construct_bibfile_data(*paths)

    if args.parseable:
        sublist = utils.bib_sublist(bibfile_data, BibliographyData)
    else:
        sublist = utils.bib_sublist(bibfile_data, PybtexError)

    msg = utils.gen_stdout_test_msg(sublist, args.verbose)

    sys.stdout.write(msg)
