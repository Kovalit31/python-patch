Library to parse and apply unified diffs.

[![Build Status](https://app.travis-ci.com/Kovalit31/python-patch.svg?branch=master)](https://app.travis-ci.com/github/Kovalit31/python-patch) [![PyPI](https://img.shields.io/pypi/v/patch)](https://pypi.python.org/pypi/patch)

### Features

 * Python 3 compatible # EOL initiated here
 * Automatic correction of
   * Linefeeds according to patched file
   * Diffs broken by stripping trailing whitespace
   * a/ and b/ prefixes
 * Single file, which is a command line tool and a library
 * No dependencies outside Python stdlib
 * Patch format detection (SVN, HG, GIT)
 * Nice diffstat histogram
 * Linux / Windows / OS X
 * Test coverage

Things that don't work out of the box:

 * File renaming, creation and removal
 * Directory tree operations (Partly*)
 * Version control specific properties
 * Non-unified diff formats
* You can use it to patch files in directory with same name of patched ones and add files ("--- /dev/null")

### Usage

Download **patch.py** and run it with Python. It is a self-contained
module without external dependencies.

    patch.py diff.patch

You can also run the .zip file.
    
    python patch-1.16.zip diff.patch

### Installation

**patch.py** is self sufficient. You can copy it into your repository
and use it from here. This setup will always be repeatable. But if
you need to add `patch` module as a dependency, make sure to use strict
specifiers to avoid hitting an API break when version 2 is released:

    pip install "patch==1.*"

## API
patch.fromfile(file) - Load patch from file
patch.fromstring(string) - Load patch from string
patch.ffromuri(uri) - Load patch from uri (need for active internet)

For example:
```
pt = patcher.fromfile("mydiff.patch")
pt.apply()
```

### Other stuff

* [CHANGES](doc/CHANGES.md)
* [LICENSE](doc/LICENSE)
* [CREDITS](doc/CREDITS)

* [test coverage](http://techtonik.github.io/python-patch/tests/coverage/)
