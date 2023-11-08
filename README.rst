.. image:: https://github.com/phx-nz/py-tty-day-1/actions/workflows/build.yml/badge.svg
   :target: https://github.com/phx-nz/py-tty-day-1/actions/workflows/build.yml

Boilerplate
===========
Katas for Python Tech Transformation Workshop day 1.

Your goal is to make all the tests in the `test directory <./test>` pass.

The corresponding code is in `kata/__init__.py <./kata/__init__.py>`.

Installation
------------
Install development dependencies via pipenv::

   pipenv install --dev

If pipenv is not installed, try this instead::

   # Create virtualenv
   python -m venv venv

   # Activate virtualenv
   . ./venv/bin/activate

   # Ensure pip and pipenv are up-to-date
   pip install --upgrade pip pipenv

   # Install project dependencies
   pipenv install --dev

Automatic code quality checks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
After installing dependencies, run the following command to install git hooks
to automatically check code quality before allowing commits::

   pipenv run autohooks activate --mode pipenv

Checking code quality
---------------------
You can manually run code quality checks with the following commands::

   # Check formatting:
   pipenv run black [file ...]

   # Linting (run both for best coverage):
   pipenv run pylint [file ...]
   pipenv run ruff check --fix [file ...]

Running Unit Tests
------------------
To run the unit tests::

   pipenv run pytest

By default this will run all of the tests.  If you just want to run specific tests, you
can provide them as arguments, e.g.::

   pipenv run pytest test/test_get_dict_item.py

See `how to invoke pytest <https://docs.pytest.org/en/7.4.x/how-to/usage.html>`_ for
more information.
