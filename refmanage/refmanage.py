# -*- coding: utf-8 -*-
"""
refmanage - Manage a BibTeX database.
"""
import os
import argparse
from pybtex.database.output.bibtex import Writer


def cl_merge(cl_args):
    """
    Handles the case "merge" was called on the command line.

    :param argparse.Namespace cl_args: Command-line arguments.
    """
    bib_filenames = list_bibtex_at_sources(cl_args.source)
    source_bib_filenames_files = import_bib_files(bib_filenames)

    # Note the following merges everything without regards to duplicates or changing bibTeX keys to UIDs.
    sources_bib = merge_pybdb(source_bib_filenames_files.values())

    # Import the target according to the `overwrite` flag, but first get the target's fully-qualified path name.
    target_fqpn = os.path.abspath(cl_args.target)
    target_bib = import_target(target_fqpn, cl_args.overwrite)

    # Combine the target and sources
    combined_bib = merge_pybdb(target_bib, sources_bib)

    # Write combined_bib to the specified file.
    w = Writer()
    w.write_file(combined_bib, target_fqpn)


def main():
    """
    Command line interface.
    """
    parser = argparse.ArgumentParser(description = "Manage bibTeX files.")

    append_overwrite_grp = parser.add_mutually_exclusive_group()

    append_overwrite_grp.add_argument("-a", "--append",
        help = "Append contents of merged source bibTeX files to target.",
        default = True,
        action = "store_true",)

    append_overwrite_grp.add_argument("-o", "--overwrite",
        help = "Overwrite target with merged source bibTeX files.",
        default = False,
        action = "store_true",)

    parser.add_argument("-i", "--include-dups",
        help = "Include duplicates to target in soure bibTeX files if they exist.",
        default = False,
        action = "store_true",)

    parser.add_argument("target",
        help = "File into which bibTeX source(s) will be merged. If the file does not exist, it will be created.",
        type = str,)

    parser.add_argument("-d", "--delete",
        help = "Delete successfully merged source bibTeX files.",
        default = False,
        action = "store_true",)

    parser.add_argument("-k", "--key-with-uid",
        help = "Change bibTeX keys in source files to UID (DOI, ISBN, etc.).",
        default = True,
        action = "store_true",)

    parser.add_argument("source",
        help = "File(s) containing bibTeX to be merged. If no argument is given, \"*.bib\" in the current directory is assumed. If a directory is given, \"*.bib\" in the specified directory is assumed.",
        nargs = "*",
        default = "*.bib",
        type = str,)

    cl_args = parser.parse_args()
    cl_merge(cl_args)
