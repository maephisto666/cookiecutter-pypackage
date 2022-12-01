"""Main module."""

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys

# TODO: default options for logging


def main() -> None:
    # TODO: default options for argparse (e.g. --verbose)
    ...
    
if __name__ == '__main__':
    sys.exit(main())
