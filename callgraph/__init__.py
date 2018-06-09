"""This package defines decorators and IPython magic to display a dynamic call graph."""

__version__ = '1.0.0'
__all__ = ['load_ipython_extension', 'decorator', 'CallGraphRecorder']

from .extension import load_ipython_extension
from .decorator import decorator
from .recorder import CallGraphRecorder
