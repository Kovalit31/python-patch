#------------------------------------------------
# Helpers (these could come with Python stdlib)

# x...() function are used to work with paths in
# cross-platform manner - all paths use forward
# slashes even on Windows.

import copy
import posixpath
import re
import os

from . import logger, variables
lg = logger


def xisabs(filename):
    """ Cross-platform version of `os.path.isabs()`
            Returns True if `filename` is absolute on
            Linux, OS X or Windows.
    """
    if filename.startswith(b'/'):     # Linux/Unix
        return True
    elif filename.startswith(b'\\'):  # Windows
        return True
    elif re.match(b'\\w:[\\\\/]', filename): # Windows
        return True
    return False

def xnormpath(path):
    """ Cross-platform version of os.path.normpath """
    # replace escapes and Windows slashes
    normalized = posixpath.normpath(path).replace(b'\\', b'/')
    # fold the result
    return posixpath.normpath(normalized)

def xstrip(filename):
    """ Make relative path out of absolute by stripping
        prefixes used on Linux, OS X and Windows.

        This function is critical for security.
    """
    while xisabs(filename):
        # strip windows drive with all slashes
        if re.match(b'\\w:[\\\\/]', filename):
            filename = re.sub(b'^\\w+:[\\\\/]+', b'', filename)
        # strip all slashes
        elif re.match(b'[\\\\/]', filename):
            filename = re.sub(b'^[\\\\/]+', b'', filename)
    return filename

# --- Utility functions ---
# [ ] reuse more universal pathsplit()
def pathstrip(path, n):
  """ Strip n leading components from the given path """
  pathlist = [path]
  while os.path.dirname(pathlist[0]) != b'':
    pathlist[0:1] = os.path.split(pathlist[0])
  return b'/'.join(pathlist[n:])
# --- /Utility function ---

def normalize_filenames(_items, logger: lg.Log, debugmode=False):
    """ sanitize filenames, normalizing paths, i.e.:
        1. strip a/ and b/ prefixes from GIT and HG style patches
        2. remove all references to parent directories (with warning)
        3. translate any absolute paths to relative (with warning)

        [x] always use forward slashes to be crossplatform
            (diff/patch were born as a unix utility after all)
        
        return None
    """
    warnings = 0
    errors = 0
    items = copy.deepcopy(_items)
    if debugmode:
        logger.debug("normalize filenames")
    for i,p in enumerate(items):
        if debugmode:
            logger.debug("    patch type = " + p.type)
            logger.debug("    source = " +str(p.source))
            logger.debug("    target = " + str(p.target))
        
        source_null = False
        target_null = False
      
        if p.type in (variables.HG, variables.GIT): # Partialy dead!
            # TODO: figure out how to deal with /dev/null entries
            logger.debug("stripping a/ and b/ prefixes")
            if p.source != '/dev/null':
                if not p.source.startswith(b"a/"):
                    logger.warning("invalid source filename")
                else:
                    p.source = p.source[2:]
            if p.target != '/dev/null':
                if not p.target.startswith(b"b/"):
                    logger.warning("invalid target filename")
                else:
                    p.target = p.target[2:]
        if p.source == b'/dev/null':
            print(True)
            source_null = True
        else:
            print(False)
        if p.target == b'/dev/null':
            print(True)
            target_null = True
        else:
            print(False)
        print(p.source, p.target)
        p.source = xnormpath(p.source) if not source_null else b'/dev/null'
        p.target = xnormpath(p.target) if not target_null else b'/dev/null'

        sep = b'/'  # sep value can be hardcoded, but it looks nice this way

        # references to parent are not allowed
        if p.source.startswith(b".." + sep) and not source_null:
            logger.warning("error: stripping parent path for source file patch no.%d" % (i+1))
            warnings += 1
            while p.source.startswith(b".." + sep):
                p.source = p.source.partition(sep)[2]
        if p.target.startswith(b".." + sep) and not target_null:
            logger.warning("error: stripping parent path for target file patch no.%d" % (i+1))
            warnings += 1
            while p.target.startswith(b".." + sep):
                p.target = p.target.partition(sep)[2]
        # absolute paths are not allowed
        if xisabs(p.source) or xisabs(p.target):
            logger.warning("error: absolute paths are not allowed - file no.%d" % (i+1))
            warnings += 1
        if xisabs(p.source) and not source_null:
            logger.warning("stripping absolute path from source name '%s'" % p.source)
            p.source = xstrip(p.source)
            warnings += 1
        if xisabs(p.target) and not target_null:
            logger.warning("stripping absolute path from target name '%s'" % p.target)
            p.target = xstrip(p.target)
            warnings += 1
    
        items[i].source = p.source
        items[i].target = p.target
    return errors, warnings, items