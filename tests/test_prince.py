import os
import sys

sys.path.insert(
    0,
    os.path.realpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
)

from pyprince import Prince
import pytest


class TestPrince(object):
    @pytest.fixture()
    def prince_bin(self):
        return 'prince'

    @pytest.fixture()
    def input_html_file(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures/input.html')

    @pytest.fixture()
    def output_html_file(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures/out.pdf')

    def test_options(self, prince_bin):
        options = {
            "debug": "",
            "page-size": "A3",
            "style": ["1.css", "2.css"]
        }
        p = Prince(prince_bin=prince_bin, options=options)
        for arg in p.options:
            assert arg.startswith("--")

    def test_command_args(self, prince_bin):
        options = {
            "debug": "",
            "page-size": "A3",
            "style": ["1.css", "2.css"],
            "output": "-"
        }
        p = Prince(prince_bin=prince_bin, options=options)
        commandline_args = p._command_args([], "input html", p.options)
        assert len(commandline_args) == 11

    def test_from_string_unicode(self, prince_bin, output_html_file):
        options = {"output": output_html_file}
        p = Prince(prince_bin=prince_bin, options=options)
        res = p.from_string(u"Input html")
        assert res is True

    def test_from_string_bytes(self, prince_bin, output_html_file):
        options = {"output": output_html_file}
        p = Prince(prince_bin=prince_bin, options=options)
        res = p.from_string(b"Input html")
        assert res is True

    def test_from_file(self, prince_bin, output_html_file, input_html_file):
        options = {"output": output_html_file}
        p = Prince(prince_bin=prince_bin, options=options)
        res = p.from_file(input_html_file)
        assert res is True

    def test_output(self, prince_bin):
        p = Prince(prince_bin=prince_bin, )
        assert p.options["--output"] == "-"

    def test_error_handler(self, prince_bin):
        p = Prince(prince_bin=prince_bin)
        with pytest.raises(Exception):
            p.from_file("./does_not_exist.html")
