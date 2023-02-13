from daidepp.grammar import (
    DAIDEGrammar,
    create_daide_grammar,
    create_grammar_from_press_keywords,
)
from daidepp.keywords import *
from daidepp.visitor import DAIDEVisitor, daide_visitor

try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

__version__ = version("daidepp")
__ben__ = 'was here'
