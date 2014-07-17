# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='refmanage',
      version='0.0.1',
      author='Joshua Ryan Smith',
      author_email='joshua.r.smith@gmail.com',
      packages=['refmanage'],
      url='https://github.com/jrsmith3/refmanage',
      description='Manage a BibTeX database.',
      install_requires=[],
      test_suite='nose.collector',
      tests_require=['nose'],
      license='MIT',
      zip_safe=False,
      entry_points= {"console_scripts":
            ["refmanage = refmanage.refmanage:main",]
      },)
