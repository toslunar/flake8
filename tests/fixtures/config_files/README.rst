About this directory
====================

The files in this directory are test fixtures for unit and integration tests.
Their purpose is described below. Please note the list of file names that can
not be created as they are already used by tests.

New fixtures are preferred over updating existing features unless existing
tests will fail.

Files that should not be created
--------------------------------

- ``tests/fixtures/config_files/missing.ini``

Purposes of existing fixtures
-----------------------------

``tests/fixtures/config_files/local-plugin.ini``

    This is for testing configuring a plugin via flake8 config file instead of
    setuptools entry-point.
