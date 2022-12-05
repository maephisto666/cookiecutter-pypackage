# -*- coding: utf-8 -*-
"""Main module."""

{%- if cookiecutter.command_line_interface|lower == "argparse" %}
import argparse
{%- endif %}
import logging
import logging.config
import sys

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
    },
    "handlers": {
        "default": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["default"],
            "level": "WARN",
            "propagate": False,
        },
        "{{cookiecutter.package_name}}": {
            "handlers": ["default"],
            "level": "WARN",
            "propagate": False,
        },
    },
}

logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger("{{cookiecutter.package_name}}.__main__")


def main({%- if cookiecutter.command_line_interface|lower == "argparse" %}argv: list[str] = None{%- endif %}) -> None:
    # TODO: default options for argparse (e.g. --verbose)
    ...
    
if __name__ == "__main__":
    sys.exit(main())
