
from daidepp.daide_visitor import daide_visitor
from daidepp.grammar import create_daide_grammar
from daidepp.keywords import *

try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

__version__ = version("daidepp")
