from typing import List, Set, Tuple, Union

from parsimonious.grammar import Grammar
from typing_extensions import Literal

from daidepp.constants import PressKeywords
from daidepp.grammar.grammar import (
    LEVEL_0,
    LEVELS,
    TRAIL_TOKEN,
    DAIDELevel,
    GrammarDict,
)


class DAIDEGrammar(Grammar):
    def __init__(self, rules: str = "", **more_rules) -> None:
        super().__init__(rules, **more_rules)
        self._set_try_tokens()

    def _set_try_tokens(self):
        try_tokens = self.get("try_tokens")
        try_tokens_strings = list(map(lambda x: x.literal, try_tokens.members))
        self.try_tokens: List[str] = try_tokens_strings

    @staticmethod
    def from_level(level: DAIDELevel, allow_just_arrangement: bool = False):
        return create_daide_grammar(level, allow_just_arrangement)


def create_daide_grammar(
    level: DAIDELevel = 30,
    allow_just_arrangement: bool = False,
    string_type: Literal["message", "arrangement", "all"] = "message",
) -> DAIDEGrammar:
    """Create a DAIDEGrammar object given a level of DAIDE.

    The DAIDEGrammar object inherits from parsimonious.grammar.Grammar,
    see https://github.com/erikrose/parsimonious for more information.

    Args:
        level (DAIDE_LEVEL, optional): level of DIADE to create grammar for. Defaults to 30.
        allow_just_arrangement (bool, optional): if set to True, the parser accepts strings that
        are only arrangements, in addition to press messages. So, for example, the parser could parse
        'PCE (GER ITA)'. Normally, this would raise a ParseError. Left for backwards compatibility.
        string_type (Literal["message", "arrangement", "all"], optional): if 'message' is passed (default), the grammar will only recognize full DAIDE messages. If 'arrangement' is passed, it will recognize messages and arrangements. And if 'all' is passed, any DAIDE pattern should be recognized.

    Returns:
        DAIDEGrammar: Grammar object
    """
    grammar_str = _create_daide_grammar_str(level, allow_just_arrangement, string_type)
    grammar = DAIDEGrammar(grammar_str)
    return grammar


def _create_daide_grammar_dict(level: DAIDELevel = 30) -> GrammarDict:
    """Combine DAIDE grammar dicts into one dict.

    Args:
        level (DAIDE_LEVEL, optional): The level of DAIDE to make grammar for. Defaults to 30.

    Returns:
        GRAMMAR_DICT: Dictionary representing all rules for passed daide level
    """

    level_idxs = list(range(int((level / 10) + 1)))
    grammar: GrammarDict = {}

    for level_idx in level_idxs:
        new_grammar = LEVELS[level_idx]
        grammar = _merge_grammars(grammar, new_grammar)
    return grammar


def _create_daide_grammar_str(
    level: DAIDELevel = 30,
    allow_just_arrangement: bool = False,
    string_type: Literal["message", "arrangement", "all"] = "message",
) -> str:
    """Create string representing DAIDE grammar in PEG

    Args:
        level (DAIDE_LEVEL, optional): _description_. Defaults to 30.

    Returns:
        str: string representing DAIDE grammar in PEG
    """
    grammar_dict = _create_daide_grammar_dict(level)
    grammar_str = _create_grammar_str_from_dict(
        grammar_dict, allow_just_arrangement, string_type
    )
    return grammar_str


def _sort_grammar_keys(keys: List[str]) -> Tuple:
    keys_list = []

    keys.remove("lpar")
    keys.remove("rpar")
    keys.remove("ws")
    keys.remove("try_tokens")

    # turn goes in front of season
    if "turn" in keys:
        keys_list.append("turn")
        keys.remove("turn")

    # wve goes in front of power
    if "wve" in keys:
        keys_list.append("wve")
        keys.remove("wve")

    # unit must be in front of power
    if "unit" in keys:
        keys_list.append("unit")
        keys.remove("unit")

    # province must be in front of all other province patterns
    if "province" in keys:
        keys_list.append("province")
        keys.remove("province")

    keys_list += keys
    return keys_list


def _create_grammar_str_from_dict(
    grammar: GrammarDict,
    allow_just_arrangement: bool = False,
    string_type: Literal["message", "arrangement", "all"] = "message",
) -> str:
    grammar_str = ""
    if string_type == "all":
        left = "daide_string"
        grammar_keys = list(grammar.keys())
        sorted_keys = _sort_grammar_keys(grammar_keys)
        right = " / ".join(sorted_keys)
        grammar_str = f"{left} = {right}\n"
    for item in grammar.items():
        # message needs to be the first rule in the string, per parsimonious rules:
        # "The first rule is taken to be the default start symbol, but you can override that."
        # https://github.com/erikrose/parsimonious#example-usage
        if item[0] == "message" and string_type == "message":
            left = item[0]
            right = item[1]
            if (
                allow_just_arrangement or string_type == "arrangement"
            ) and string_type != "all":
                right += " / arrangement"
            grammar_str = f"{left} = {right}\n" + grammar_str

        else:
            grammar_str += f"{item[0]} = {item[1]}\n"
    return grammar_str


def _merge_grammars(old_grammar: GrammarDict, new_grammar: GrammarDict) -> GrammarDict:
    old_keys = set(old_grammar.keys())
    new_keys = set(new_grammar.keys())

    old_unique = old_keys.difference(new_keys)
    new_unique = new_keys.difference(old_keys)
    shared_keys = new_keys.intersection(old_keys)

    merged_grammar: GrammarDict = {}
    for key in old_unique:
        merged_grammar[key] = old_grammar[key]
    for key in new_unique:
        merged_grammar[key] = new_grammar[key]
    for key in shared_keys:
        merged_grammar[key] = _merge_shared_key_value(old_grammar, new_grammar, key)
    return merged_grammar


def _merge_shared_key_values(
    old_grammar: GrammarDict, new_grammar: GrammarDict, shared_keys: Set[str]
) -> GrammarDict:
    merged_grammar = {}
    for key in shared_keys:
        merged_grammar[key] = _merge_shared_key_value(old_grammar, new_grammar, key)
    return merged_grammar


def _merge_shared_key_value(
    old_grammar: GrammarDict, new_grammar: GrammarDict, shared_key: str
) -> str:

    if new_grammar[shared_key][:3] == TRAIL_TOKEN:
        new_value = old_grammar[shared_key] + " / " + new_grammar[shared_key][3:]
    else:
        new_value = new_grammar[shared_key]
    return new_value


def create_grammar_from_press_keywords(
    keywords: List[PressKeywords],
    allow_just_arrangement: bool = False,
    string_type: Literal["message", "arrangement", "all"] = "message",
    include_level_0: bool = True,
) -> DAIDEGrammar:
    """_summary_

    Parameters
    ----------
    keywords : List[PressKeywords]
        _description_
    allow_just_arrangement : bool, optional
        _description_, by default False
    string_type : Literal['message', 'arrangement', 'all'], optional
        _description_, by default "message"
    include_level_0 : bool, optional
        _description_, by default True

    Returns
    -------
    DAIDEGrammar
        _description_
    """

    grammar = create_daide_grammar(
        level=DAIDELevel.__args__[-1],
        allow_just_arrangement=allow_just_arrangement,
        string_type=string_type,
    )

    keywords_dependencies = _find_grammar_key_dependencies(
        keywords=keywords, grammar=grammar, include_level_0=include_level_0
    )

    grammar_dict = _create_daide_grammar_dict(level=DAIDELevel.__args__[-1])

    if "press_message" in keywords_dependencies:
        members_in_dependencies = _get_original_members_in_dependencies(
            "press_message", keywords_dependencies, grammar
        )

        if not members_in_dependencies:
            raise ValueError(
                f"New grammar depends on `press_message`, but the given keywords "
                f"do not depend on the 'press_message' members. Such as: {[member.name for member in grammar['press_message'].members]}"
            )

        grammar_dict["press_message"] = " / ".join(members_in_dependencies)

    if "reply" in keywords_dependencies:
        members_in_dependencies = _get_original_members_in_dependencies(
            "reply", keywords_dependencies, grammar
        )

        if not members_in_dependencies:
            raise ValueError(
                f"New grammar depends on `reply`, but the given keywords do not "
                f"depend on the 'reply' members. Such as: {[member.name for member in grammar['reply'].members]}"
            )

        grammar_dict["reply"] = " / ".join(members_in_dependencies)

    if "message" in keywords_dependencies:
        possible_message_dependencies = []

        if "press_message" in keywords_dependencies:
            possible_message_dependencies.append("press_message")
        if "reply" in keywords_dependencies:
            possible_message_dependencies.append("reply")

        if not possible_message_dependencies:
            raise ValueError(
                f"New grammar depends on `message`, but the given keywords do "
                f"not depend on the 'message' members. Such as: {[member.name for member in grammar['message'].members]}"
            )

        grammar_dict["message"] = " / ".join(possible_message_dependencies)

    if "arrangement" in keywords_dependencies:
        members_in_dependencies = _get_original_members_in_dependencies(
            "arrangement", keywords_dependencies, grammar
        )

        if not members_in_dependencies:
            raise ValueError(
                f"New grammar depends on `arrangement`, but the given keywords "
                f"do not depend on the 'arrangment' members. Such as: {[member.name for member in grammar['arrangement'].members]}"
            )

        grammar_dict["arrangement"] = " / ".join(members_in_dependencies)

    if "sub_arrangement" in keywords_dependencies:
        members_in_dependencies = _get_original_members_in_dependencies(
            "sub_arrangement", keywords_dependencies, grammar
        )

        if not members_in_dependencies:
            raise ValueError(
                f"New grammar depends on `sub_arrangement`, but the given keywords "
                f"do not depend on the 'sub_arrangment' members. Such as: {[member.name for member in grammar['sub_arrangement'].members]}"
            )

        grammar_dict["sub_arrangement"] = " / ".join(members_in_dependencies)

    # set try_tokens
    if not "try_tokens" in keywords_dependencies:
        keywords_dependencies.append("try_tokens")
    try_tokens_members = [member.literal for member in grammar["try_tokens"].members]
    members_in_dependencies = [
        '"' + keyword.upper() + '"'
        for keyword in keywords_dependencies
        if keyword.upper() in try_tokens_members
    ]
    grammar_dict["try_tokens"] = " / ".join(members_in_dependencies)
    if not members_in_dependencies:
        raise ValueError(
            f"New grammar depends on `try_tokens`, but the given keywords "
            f"do not depend on the 'try_tokens' members. Such as: {try_tokens_members}"
        )

    new_grammar_dict = {
        keyword: grammar_dict[keyword] for keyword in keywords_dependencies
    }

    new_grammar_str = _create_grammar_str_from_dict(
        new_grammar_dict, allow_just_arrangement, string_type
    )
    new_grammar = DAIDEGrammar(new_grammar_str)

    return new_grammar


def _get_original_members_in_dependencies(
    keyword: str, keywords_dependencies: List[str], grammar: DAIDEGrammar
) -> List[str]:
    original_members: List[str] = [member.name for member in grammar[keyword].members]
    original_members_in_dependencies: List[str] = [
        keyword for keyword in keywords_dependencies if keyword in original_members
    ]
    return original_members_in_dependencies


def _find_grammar_key_dependencies(
    keywords: List[PressKeywords], grammar: DAIDEGrammar, include_level_0: bool = True
) -> DAIDEGrammar:

    keywords_dependencies = []
    if include_level_0:
        keywords_dependencies.extend(LEVEL_0.keys())

    for keyword in keywords:
        if not isinstance(keyword, str):
            keyword = keyword.__name__

        keyword = keyword.lower()
        if not keyword in grammar.keys():
            raise ValueError(
                f"keyword: '{keyword}' is not part of the DAIDE++ grammar."
            )

        accumulator = []
        _find_grammar_key_dependencies_helper(
            grammar_key=keyword, grammar=grammar, accumulator=accumulator
        )
        keywords_dependencies.extend(accumulator)

    keywords_dependencies = list(set(keywords_dependencies))
    keywords_dependencies.sort()

    return keywords_dependencies


def _find_grammar_key_dependencies_helper(
    grammar_key: str, grammar: DAIDEGrammar, accumulator: List[str]
) -> List[str]:

    grammar_key = grammar_key.lower()

    recursion_terminators = [
        "message",
        "reply",
        "press_message",
        "arrangement",
        "sub_arrangement",
        "lpar",
        "rpar",
        "ws",
    ]

    if grammar_key in accumulator:
        return

    elif grammar_key in recursion_terminators:
        accumulator.append(grammar_key)

    else:
        accumulator.append(grammar_key)
        for member in grammar[grammar_key].members:
            if member.name != "":
                _find_grammar_key_dependencies_helper(member.name, grammar, accumulator)

            elif hasattr(member, "members"):
                for member_member in member.members:
                    if member_member.name != "":
                        _find_grammar_key_dependencies_helper(
                            member_member.name, grammar, accumulator
                        )


# create_grammar_from_press_keywords(["POB", "WHY", "YES", "FRM", "IDK", "TRY"])
# create_grammar_from_press_keywords(["POB", "WHY", "YES", "FRM", "IDK", "TRY"], include_level_0=False)
# create_grammar_from_press_keywords(["POB", "WHY", "YES", "FRM", "IDK"], include_level_0=False)
# create_grammar_from_press_keywords(["POB"])
# create_grammar_from_press_keywords(["POB"], include_level_0=False)
# create_grammar_from_press_keywords(["PRP", "YES", "CCL", "XDO"], include_level_0=False)
# create_grammar_from_press_keywords(["PRP", "YES", "CCL"], include_level_0=False)
# create_grammar_from_press_keywords(["SND"], include_level_0=False)
# create_grammar_from_press_keywords(["FRM"], include_level_0=False)
# from daidepp.keywords import POB
# create_grammar_from_press_keywords(["POB", "WHY", "YES", "FRM", "IDK"], include_level_0=False)
# create_grammar_from_press_keywords(["IDK"])
# create_grammar_from_press_keywords(["IDK"], include_level_0=False)
# create_grammar_from_press_keywords(["WHT"], include_level_0=False)
# create_grammar_from_press_keywords(["PRP"], include_level_0=False)
# create_grammar_from_press_keywords(["INS"], include_level_0=False)
# create_grammar_from_press_keywords(["POB", "WHY", "YES", "FRM", "QRY", "WHT"], include_level_0=False)
# create_grammar_from_press_keywords(["AND"], include_level_0=False)
# create_grammar_from_press_keywords(["FCT"], include_level_0=False)
# create_grammar_from_press_keywords(["NOT"], include_level_0=False)
