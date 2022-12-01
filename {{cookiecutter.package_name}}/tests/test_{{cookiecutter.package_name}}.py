"""Tests for `{{ cookiecutter.project_name }}` package."""

import unittest

class Test{{ cookiecutter.project_name|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_name }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
    def test_command_line_interface(self):
        """Test the CLI."""
        # TODO: templatize the test for CLI
{%- endif %}