## Learn python my way

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

### print
In Python 2.x `print` is actually a special statement and not a function.

### module system

### `pip` and `virtualenv`

Basically `npm` and `node_modules`. Start by installing `pip`. I did it manually following the instructions on [pip website](https://pip.pypa.io/en/stable/installing/). However someone suggested also `sudo easy_install pip` (haven't tried it though).

After `pip` let's install virtualenv with `sudo pip install virtualenv`. Once that finished you can create a new virtual environment with `virtualenv env`. This will install a specific python and pip version. This virtual environment is basically a directory.

To run or activate the local python and pip binaries use `source env/bin/activate`. To deactivate them just type `deactivate`.

For more info read [this useful tutorial](https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/).

### virtualenv vs virtualenvwrapper



### scientific packages
