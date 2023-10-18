.. image:: https://github.com/phx-nz/py-tty-day-1/actions/workflows/build.yml/badge.svg
   :target: https://github.com/phx-nz/py-tty-day-1/actions/workflows/build.yml

Boilerplate
===========
Katas for Python Tech Transformation Workshop day 1.

Your goal is to make all the tests in
`./test/test_inspections.py <./test/test_inspections>` pass.

The corresponding code is in `./kata/inspections.py <./kata/inspections.py>`.

Installation
------------
Install development dependencies via pipenv::

   pipenv install -e .

If pipenv is not installed, try this instead::

   # Create virtualenv
   python -m venv venv

   # Activate virtualenv
   . ./venv/bin/activate

   # Ensure pip and pipenv are up-to-date
   pip install --upgrade pip pipenv

   # Install project dependencies
   pipenv install -e .

Running Unit Tests
------------------
To run the unit tests::

   pytest

If the above command doesn't work, try ``python -m pytest`` instead.
