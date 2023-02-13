from abc import ABC, abstractmethod
from dataclasses import dataclass

from typing_extensions import get_args

from daidepp.grammar import create_daide_grammar
from daidepp.grammar.grammar import DAIDELevel

_grammar = create_daide_grammar(get_args(DAIDELevel)[-1], string_type="all")


@dataclass
class _DAIDEObject(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    def __post_init__(self):
        try:
            _grammar.parse(str(self))
        except Exception as e:
            raise ValueError(
                f"Incorrect values passed, object is not valid DAIDE. Received '{str(self)}'"
            )
