import pytest
from daidepp.grammar.grammar_utils import _find_grammar_key_dependencies
from daidepp.keywords import *


@pytest.mark.parametrize(
    "grammar", [130], indirect=True
)
def test_find_grammar_key_dependencies(grammar):

    keywords_dependecies = _find_grammar_key_dependencies(
        keywords=["POB"], grammar=grammar, include_level_0=True
    )
    assert keywords_dependecies == ['arrangement', 'bld', 'build', 'coast', 'cvy', 'dsb', 'fct', 'hld', 'ins', 'lpar', 'move_by_cvy', 'mto', 'not', 'order', 'pob', 'power', 'prov_coast', 'prov_land_sea', 'prov_landlock', 'prov_no_coast', 'prov_sea', 'province', 'prp', 'qry', 'rem', 'retreat', 'rpar', 'rto', 'season', 'sup', 'supply_center', 'thk', 'turn', 'unit', 'unit_type', 'why', 'why_param', 'ws', 'wve']

    keywords_dependecies = _find_grammar_key_dependencies(
        keywords=["POB"], grammar=grammar, include_level_0=False
    )
    assert keywords_dependecies == ['arrangement', 'fct', 'ins', 'lpar', 'not', 'pob', 'prp', 'qry', 'rpar', 'thk', 'why', 'why_param']

    keywords_dependecies = _find_grammar_key_dependencies(
        keywords=[POB], grammar=grammar, include_level_0=True
    )
    assert keywords_dependecies == ['arrangement', 'bld', 'build', 'coast', 'cvy', 'dsb', 'fct', 'hld', 'ins', 'lpar', 'move_by_cvy', 'mto', 'not', 'order', 'pob', 'power', 'prov_coast', 'prov_land_sea', 'prov_landlock', 'prov_no_coast', 'prov_sea', 'province', 'prp', 'qry', 'rem', 'retreat', 'rpar', 'rto', 'season', 'sup', 'supply_center', 'thk', 'turn', 'unit', 'unit_type', 'why', 'why_param', 'ws', 'wve']

    keywords_dependecies = _find_grammar_key_dependencies(
        keywords=[POB], grammar=grammar, include_level_0=False
    )
    assert keywords_dependecies == ['arrangement', 'fct', 'ins', 'lpar', 'not', 'pob', 'prp', 'qry', 'rpar', 'thk', 'why', 'why_param']

    keywords_dependecies = _find_grammar_key_dependencies(
        keywords=["POB", "WHY", "YES", "FRM", "IDK", "TRY"], grammar=grammar, include_level_0=False
    )
    assert keywords_dependecies == ['arrangement', 'exp', 'fct', 'frm', 'idk', 'idk_param', 'ins', 'lpar', 'message', 'not', 'pob', 'power', 'press_message', 'prov_coast', 'prov_land_sea', 'prov_landlock', 'prov_sea', 'province', 'prp', 'qry', 'rpar', 'season', 'sug', 'thk', 'try', 'try_tokens', 'turn', 'unit', 'unit_type', 'wht', 'why', 'why_param', 'ws', 'yes']

    keywords_dependecies = _find_grammar_key_dependencies(
        keywords=[POB, WHY, YES, FRM, IDK, TRY], grammar=grammar, include_level_0=False
    )
    assert keywords_dependecies == ['arrangement', 'exp', 'fct', 'frm', 'idk', 'idk_param', 'ins', 'lpar', 'message', 'not', 'pob', 'power', 'press_message', 'prov_coast', 'prov_land_sea', 'prov_landlock', 'prov_sea', 'province', 'prp', 'qry', 'rpar', 'season', 'sug', 'thk', 'try', 'try_tokens', 'turn', 'unit', 'unit_type', 'wht', 'why', 'why_param', 'ws', 'yes']

    keywords_dependecies = _find_grammar_key_dependencies(
        keywords=[AND], grammar=grammar, include_level_0=False
    )
    assert keywords_dependecies == ['and', 'arrangement', 'lpar', 'rpar', 'sub_arrangement']

    keywords_dependecies = _find_grammar_key_dependencies(
        keywords=[FCT], grammar=grammar, include_level_0=False
    )
    assert keywords_dependecies == ['arrangement', 'fct', 'lpar', 'not', 'qry', 'rpar']

    with pytest.raises(ValueError):
        keywords_dependecies = _find_grammar_key_dependencies(
            keywords=["AAND"], grammar=grammar, include_level_0=False
        )


@pytest.mark.parametrize(
    "grammar", [130], indirect=True
)
def test_create_grammar_from_press_keywords(grammar):
    # create_grammar_from_press_keywords(["POB", "WHY", "YES", "FRM", "QRY", "WHT"], include_level_0=False)
	...

