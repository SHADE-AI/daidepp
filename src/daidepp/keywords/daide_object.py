from abc import ABC, abstractmethod
from dataclasses import dataclass

from daidepp.grammar import create_daide_grammar
from daidepp.grammar.grammar import MAX_DAIDE_LEVEL

_grammar = create_daide_grammar(MAX_DAIDE_LEVEL, string_type="all")


@dataclass(eq=True, frozen=True)
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
            ) from e
