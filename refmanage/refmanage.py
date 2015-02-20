# -*- coding: utf-8 -*-
import os
import argparse


def main():
    """
    Command-line interface
    """
    parser = argparse.ArgumentParser(description="Manage BibTeX files")

    parser.add_argument("-t", "--test",
                        help="Test parseability of BibTeX file(s)",
                        action="store_true",)

    parser.add_argument("-v", "--verbose",
                        help="Verbose output",
                        action="store_true",)

    parser.add_argument("files",
                        help="File(s) to test parseability")

    args = parser.parse_args()


if __name__ == '__main__':
    main()
