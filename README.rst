Usage
-----

You can specify all pyprince `options <http://www.princexml.com/doc/command-line/#idp47329832745904>_.` You can drop '--' in option name.
If option is without value use None or False:

.. code-block:: python

    import pyprince

    options = {
        "page-size": "A3",
        "output": "./output.pdf",
        "style": "./styles.css"
    }

    p = pyprince.Prince(options)

    p.from_string("Hello")
    p.from_file("./input.html")

    # Override options

    extra_options = {
        "page-size": "A4",
        "debug": None
    }

    p.from_string("Hello", extra_options)
    p.from_file("./input.html", extra_options)


You can read it to a variable

.. code-block:: python

        # From pyprince documentation:
        # The output file name can be specified on the command line using
        # the --output command line option.
        # An output filename consisting of a single hyphen "-" will
        # cause pyprince to write to the standard output stream.

        import pyprince

        p = pyprince.Prince()

        options = {"output": "-"}
        pdf = p.from_file("./input.html", options)


    


