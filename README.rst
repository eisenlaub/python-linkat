python-linkat
=============

.. image:: https://pypip.in/version/linkat/badge.png
    :target: https://pypi.python.org/pypi/linkat/
    :alt: Latest Version

.. image:: https://pypip.in/license/linkat/badge.png
    :target: https://pypi.python.org/pypi/linkat/
    :alt: License

The single purpose of `python-linkat`_ is to provide python developers with
the ability to use the system native functions ``linkat`` and ``symlinkat``.
The Library is written in plain python and utilizes `cffi`_ to call native 
system functions and therefore depends on it.


Documentation
-------------

This module provides only the 2 functions  ``linkat`` and ``symlinkat``
and their constants which can be used as arguments for the ``flag`` parameter.
For a more detailed documentation please look at the corresponding linux
man pages for `linkat`_ and `symlinkat`_. If there was an error during 
the system call, ``OSError`` with the corresponding error code will be raised.


Installation
------------
The package is available on `PyPI`_ and thus it can be installed with pip:

::

  $ pip install linkat


.. _python-linkat: https://github.com/eisenlaub/python-linkat
.. _PyPI: https://pypi.python.org/pypi/linkat/
.. _cffi: https://cffi.readthedocs.org/
.. _linkat: http://man7.org/linux/man-pages/man2/link.2.html
.. _symlinkat: http://man7.org/linux/man-pages/man2/symlink.2.html
