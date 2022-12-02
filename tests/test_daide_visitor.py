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
    # fmt: off
    ["daide_message", "expected_type"],
    [
        ("PCE(AUS GER)", PCE),
        ("PRP(PCE(AUS GER))", PRP),
        ("FRA FLT APU", Unit),
        ("HUH ( PRP ( PCE ( AUS ENG ) ) )", HUH),
        ("FCT ( NOT ( PCE ( AUS ENG ) ) )", FCT),
        ("FRM ( AUS ) ( GER FRA ) ( PRP ( PCE ( AUS ENG ) ) )", FRM),
        ("XDO ( ( AUS FLT ALB ) HLD )", XDO),
        ("ALY ( GER AUS) VSS (ENG FRA)", ALYVSS),
        ("( ENG AMY LVP) HLD", HLD),
        ("( ENG AMY LVP) MTO YOR", MTO),
        ("( FRA AMY CON ) SUP ( TUR AMY BUL)", SUP),
        ("( FRA FLT ECH ) CVY ( FRA AMY BEL ) CTO YOR", CVY),
        ("(ENG AMY YOR) CTO NWY VIA (NTH)", MoveByCVY),
        ("DRW ( ENG FRA)", DRW),
        ("REJ ( PRP (PCE (ENG FRA ) ) )", REJ),
        ("BWX ( PRP (PCE ( ENG FRA ) ) )", BWX),
    ],
    # fmt: on
)
def test_visitor_objects(daide_message: str, expected_type: AnyDAIDEToken):
    tree = grammar.parse(daide_message)
    daide_object = daide_visitor.visit(tree)
    assert isinstance(daide_object, expected_type)
