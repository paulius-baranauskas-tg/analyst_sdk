# tgo_analyst_sdk

## Definition

Most common pyhton functions used in TransferGo analytical scripts.

## Installation

Installation consists of 2 steps: module file creation, and module installation.

To create a module file, in project directory run:

`python setup.py sdist`

This should create a module file under `dist` directory.

To install module then run:
`pip install ./dist/[file with module name].tar.gz`
Note that this file will have version number, thus use `Tab` to complete filename for you.
More info in this [StackOverflow](https://stackoverflow.com/questions/15746675/how-to-write-a-python-module-package) thread.