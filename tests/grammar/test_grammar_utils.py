from typing import List

import pytest

from daidepp.grammar.grammar_utils import (
    _find_grammar_key_dependencies,
    create_grammar_from_press_keywords,
)
from daidepp.keywords import *


@pytest.mark.parametrize(
    [
        "keywords",
        "allow_just_arrangement",
        "test_messages",
        "outcomes",
    ],
    [
        (
            ["PRP", "PCE"],
            False,
            ["PRP(PCE (AUS ENG))", "PCE (AUS ENG)"],
            [True, False],
        ),
        (
            ["PCE"],
            True,
            ["PRP(PCE (AUS ENG))", "PCE (AUS ENG)"],
            [False, True],
        ),
        (
            ["PRP", "XDO"],
            False,
            [
                "PRP(XDO((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY))",
                "PRP(XDO((ENG FLT (STP SCS)) SUP (ENG AMY LVP) MTO CLY))",
            ],
            [True, True],
        ),
        (
            ["PRP", "ALY_VSS"],
            False,
            [
                "PRP (ALY (ITA TUR) VSS (ENG RUS))",
                "PRP(XDO((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY))",
            ],
            [True, False],
        ),
        (
            ["PRP", "XDO", "ALY_VSS"],
            False,
            [
                "PRP (ALY (ITA TUR) VSS (ENG RUS))",
                "PRP(XDO((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY))",
            ],
            [True, True],
        ),
        (["PCE", "AND"], False, ["AND (PCE (AUS GER)) (PCE (AUS ENG))"], [True]),
        (
            ["PRP", "PCE", "AND"],
            False,
            ["PRP (AND (PCE (AUS GER)) (PCE (AUS ENG)))"],
            [True],
        ),
        (
            ["XDO", "PCE", "AND"],
            False,
            [
                "AND (PCE (AUS GER)) (PCE (AUS ENG))",
                "AND (XDO ((ENG FLT (STP SCS)) SUP (ENG AMY LVP) MTO CLY)) ((ENG FLT EDI) MTO CLY)",
                "ORR (DRW) (DRW (ENG FRA))",
            ],
            [True, True, False],
        ),
        (
            ["XDO", "PCE", "DRW", "AND", "ORR"],
            True,
            [
                "AND (PCE (AUS GER)) (PCE (AUS ENG))",
                "AND (XDO ((ENG FLT (STP SCS)) SUP (ENG AMY LVP) MTO CLY)) ((ENG FLT EDI) MTO CLY)",
                "ORR (DRW) (DRW (ENG FRA))",
            ],
            [True, True, True],
        ),
        (
            ["XDO", "PCE", "DRW", "AND"],
            True,
            [
                "AND (PCE (AUS GER)) (PCE (AUS ENG))",
                "AND (XDO ((ENG FLT (STP SCS)) SUP (ENG AMY LVP) MTO CLY)) ((ENG FLT EDI) MTO CLY)",
                "ORR (DRW) (DRW (ENG FRA))",
            ],
            [True, True, False],
        ),
        (
            ["ALY_VSS"],
            False,
            [
                "ALY (ITA TUR) VSS (ENG RUS)",
            ],
            [True],
        ),
        (
            [
                "PRP",
                "PCE",
                "ALY_VSS",
                "YES",
                "REJ",
                "XDO",
                "DMZ",
                "AND",
                "NAR",
                "CCL",
                "FCT",
            ],
            False,
            [
                "FCT(PCE (AUS GER))",
                "FCT  (ALY (ITA TUR) VSS (ENG RUS))",
                "FCT (QRY (PCE (AUS GER)))",
                "FCT (NOT (PCE (AUS GER)))",
            ],
            [True, True, False, False],
        ),
    ],
)
def test_create_grammar_from_press_keywords(
    keywords: List[PressKeywords],
    allow_just_arrangement: bool,
    test_messages: List[str],
    outcomes: List[bool],
):
    grammar = create_grammar_from_press_keywords(
        keywords,
        allow_just_arrangement=allow_just_arrangement,
    )
    for message, outcome in list(zip(test_messages, outcomes)):
        if outcome:
            grammar.parse(message)
        else:
            with pytest.raises(Exception):
                grammar.parse(message)
