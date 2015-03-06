# -*- coding: utf-8 -*-
from distutils.core import setup
import refmanage

setup(name="refmanage",
      version=refmanage.__version__,
      author="Joshua Ryan Smith",
      author_email="joshua.r.smith@gmail.com",
      packages=["refmanage"],
      url="https://github.com/jrsmith3/refmanage",
      description="Manage a BibTeX database",
      classifiers=["Programming Language :: Python",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Development Status :: 3 - Alpha",
                   "Intended Audience :: Science/Research",
                   "Topic :: Text Processing",
                   "Natural Language :: English", ],
      install_requires=["pybtex",
                        "pathlib2",],
      entry_points={"console_scripts": "ref=refmanage.refmanage:main"},)
