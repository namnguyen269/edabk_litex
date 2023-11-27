/*
 * Copyright (c) 1990 The Regents of the University of California.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms are permitted
 * provided that the above copyright notice and this paragraph are
 * duplicated in all such forms and that any documentation,
 * and/or other materials related to such
 * distribution and use acknowledge that the software was developed
 * by the University of California, Berkeley.  The name of the
 * University may not be used to endorse or promote products derived
 * from this software without specific prior written permission.
 * THIS SOFTWARE IS PROVIDED ``AS IS'' AND WITHOUT ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
 */
/* doc in swprintf.c */

#define _DEFAULT_SOURCE
#include <_ansi.h>
#include <stdio.h>
#include <wchar.h>
#include <stdarg.h>
#include "local.h"

int
_wprintf_r (struct _reent *ptr,
       const wchar_t *fmt, ...)
{
  int ret;
  va_list ap;

  _REENT_SMALL_CHECK_INIT (ptr);
  va_start (ap, fmt);
  ret = _vfwprintf_r (ptr, _stdout_r (ptr), fmt, ap);
  va_end (ap);
  return ret;
}

#ifndef _REENT_ONLY

int
wprintf (const wchar_t *__restrict fmt, ...)
{
  int ret;
  va_list ap;
  struct _reent *ptr = _REENT;

  _REENT_SMALL_CHECK_INIT (ptr);
  va_start (ap, fmt);
  ret = _vfwprintf_r (ptr, _stdout_r (ptr), fmt, ap);
  va_end (ap);
  return ret;
}

#endif /* ! _REENT_ONLY */
