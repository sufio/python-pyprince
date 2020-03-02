python-pyprince
===============

.. image:: https://img.shields.io/pypi/v/pyprince.svg
    :target: https://pypi.python.org/pypi/pyprince/

A simple Python wrapper for the PrinceXML PDF generation library

Installation
------------

Prince XML
~~~~~~~~~~

Prince XML `installation guide <http://www.princexml.com/doc/installing/>`_.

python-pyprince
~~~~~~~~~~~~~~~

.. code-block::

    $ pip install pyprince

Usage
-----

Path to prince binary must be set using the `prince_bin` param:

.. code-block:: python

    import pyprince

    p = pyprince.Prince(prince_bin='/usr/local/bin/prince')

You can specify all Prince XML `options <http://www.princexml.com/doc/command-line/#idp47329832745904>`_. You can drop '--' in option name.
If option is without value use None or False:

.. code-block:: python

    import pyprince

    options = {
        "page-size": "A3",
        "output": "./output.pdf",
        "style": "./styles.css"
    }

    p = pyprince.Prince(prince_bin='/usr/local/bin/prince', options=options)

    p.from_string("Hello")
    p.from_file("./input.html")

    # pass a list with multiple files
    p.from_file(["./input1.html", "./input2.html"])

    # Override options

    extra_options = {
        "page-size": "A4",
        "debug": None
    }

    p.from_string("Hello", extra_options)
    p.from_file("./input.html", extra_options)


You can read it to a variable:

.. code-block:: python

        # From Prince documentation:
        # The output file name can be specified on the command line using
        # the --output command line option.
        # An output filename consisting of a single hyphen "-" will
        # cause pyprince to write to the standard output stream.

        import pyprince

        p = pyprince.Prince(prince_bin='/usr/local/bin/prince')

        options = {"output": "-"}
        pdf = p.from_file("./input.html", options)


This library is maintained by `Sufio - Professional Invoices <https://sufio.com?-h>`_.
