# -*- coding: utf-8 -*-
import os
import glob
import pathlib2 as pathlib


def handle_files_args(paths_args):
    """
    Handle files arguments from command line

    This method takes a list of strings representing paths passed to the cli. It expands the path arguments and creates a list of pathlib.Path objects which unambiguously point to the files indicated by the command line arguments.

    :param list paths_args: Paths to files.
    """
    for paths_arg in paths_args:
        # Handle paths implicitly rooted at user home dir
        paths_arg = os.path.expanduser(paths_arg)

        # Expand wildcards
        paths_arg = glob.glob(paths_arg)

        # Create list of pathlib.Path objects
        paths = [pathlib.Path(path_arg) for path_arg in paths_arg]

    return paths
