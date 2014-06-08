#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import io
import re

from setuptools import setup, find_packages
import linkat



def _read_version():
    with io.open('linkat/__init__.py', encoding='utf-8') as module_stream:
        return re.search(r'''__version__ = ['"](?P<version>[\d.]+)['"]''',
                         module_stream.read()).group('version')


def _read_long_description():
    with io.open('README.rst', encoding='utf-8') as ld_stream:
        return ld_stream.read()


setup(name='linkat',
      version=_read_version(),
      description=('Python support for the POSIX/Linux'
                   ' functions linkat and symlinkat.'),
      long_description=_read_long_description(),
      author='eisenlaub',
      author_email='eisenlaub@fea.st',
      url='https://github.com/eisenlaub/python-linkat',
      license='MIT License',
      packages=find_packages(),
      setup_requires=('cffi', ),
      install_requires=('cffi', ),
      zip_safe=False,
      ext_package='linkat',
      ext_modules=[linkat.get_extension(), ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Filesystems',
      ])
