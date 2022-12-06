from abc import ABC, abstractmethod
from dataclasses import dataclass

from daidepp.grammar import create_daide_grammar

_grammar = create_daide_grammar(130, string_type="all")


@dataclass
class _DAIDEObject(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    def __post_init__(self):
        try:
            _grammar.parse(str(self))
        except Exception as e:
            raise Exception(
                f"Incorrect values passed, object is not valid DAIDE. Received '{str(self)}'"
            )