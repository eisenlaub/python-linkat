# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import os

from linkat.ffi import ffi, ffi_lib


AT_FDCWD = ffi_lib.AT_FDCWD
if ffi_lib.AT_SYMLINK_FOLLOW != 0:
    AT_SYMLINK_FOLLOW = ffi_lib.AT_SYMLINK_FOLLOW
if ffi_lib.AT_EMPTY_PATH != 0:
    AT_EMPTY_PATH = ffi_lib.AT_EMPTY_PATH


def link_at(old_dir_fd, old_path, new_dir_fd, new_path, flags=0):
    """
    The linkat() system call operates in exactly the  same  way  as
    link(), except for the differences described here.

    If the pathname given in oldpath is relative, then it is inter‐
    preted relative to  the  directory  referred  to  by  the  file
    descriptor  olddirfd (rather than relative to the current work‐
    ing directory of the calling process, as is done by link()  for
    a relative pathname).

    If  oldpath  is  relative  and  olddirfd  is  the special value
    AT_FDCWD, then oldpath is interpreted relative to  the  current
    working directory of the calling process (like link()).

    If oldpath is absolute, then olddirfd is ignored.

    The  interpretation of newpath is as for oldpath, except that a
    relative pathname is  interpreted  relative  to  the  directory
    referred to by the file descriptor newdirfd.

    The following values can be bitwise ORed in flags:

    AT_EMPTY_PATH (since Linux 2.6.39)
           If oldpath is an empty string, create a link to the file
           referenced by olddirfd (which  may  have  been  obtained
           using  the open(2) O_PATH flag).  In this case, olddirfd
           can refer to any type of file,  not  just  a  directory.
           This  will  generally  not  work  if the file has a link
           count of zero (files created with O_TMPFILE and  without
           O_EXCL  are  an  exception).   The  caller must have the
           CAP_DAC_READ_SEARCH capability  in  order  to  use  this
           flag.   This  flag is Linux-specific; define _GNU_SOURCE
           to obtain its definition.

    AT_SYMLINK_FOLLOW (since Linux 2.6.18)
           By default, linkat(), does not dereference oldpath if it
           is  a  symbolic  link  (like  link()).  The flag AT_SYM‐
           LINK_FOLLOW can be specified in flags to  cause  oldpath
           to  be dereferenced if it is a symbolic link.  If procfs
           is mounted, this  can  be  used  as  an  alternative  to
           AT_EMPTY_PATH, like this:

               linkat(AT_FDCWD, "/proc/self/fd/<fd>", newdirfd,
                      newname, AT_SYMLINK_FOLLOW);

    :type old_dir_fd: int
    :type old_path: str
    :type new_dir_fd: int
    :type new_path: int
    :type flags: int
    """
    out = ffi_lib.linkat(old_dir_fd, old_path, new_dir_fd, new_path, flags)
    if out == -1:
        raise OSError(ffi.errno, os.strerror(ffi.errno))
    return out


def symlink_at(target, new_dir_fd, link_path):
    """
    The symlinkat() system call operates in exactly the same way as
    symlink(), except for the differences described here.

    If  the  pathname  given  in  linkpath  is relative, then it is
    interpreted relative to the directory referred to by  the  file
    descriptor  newdirfd (rather than relative to the current work‐
    ing directory of the calling process, as is done  by  symlink()
    for a relative pathname).

    If  linkpath  is  relative  and  newdirfd  is the special value
    AT_FDCWD, then linkpath is interpreted relative to the  current
    working directory of the calling process (like symlink()).

    If linkpath is absolute, then newdirfd is ignored.

    :type target: str
    :type new_dir_fd: int
    :type link_path: str
    """
    out = ffi_lib.symlinkat(target, new_dir_fd, link_path)
    if out == -1:
        raise OSError(ffi.errno, os.strerror(ffi.errno))
    return out
