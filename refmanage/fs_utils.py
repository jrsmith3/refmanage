# -*- coding: utf-8 -*-
import os
import glob
import pathlib2 as pathlib


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

