# -*- coding: utf-8 -*-
from distutils.core import setup

setup(name = "refmanage",
      version = "0.0.1",
      author = "Joshua Ryan Smith",
      author_email = "joshua.r.smith@gmail.com",
      packages = ["refmanage"],
      url = "https://github.com/jrsmith3/refmanage",
      description = "Manage a BibTeX database.",
      classifiers = ["Programming Language :: Python",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                     "Development Status :: 3 - Alpha",
                     "Intended Audience :: Science/Research",
                     "Topic :: Text Processing",
                     "Natural Language :: English",],
      install_requires = ["pybtex"],)
