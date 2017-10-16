************
Installation
************

Prerequisites
=============

pip and setuptools
------------------

Make sure you have the latest versions of `pip
<https://pip.pypa.io/en/stable/>`_ and `setuptools
<https://bitbucket.org/pypa/setuptools>`_  installed.

::

    $ pip --version

.. note::

    The package managers of most Linux/Unix distributions usually use outdated
    versions of :program:`pip`. Please uninstall the package providing
    :program:`pip` (usually it's named ``python-pip``) and :ref:`reinstall it
    using the bootstrap script <pip_bootstrap_script>`.

Install/upgrade pip using ensurepip
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have Python 3.4 (or newer) or Python 2.7.9 (or newer) installed you can
use `ensurepip <https://docs.python.org/3/library/ensurepip.html>`_ to install
or upgrade :program:`pip`:

::

    $ python -m ensurepip --upgrade

If your Python version is too old you will simply see an error message like
that:

::

    $ python -m ensurepip --upgrade
    /usr/bin/python: No module named ensurepip

In this case :ref:`reinstall it using the bootstrap script
<pip_bootstrap_script>`.

.. _pip_bootstrap_script:

Install/upgrade pip using the bootstrap script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:program:`pip` can be installed with the help from a `bootstrap script
<https://bootstrap.pypa.io/get-pip.py>`_. If :program:`curl` is installed, you
can use it to download :program:`pip` at the command line. Otherwise just use
the browser.

::

    $ curl -O https://bootstrap.pypa.io/get-pip.py

When the bootstrap script has been downloaded execute it to install
:program:`pip`:

::

    $ python get-pip.py

virtualenvwrapper
-----------------

Make sure you have installed the latest version of `virtualenvwrapper
<https://virtualenvwrapper.readthedocs.org/>`_. You can use :program:`pip` to
either install or upgrade it:

::

    $ pip install -U virtualenvwrapper

.. note::

    If you installed :program:`virtualenvwrapper` for the first time, take your
    time to read the installation documentation.

pyenv
-----

This project will be tested with different Python versions. You should install
`pyenv <https://github.com/yyuu/pyenv>`_ to make the installation of different
Python versions as easy as possible.

Also install `pyenv-virtualenvwrapper <https://github.com/yyuu/pyenv-
virtualenvwrapper>`_, a :program:`pyenv` plugin which provides a
:program:`pyenv virtualenvwrapper` command to manage your virtualenvs with
virtualenvwrapper.

After you have installed and configured :program:`pyenv` and the plugin you can
use the following command in the root of the project to configure the Python
versions to use:

::

    $ pyenv local 3.4.3 2.7.9

.. note::

    You first have to install the Python versions you want to use using
    :program:`pyenv install`. :program:`pyenv install -l` lists all available
    versions.

    The first version passed to :program:`pyenv local` will be the main version
    used for the project.

EditorConfig
------------

`EditorConfig <http://editorconfig.org/>`_ helps developers define and maintain
consistent coding styles between different editors and IDEs. `Download a plugin
<http://editorconfig.org/#download>`_ for your favourite editor to enable it to
read the file format and adhere to the defined styles.

Development Setup
=================

Git 
----------------

Clone the repository using `Git <https://git-scm.com/>`_:

::

    $ git clone git@github.com:bocian67/dezentrale_web.git

Then change into the cloned repository:

::

    $ cd dezentrale_web


Install Python packages
-----------------------

First create a new virtualenv for the project using virtualenvwrapper:

::

    $ mkvirtualenv -a `pwd` dezentrale_web

Now you can install the packages for development:

::

    $ make develop

You should run this command every time a requirement changes to update your
development environment.

Create the database
-------------------

Now it's the time to create the database tables:

::

    $ make migrate

And to create a new Django superuser:

::

    $ envdir envs/dev/ python manage.py createsuperuser

Start the development webserver
-------------------------------

Finally start the development webserver:

::

    $ make runserver

To see the other targets available in the :file:`Makefile` simply run:

::

    $ make
