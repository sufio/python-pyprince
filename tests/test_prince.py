
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
    def input_html_file(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures/input.html')

    @pytest.fixture()
    def output_html_file(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures/out.pdf')

    def test_options(self):
        options = {
            "debug": "",
            "page-size": "A3",
            "style": ["1.css", "2.css"]
        }
        p = Prince(options)
        for arg in p.options:
            assert arg.startswith("--")

    def test_command_args(self):
            options = {
                "debug": "",
                "page-size": "A3",
                "style": ["1.css", "2.css"]
            }
            p = Prince(options)
            commandline_args = p._command_args([], "input html", p.options)
            assert len(commandline_args) == 9

    def test_from_string(self, output_html_file):
        options = {"output": output_html_file}
        p = Prince(options)
        res = p.from_string("Input html")
        assert res == True

    def test_from_file(self, input_html_file):
        options = {"output": input_html_file}
        p = Prince(options)
        res = p.from_file(input_html_file)
        assert res == True
