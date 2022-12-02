import pytest

from daidepp.grammar.grammar_utils import (
    _find_grammar_key_dependencies,
    create_grammar_from_press_keywords,
)
from daidepp.keywords import *


@pytest.mark.parametrize("grammar", [130], indirect=True)
@pytest.mark.parametrize(
    # fmt: off
    ["keyword", "include_level_0", "expected_output"], 
    [
        (["POB"], True, ['arrangement', 'bld', 'build', 'coast', 'cvy', 'dsb', 'fct', 'hld', 'ins', 'lpar', 'move_by_cvy', 'mto', 'not', 'order', 'pob', 'power', 'prov_coast', 'prov_land_sea', 'prov_landlock', 'prov_no_coast', 'prov_sea', 'province', 'prp', 'qry', 'rem', 'retreat', 'rpar', 'rto', 'season', 'sup', 'supply_center', 'thk', 'turn', 'unit', 'unit_type', 'why', 'why_param', 'ws', 'wve']),
        (["POB"], False, ['arrangement', 'fct', 'ins', 'lpar', 'not', 'pob', 'prp', 'qry', 'rpar', 'thk', 'why', 'why_param']),
        ([POB], True, ['arrangement', 'bld', 'build', 'coast', 'cvy', 'dsb', 'fct', 'hld', 'ins', 'lpar', 'move_by_cvy', 'mto', 'not', 'order', 'pob', 'power', 'prov_coast', 'prov_land_sea', 'prov_landlock', 'prov_no_coast', 'prov_sea', 'province', 'prp', 'qry', 'rem', 'retreat', 'rpar', 'rto', 'season', 'sup', 'supply_center', 'thk', 'turn', 'unit', 'unit_type', 'why', 'why_param', 'ws', 'wve']),
        ([POB], False,  ['arrangement', 'fct', 'ins', 'lpar', 'not', 'pob', 'prp', 'qry', 'rpar', 'thk', 'why', 'why_param']),
        (["POB", "WHY", "YES", "FRM", "IDK", "TRY"], False, ['arrangement', 'exp', 'fct', 'frm', 'idk', 'idk_param', 'ins', 'lpar', 'message', 'not', 'pob', 'power', 'press_message', 'prov_coast', 'prov_land_sea', 'prov_landlock', 'prov_sea', 'province', 'prp', 'qry', 'rpar', 'season', 'sug', 'thk', 'try', 'try_tokens', 'turn', 'unit', 'unit_type', 'wht', 'why', 'why_param', 'ws', 'yes']),
        ([POB, WHY, YES, FRM, IDK, TRY], False, ['arrangement', 'exp', 'fct', 'frm', 'idk', 'idk_param', 'ins', 'lpar', 'message', 'not', 'pob', 'power', 'press_message', 'prov_coast', 'prov_land_sea', 'prov_landlock', 'prov_sea', 'province', 'prp', 'qry', 'rpar', 'season', 'sug', 'thk', 'try', 'try_tokens', 'turn', 'unit', 'unit_type', 'wht', 'why', 'why_param', 'ws', 'yes']),
        ([AND], False, ['and', 'arrangement', 'lpar', 'rpar', 'sub_arrangement']),
        ([FCT], False, ['arrangement', 'fct', 'lpar', 'not', 'qry', 'rpar']),
    ],
    # fmt: on
)
def test_find_grammar_key_dependencies(
    grammar, keyword, include_level_0, expected_output
):
    keywords_dependecies = _find_grammar_key_dependencies(
        keywords=keyword, grammar=grammar, include_level_0=include_level_0
    )
    assert keywords_dependecies == expected_output


@pytest.mark.parametrize("grammar", [130], indirect=True)
@pytest.mark.parametrize(
    # fmt: off
    ["keyword", "include_level_0"],
    [
        (["AAND"], False),
    ],
    # fmt: on
)
def test_find_grammar_key_dependencies_bad(grammar, keyword, include_level_0):
    with pytest.raises(ValueError):
        _find_grammar_key_dependencies(
            keywords=keyword, grammar=grammar, include_level_0=include_level_0
        )


@pytest.mark.parametrize(
    # fmt: off
    ["keywords", "allow_just_arrangement", "include_level_0", "test_messages", "outcomes"],
    [
        (["PRP", "PCE"], False, True, ["PRP(PCE (AUS ENG))", "PCE (AUS ENG)"], [True, False]),
        (["PCE"], True, True, ["PRP(PCE (AUS ENG))", "PCE (AUS ENG)"], [False, True]),
        (["PRP", "XDO"], False, True, ["PRP(XDO((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY))", "PRP(XDO((ENG FLT (STP SCS)) SUP (ENG AMY LVP) MTO CLY))"], [True, True]),
        (["PRP", "ALY_VSS"], False, True, ["PRP (ALY (ITA TUR) VSS (ENG RUS))", "PRP(XDO((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY))"], [True, False]),
        (["PRP", "XDO", "ALY_VSS"], False, True, ["PRP (ALY (ITA TUR) VSS (ENG RUS))", "PRP(XDO((ENG FLT EDI) SUP (ENG AMY LVP) MTO CLY))"], [True, True]),
        (["PCE", "AND"], False, True, ["AND (PCE (AUS GER)) (PCE (AUS ENG))"], [True]),
        (["PRP", "PCE", "AND"], False, True, ["PRP (AND (PCE (AUS GER)) (PCE (AUS ENG)))"], [True]),
        (["XDO", "PCE", "AND"], False, True, ["AND (PCE (AUS GER)) (PCE (AUS ENG))", "AND (XDO ((ENG FLT (STP SCS)) SUP (ENG AMY LVP) MTO CLY)) ((ENG FLT EDI) MTO CLY)", "ORR (DRW) (DRW (ENG FRA))",], [True, True, False]),
        (["XDO", "PCE", "DRW", "AND", "ORR"], True, True, ["AND (PCE (AUS GER)) (PCE (AUS ENG))", "AND (XDO ((ENG FLT (STP SCS)) SUP (ENG AMY LVP) MTO CLY)) ((ENG FLT EDI) MTO CLY)", "ORR (DRW) (DRW (ENG FRA))",], [True, True, True]),
        (["XDO", "PCE", "DRW", "AND"], True, True, ["AND (PCE (AUS GER)) (PCE (AUS ENG))", "AND (XDO ((ENG FLT (STP SCS)) SUP (ENG AMY LVP) MTO CLY)) ((ENG FLT EDI) MTO CLY)", "ORR (DRW) (DRW (ENG FRA))",], [True, True, False]),
        (["ALY_VSS"], False, True, ["ALY (ITA TUR) VSS (ENG RUS)",], [True]),
    ],
    # fmt: on
)
def test_create_grammar_from_press_keywords(
    keywords: List[PressKeywords],
    allow_just_arrangement: bool,
    include_level_0: bool,
    test_messages: List[str],
    outcomes: List[bool],
):
    grammar = create_grammar_from_press_keywords(
        keywords,
        allow_just_arrangement=allow_just_arrangement,
        include_level_0=include_level_0,
    )
    for message, outcome in list(zip(test_messages, outcomes)):
        if outcome:
            grammar.parse(message)
        else:
            with pytest.raises(Exception):
                grammar.parse(message)
