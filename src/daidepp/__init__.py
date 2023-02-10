from daidepp.grammar import *
from daidepp.keywords import *
from daidepp.visitor import *

try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

__version__ = version("daidepp")
