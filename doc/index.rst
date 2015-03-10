.. refmanage documentation master file, created by
   sphinx-quickstart on Tue Mar 10 19:08:03 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

refmanage - Manage a BibTeX database
====================================

.. toctree::
   :maxdepth: 2


Scope
=====
This project features a command line program, `ref`, written in python, to manage BibTeX database files.


Installation
============
    
    $ pip install refmanage


Examples
========
View list of files which contain unparseable BibTeX

    $ ref -tv *.bib


License
=======
The code is licensed under the `MIT license <http://opensource.org/licenses/MIT>`_. You can use this code in your project without telling me, but it would be great to hear about who's using the code. You can reach me at joshua.r.smith@gmail.com.


Contributing
============
The repository is hosted on `github <https://github.com/jrsmith3/refmanage>`_ . Feel free to fork this project and/or submit a pull request. Please notify me of any issues using the `issue tracker <https://github.com/jrsmith3/refmanage/issues>`_ .

In the unlikely event that a community forms around this project, please adhere to the `Python Community code of conduct <https://www.python.org/psf/codeofconduct/>`_.

Version numbers follow the `semver <http://semver.org>`_ rubric.


API Reference
=============
.. toctree::
    :maxdepth: 2

    api
