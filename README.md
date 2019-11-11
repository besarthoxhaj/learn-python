## Start the project

Clone the repo

```
make install
source env/bin/activate
```

And you are ready to go!

## General

Use `pyenv` to manage multiple versions https://github.com/pyenv/pyenv

```sh
brew update
brew install pyenv
pyenv init
# will suggest to add `eval "$(pyenv init -)"`
# at the end of the current `.bash_profile`
pyenv install 3.8.0
pyenv install 2.7.17
pyenv global 3.8.0
pyenv versions
#   system
#   2.7.8
# * 3.8.0 (set by /Users/besartshyti/.pyenv/version)
python -V
# Python 3.8.0
pip -V
# pip 19.2.3 from
# /Users/besartshyti/.pyenv
# /versions/3.8.0/lib/python3.8/site-packages/pip (python 3.8)
```

## Goals to learn python

In order to understand a programming language I need to know:

- how to `print` stuff
- reserved words
- how to run code in one file
- how to import/require other files aka [module system](https://docs.python.org/2.7/tutorial/modules.html)
- scopes
- how to create a simple server
- [coding style](https://www.python.org/dev/peps/pep-0008/)
- how to use external dependencies

All of it can be found at [https://docs.python.org/2.7/tutorial/](https://docs.python.org/2.7/tutorial/)

## print

In Python 2.x `print` is actually a special statement and not a function.

## modules

```py
#

```

## `pip` and `virtualenv`

Basically `npm` and `node_modules`. Start by installing `pip`. I did it manually
following the instructions on [pip website](https://pip.pypa.io/en/stable/installing/).
However someone suggested also `sudo easy_install pip` (haven't tried it though).

After `pip` let's install virtualenv with `sudo pip install virtualenv`. Once
that finished you can create a new virtual environment with `virtualenv env`.
This will install a specific python and pip version. This virtual environment is
basically a directory.

To run or activate the local python and pip binaries use `source env/bin/activate`.
To deactivate them just type `deactivate`.

For more info read [this useful tutorial](https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/).

When installing a new package run `pip freeze > requirements.txt`,
sort of `npm install <name> --save`.

## testing

Use `pytest` https://github.com/pytest-dev/pytest

```sh
pip install pytest
# run tests on a single file
pytest [file]
# or simply to look for golabl configs
pytest
# for watch mode
pip install pytest-watch
# run
ptw
# to run only affected tests
pip install pytest-testmon
# run with
ptw --runner "pytest --testmon"
# to print
pytest -s
```

Pytest will recursively look for `test_*.py` or `*_test.py`. Inside those files
will collect `test` prefixed functions.

For more info check:
  - https://docs.pytest.org/en/latest/goodpractices.html#test-discovery
  - https://github.com/joeyespo/pytest-watch
  - https://github.com/tarpas/pytest-testmon
  - https://stackoverflow.com/q/43162722
  - https://stackoverflow.com/q/8658043
  - https://stackoverflow.com/q/24617397

## lint and prettify

Use `yapf` https://github.com/google/yapf

```sh
pip install yapf
yapf lint_prettify/messy.py
# output prettified file with default style (google)
yapf lint_prettify/messy.py --style chromium
# or
yapf --in-place lint_prettify/messy.py
# or
yapf --in-place --recursive lint_prettify
```

Use `pylint` https://github.com/PyCQA/pylint

```sh
pip install pylint
pylint lint_prettify
```

## scientific packages

http://www.lowindata.com/2013/installing-scientific-python-on-mac-os-x/
