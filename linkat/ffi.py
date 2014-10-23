# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from cffi import FFI

ffi = FFI()

ffi.cdef("""
#define AT_FDCWD ...
#define AT_SYMLINK_FOLLOW ...
#define AT_EMPTY_PATH ...

int linkat(int olddirfd, const char *oldpath,
           int newdirfd, const char *newpath, int flags);

int symlinkat(const char *target, int newdirfd, const char *linkpath);
""")

ffi_lib = ffi.verify("""
#include <fcntl.h>
#include <unistd.h>
#ifndef AT_SYMLINK_FOLLOW
#  define AT_SYMLINK_FOLLOW 0
#endif
#ifndef AT_EMPTY_PATH
#  define AT_EMPTY_PATH 0
#endif
""",  ext_package='linkat')


def get_extension():
    return ffi.verifier.get_extension()
