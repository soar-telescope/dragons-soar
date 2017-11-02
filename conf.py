"""

    Configuration File for SPHINX

    This file is created simply to add Markdown to the available languages for documentation.

"""

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

