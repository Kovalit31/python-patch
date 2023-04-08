# Unified patcher

Library to parse and apply unified diffs.

[![Build Status](https://app.travis-ci.com/Kovalit31/python-patch.svg?branch=master)](https://app.travis-ci.com/github/Kovalit31/python-patch)

## Features

* Python 3 compatible # EOL initiated here
* Automatic correction of
  * Linefeeds according to patched file
  * Diffs broken by stripping trailing whitespace
  * a/ and b/ prefixes
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

## Usage

Install  and run it with Python.
Example:

``` bash
python3 -m patcher diff.patch
```

or

```bash
patcher diff.patch
```

For more instructions, run

```bash
python3 -m patcher --help
```

## Installation

You can install from this repository:

```bash
pip install https://github.com/Kovalit31/python-patch
```

After (may be) it will be on PyPI

## API

patch.fromfile(file) - Load patch from file
patch.fromstring(string) - Load patch from string
patch.ffromuri(uri) - Load patch from uri (need for active internet)

For example:

```python
pt = patcher.fromfile("mydiff.patch")
pt.apply()
```

## Other stuff

* [CHANGES](CHANGES.md)
* [LICENSE](LICENSE)
* [CREDITS](CREDITS)

* [test coverage](http://techtonik.github.io/python-patch/tests/coverage/)
