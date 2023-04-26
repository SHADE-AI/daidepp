import warnings
from collections import OrderedDict, defaultdict
from typing import Dict, List, Optional, Set, Tuple, Union

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

__all__ = ["DAIDEGrammar", "create_daide_grammar", "create_grammar_from_press_keywords"]


class DAIDEGrammar(Grammar):
    def __init__(self, rules: str = "", **more_rules) -> None:
        super().__init__(rules, **more_rules)
        self._set_try_tokens()

    def _set_try_tokens(self):
        try_tokens = self.get("try_tokens")

        if try_tokens == None:
            self.try_tokens = None
        else:
            if try_tokens.name == "try_tokens" and hasattr(try_tokens, "members"):
                try_tokens_strings: List[PressKeywords] = list(
                    map(lambda x: x.literal, try_tokens.members)
                )
            else:  # condition when there is a single try token. parsimonious replaces token with actual rule.
                try_tokens_strings = try_tokens.name.upper()
            self.try_tokens: List[PressKeywords] = try_tokens_strings

    @staticmethod
    def from_level(
        level: Union[DAIDELevel, List[DAIDELevel]], allow_just_arrangement: bool = False
    ):
        return create_daide_grammar(level, allow_just_arrangement)


def create_daide_grammar(
    level: Union[DAIDELevel, List[DAIDELevel]] = 30,
    allow_just_arrangement: bool = False,
    string_type: Literal["message", "arrangement", "all"] = "message",
) -> DAIDEGrammar:
    """Create a DAIDEGrammar object given a level of DAIDE.

    The DAIDEGrammar object inherits from parsimonious.grammar.Grammar,
    see https://github.com/erikrose/parsimonious for more information.

    Args:
        level (Union[DAIDELevel,List[DAIDELevel]], optional):
            The level of DAIDE to make grammar for. Defaults to 30. If its a list,
            only include levels in list rather than all levels up to given value.
        allow_just_arrangement (bool, optional):
            if set to True, the parser accepts strings that are only arrangements,
            in addition to press messages. So, for example, the parser could parse
            'PCE (GER ITA)'. Normally, this would raise a ParseError. Left for backwards compatibility.
        string_type (Literal["message", "arrangement", "all"], optional):
            if 'message' is passed (default), the grammar will only recognize full DAIDE messages.
            If 'arrangement' is passed, it will recognize messages and arrangements. And if 'all' is
            passed, any DAIDE pattern should be recognized.

    Returns:
        DAIDEGrammar: Grammar object
    """
    if allow_just_arrangement and string_type == "message":
        string_type = "arrangement"

    grammar_str = _create_daide_grammar_str(level, string_type)
    grammar = DAIDEGrammar(grammar_str)
    return grammar


def _create_daide_grammar_dict(
    level: Union[DAIDELevel, List[DAIDELevel]] = 30
) -> GrammarDict:
    """Combine DAIDE grammar dicts into one dict.

    Args:
        level (Union[DAIDELevel,List[DAIDELevel]], optional):
            The level of DAIDE to make grammar for. Defaults to 30. If its a list,
            only include levels in list rather than all levels up to given value.

    Returns:
        GrammarDict: Dictionary representing all rules for passed daide level
    """

    if type(level) is list:
        level_idxs = [int((i) / 10) for i in level]
    else:
        level_idxs = list(range(int((level / 10) + 1)))
    grammar: GrammarDict = {}

    for level_idx in level_idxs:
        new_grammar = LEVELS[level_idx]
        grammar = _merge_grammars(grammar, new_grammar)
    return grammar


def _create_daide_grammar_str(
    level: Union[DAIDELevel, List[DAIDELevel]] = 30,
    string_type: Literal["message", "arrangement", "all"] = "message",
) -> str:
    """Create string representing DAIDE grammar in PEG

    Args:
        level (Union[DAIDELevel,List[DAIDELevel]], optional):
            The level of DAIDE to make grammar for. Defaults to 30. If its a list,
            only include levels in list rather than all levels up to given value.
        string_type (Literal["message", "arrangement", "all"], optional):
            if 'message' is passed (default), the grammar will only recognize full DAIDE messages.
            If 'arrangement' is passed, it will recognize messages and arrangements. And if 'all' is
            passed, any DAIDE pattern should be recognized.

    Returns:
        str: string representing DAIDE grammar in PEG
    """
    grammar_dict = _create_daide_grammar_dict(level)
    grammar_str = _create_grammar_str_from_dict(grammar_dict, string_type)
    return grammar_str


def _sort_grammar_keys(keys: List[str]) -> List[str]:
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
        if item[0] == "message" and string_type in {"message", "arrangement"}:
            left = item[0]
            right = item[1]
            if string_type == "arrangement":
                right += " / arrangement"
            grammar_str = f"{left} = {right}\n" + grammar_str

        else:
            grammar_str += f"{item[0]} = {item[1]}\n"
    return grammar_str


def _merge_grammars(old_grammar: GrammarDict, new_grammar: GrammarDict) -> GrammarDict:
    old_keys = set(old_grammar.keys())
    new_keys = set(new_grammar.keys())

    # Sorting is needed to maintain the original order of the `GrammarDict`s
    sort_key = (list(old_grammar) + list(new_grammar)).index
    old_unique = sorted(old_keys.difference(new_keys), key=sort_key)
    new_unique = sorted(new_keys.difference(old_keys), key=sort_key)
    shared_keys = sorted(new_keys.intersection(old_keys), key=sort_key)

    merged_grammar: GrammarDict = {}
    for key in old_unique:
        merged_grammar[key] = old_grammar[key]
    for key in new_unique:
        merged_grammar[key] = new_grammar[key]
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
) -> DAIDEGrammar:
    """Construct new DAIDE grammar from a list of keywords.

    Parameters
    ----------
    keywords : List[PressKeywords]
        List of press keywords. Although the type hint says List[PressKeywords],
        this can be a list of string literals or DAIDEObjects (to avoid circular imports).
    allow_just_arrangement : bool, optional
        if set to True, the parser accepts strings that are only arrangements, in
        addition to press messages. So, for example, the parser could parse, by default False
    string_type : Literal['message', 'arrangement', 'all'], optional
        if set to True, the parser accepts strings that
        are only arrangements, in addition to press messages. So, for example, the parser could parse
        'PCE (GER ITA)'. Normally, this would raise a ParseError. Left for backwards compatibility.
        string_type (Literal["message", "arrangement", "all"], optional): if 'message' is passed (default),
        the grammar will only recognize full DAIDE messages. If 'arrangement' is passed, it will recognize
        messages and arrangements. And if 'all' is passed, any DAIDE pattern should be recognized, by default "message"

    Returns
    -------
    DAIDEGrammar
        DAIDEGrammar composed from the list of keywords.
    """
    if allow_just_arrangement and string_type == "message":
        string_type = "arrangement"

    full_grammar = create_daide_grammar(
        level=DAIDELevel.__args__[-1],
        string_type=string_type,
    )
    current_set = set(LEVEL_0.keys())
    current_set |= set(keyword.lower() for keyword in keywords)

    # dict of special keywords and their members
    special_keywords = {
        special_keyword: [
            member.name for member in full_grammar[special_keyword].members
        ]
        for special_keyword in [
            "message",
            "arrangement",
            "sub_arrangement",
            "press_message",
            "reply",
        ]
    }

    special_keywords["try_tokens"] = [
        member.literal.lower() for member in full_grammar["try_tokens"].members
    ]
    keyword_dependencies_special_keywords = defaultdict(list)
    for keyword in current_set:
        # 'message' is only added if press_message or reply is added
        for special_keyword in [
            "arrangement",
            "sub_arrangement",
            "press_message",
            "reply",
        ]:
            if keyword in special_keywords[special_keyword]:
                keyword_dependencies_special_keywords[special_keyword].append(
                    (keyword, [keyword])
                )
        if keyword in special_keywords["try_tokens"] or keyword == "aly_vss":
            if keyword == "aly_vss":
                keyword_dependencies_special_keywords["try_tokens"] += [
                    ('"ALY"', []),
                    ('"VSS"', []),
                ]
            else:
                keyword_dependencies_special_keywords["try_tokens"].append(
                    (f'"{keyword.upper()}"', [])
                )

    if "press_message" in keyword_dependencies_special_keywords:
        keyword_dependencies_special_keywords["message"].append(
            ("press_message", ["press_message"])
        )
    if "reply" in keyword_dependencies_special_keywords:
        keyword_dependencies_special_keywords["message"].append(("reply", ["reply"]))

    current_set |= set(keyword_dependencies_special_keywords.keys())

    keyword_dependencies = _find_grammar_key_dependencies(
        keywords=keywords, current_set=current_set
    )
    keyword_dependencies = {
        **keyword_dependencies,
        **keyword_dependencies_special_keywords,
    }

    new_grammar_dict = OrderedDict(LEVEL_0)
    for keyword, rules in keyword_dependencies.items():
        rule_str = _create_grammar_dict_entry(keyword, rules)
        if rule_str:
            new_grammar_dict[keyword] = rule_str

    if "sub_arrangement" in new_grammar_dict:
        new_grammar_dict.move_to_end("sub_arrangement", last=False)
    if "arrangement" in new_grammar_dict:
        new_grammar_dict.move_to_end("arrangement", last=False)
    if "reply" in new_grammar_dict:
        new_grammar_dict.move_to_end("reply", last=False)
    if "press_message" in new_grammar_dict:
        new_grammar_dict.move_to_end("press_message", last=False)
    if "message" in new_grammar_dict:
        new_grammar_dict.move_to_end("message", last=False)

    new_grammar_str = _create_grammar_str_from_dict(new_grammar_dict, string_type)
    new_grammar = DAIDEGrammar(new_grammar_str)
    return new_grammar


def _create_grammar_dict_entry(keyword, rules):
    if not rules:
        warnings.warn(
            f"Requires addtional keywords to form {keyword}'s grammar rule. Ommiting {keyword} from new new grammar."
        )
        return

    rule_str, _ = rules[0]
    for rule, _ in rules[1:]:
        rule_str += f" / {rule}"

    return rule_str


def _find_grammar_key_dependencies(
    keywords: List[PressKeywords],
    current_set: Set[str],
) -> Dict[str, List[Tuple[str, List[str]]]]:
    keywords_dependencies = defaultdict(list)

    for keyword in keywords:
        if not isinstance(keyword, str):
            keyword = keyword.__name__

        keyword = keyword.lower()
        if not any(keyword in level.keys() for level in LEVELS):
            raise ValueError(
                f"keyword: '{keyword}' is not part of the DAIDE++ grammar."
            )

        grammar = _find_highest_level_grammar_dict(keyword)
        grammar_rule = grammar[keyword]
        for split in grammar_rule.split("/"):
            split = split.strip()
            chars_to_replace = [
                '"',
                "(",
                ")",
                "+",
                "*",
                "?",
                "/",
            ]
            tokens = set(
                split.translate({ord(char): "" for char in chars_to_replace}).split()
            )
            dependencies = set()
            for token in tokens:
                if _find_highest_level_grammar_dict(token):
                    dependencies.add(token)
            if (
                dependencies & current_set - set(["lpar", "rpar", "ws"])
                or not dependencies
            ):
                keywords_dependencies[keyword].append((split, list(dependencies)))

    return keywords_dependencies


def _find_highest_level_grammar_dict(grammar_key: str) -> Optional[GrammarDict]:
    for grammar_level in LEVELS[::-1]:
        if grammar_key in grammar_level.keys():
            return grammar_level
    return None
