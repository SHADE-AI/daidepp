from typing import List

import pytest

from daidepp.daide_visitor import daide_visitor
from daidepp.grammar import create_daide_grammar
from daidepp.keywords import *

grammar = create_daide_grammar(level=130, string_type="all")


def test_basic_visitor(sample_daide_messages: List[str]):
    for message in sample_daide_messages:
        tree = grammar.parse(message)
        daide_visitor.visit(tree)

    assert True


@pytest.mark.parametrize(
    ["daide_message", "expected_type"],
    [
        ("PCE(AUS GER)", PCE),
        ("PRP(PCE(AUS GER))", PRP),
        ("FRA FLT APU", Unit),
        ("HUH ( PRP ( PCE ( AUS ENG ) ) )", HUH),
        ("FCT ( NOT ( PCE ( AUS ENG ) ) )", FCT),
        ("FRM ( AUS ) ( GER FRA ) ( PRP ( PCE ( AUS ENG ) ) )", FRM),
        ("XDO ( ( AUS FLT ALB ) HLD )", XDO),
    ],
)
def test_visitor_objects(daide_message: str, expected_type: AnyDAIDEToken):
    tree = grammar.parse(daide_message)
    daide_object = daide_visitor.visit(tree)
    assert isinstance(daide_object, expected_type)
