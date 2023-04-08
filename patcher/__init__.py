"""
    Patch utility to apply unified diffs

    Brute-force line-by-line non-recursive parsing 

    Copyright (c) 2008-2016 anatoly techtonik
                  2023 Kovalit31
    Available under the terms of MIT license

    Original: https://github.com/techtonik/python-patch/
    Newer: https://github.com/Kovalit31/python-patch
"""

from io import StringIO

import urllib
from . import utils

#-----------------------------------------------
# Main API functions

logger = utils.logger.Log(logging_name=__name__)

def fromfile(filename):
  """ Parse patch file. If successful, returns
      PatchSet() object. Otherwise returns False.
  """
  patchset = utils.patch.PatchSet()
  logger.debug("reading %s" % filename)
  fp = open(filename, "rb")
  res = patchset.parse(fp)
  fp.close()
  if res == True:
    return patchset
  return False


def fromstring(s):
  """ Parse text string and return PatchSet()
      object (or False if parsing fails)
  """
  ps = utils.patch.PatchSet(StringIO(s))
  if ps.errors == 0:
    return ps
  return False


def fromurl(url):
  """ Parse patch from an URL, return False
      if an error occured. Note that this also
      can throw urlopen() exceptions.
  """
  ps = utils.patch.PatchSet(urllib.request.urlopen(url))
  if ps.errors == 0:
    return ps
  return False

# /API