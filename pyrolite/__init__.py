import sys
import logging
from ._version import get_versions
from .plot import pyroplot

__version__ = get_versions()["version"]
del get_versions

# http://docs.python-guide.org/en/latest/writing/logging/
logging.getLogger(__name__).addHandler(logging.NullHandler())
logging.captureWarnings(True)

__all__ = ['plot', 'comp', 'geochem', 'mineral', 'util']
