# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from .linkat import (AT_FDCWD, AT_SYMLINK_FOLLOW, AT_EMPTY_PATH,
                     link_at, symlink_at)

from .ffi import get_extension

__all__ = ['get_extension',
           'AT_FDCWD', 'AT_SYMLINK_FOLLOW', 'AT_EMPTY_PATH',
           'link_at', 'symlink_at', ]

__version__ = '1.0.0'
