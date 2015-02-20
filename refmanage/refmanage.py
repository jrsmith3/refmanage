# -*- coding: utf-8 -*-
import os
import argparse


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

    parser.add_argument("files",
                        help="File(s) to test parseability",)

    args = parser.parse_args()


if __name__ == '__main__':
    main()
