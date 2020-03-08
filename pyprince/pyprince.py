# -*- coding: utf-8 -*-

import copy
import logging
import subprocess

logger = logging.getLogger('pyprince')


class Prince(object):
    def __init__(self, prince_bin, options=None):
        self.prince_bin = prince_bin
        self.options = self._prepare_options(options)

        # if output is not specified use standard output by default
        if "--output" not in self.options:
            self.options["--output"] = "-"

    def _prepare_options(self, options):
        """
        Make options usable for command line
        """
        _options = {}

        if not options:
            return _options

        for key in options:
            normalized_key = key

            if not key.startswith("--"):
                normalized_key = "--%s" % key

            normalized_key = normalized_key.lower()

            _options[normalized_key] = options[key]

        return _options

    def _command_args(self, files, input_data, options):
        """
        Prepare command line arguments
        """
        args = [self.prince_bin]

        # Specifying input
        # The command line must contain the name of the input file to process.
        # An input filename consisting of a single hyphen "-" will
        # cause Prince to read from the standard input stream.

        if input_data:
            args.append("-")

        if files:
            args.extend(files)

        for key, arg in options.items():

            # None, False and '' args
            if not arg:
                args.append(key)
                continue

            # multiple args FILES, STYLESHEETS ...
            if isinstance(arg, list):
                for a in arg:
                    args.extend([key, a])
            else:
                args.extend([key, arg])

        return args

    def _is_stdout(self, options):
        # Specifying output
        # The output file name can be specified on the command line using
        # the --output command line option.
        # An output filename consisting of a single hyphen "-" will
        # cause Prince to write to the standard output stream.
        return options["--output"] == "-"

    def _to_pdf(self, files=None, input_data=None, extra_options=None):
        options = copy.copy(self.options)
        if extra_options:
            options.update(self._prepare_options(extra_options))

        args = self._command_args(files, input_data, options)

        logger.debug(' '.join(args))

        result = subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if input_data and not isinstance(input_data, bytes):
            input_data = input_data.encode("utf-8")
        stdout, stderr = result.communicate(input=input_data)

        if result.returncode != 0:
            # not ok
            raise Exception(stderr)

        # ok
        if self._is_stdout(options):
            return stdout

        return True

    # public API
    def from_string(self, input_data, options=None):
        return self._to_pdf(input_data=input_data, extra_options=options)

    def from_file(self, files, options=None):
        if not isinstance(files, list):
            files = [files]
        return self._to_pdf(files=files, extra_options=options)
