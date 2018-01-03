"""Decorators and Jupyter IPython magic to display a dynamic call graph."""

__version__ = '0.1.2'

from .extension import load_ipython_extension
from .decorator import decorator
from .recorder import CallGraphRecorder
