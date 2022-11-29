"""
For now this grammar assumes NO PDA games
"""

from __future__ import annotations

from typing import Dict, List, Set, Tuple

from parsimonious.grammar import Grammar
from typing_extensions import Literal


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


DAIDELevel = Literal[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

TRAIL_TOKEN = "---"  # any value starting with '---' is meant to be a continuation of that key, not a replacement

LEVEL_0: GrammarDict = {
    "power": '"AUS" / "ENG" / "FRA" / "GER" / "ITA" / "RUS" / "TUR"',
    "order": "hld / mto / sup / cvy / move_by_cvy / retreat / build",
    "hld": 'lpar unit rpar "HLD"',
    "mto": 'lpar unit rpar "MTO" ws province',
    "sup": 'lpar unit rpar "SUP" lpar unit rpar ("MTO" ws prov_no_coast)?',
    "cvy": 'lpar unit rpar "CVY" lpar unit rpar "CTO" ws province',
    "move_by_cvy": 'lpar unit rpar "CTO" ws province ws "VIA" lpar prov_sea (ws prov_sea)* rpar',
    "retreat": "rto / dsb",
    "rto": 'lpar unit rpar "RTO" ws province',
    "dsb": 'lpar unit rpar "DSB"',
    "build": "bld / rem / wve",
    "bld": 'lpar unit rpar "BLD"',
    "rem": 'lpar unit rpar "REM"',
    "wve": 'power ws "WVE"',
    "unit_type": '"AMY" / "FLT"',
    "unit": "power ws unit_type ws province",
    "prov_no_coast": "prov_land_sea / prov_landlock / prov_sea",
    "prov_coast": '(lpar "STP" ws "NCS" rpar) / (lpar "STP" ws "SCS" rpar) / (lpar "SPA" ws "NCS" rpar) / (lpar "SPA" ws "SCS" rpar) / (lpar "BUL" ws "ECS" rpar) / (lpar "BUL" ws "SCS" rpar)',
    "province": "prov_coast / prov_land_sea / prov_landlock / prov_sea",
    "coast": '"NCS" / "ECS" / "SCS" / "WCS"',
    "prov_land_sea": '"ALB" / "ANK" / "APU" / "ARM" / "BEL" / "BER" / "BRE" / "BUL" / "CLY" / "CON" / "DEN" / "EDI" / "FIN" / "GAS" / "GRE" / "HOL" / "KIE" / "LON" / "LVN" / "LVP" / "MAR" / "NAF" / "NAP" / "NWY" / "PIC" / "PIE" / "POR" / "PRU" / "ROM" / "RUM" / "SEV" / "SMY" / "SPA" / "STP" / "SWE" / "SYR" / "TRI" / "TUN" / "TUS" / "VEN" / "YOR" / "WAL"',
    "prov_landlock": '"BOH" / "BUD" / "BUR" / "MOS" / "MUN" / "GAL" / "PAR" / "RUH" / "SER" / "SIL" / "TYR" / "UKR" / "VIE" / "WAR" ',
    "prov_sea": '"ADR" / "AEG" / "BAL" / "BAR" / "BLA" / "GOB" / "EAS" / "ECH" / "HEL" / "ION" / "IRI" / "LYO" / "MAO" / "NAO" / "NTH" / "NWG" / "SKA" / "TYS" / "WES"',
    "supply_center": '"ANK" / "BEL" / "BER" / "BRE" / "BUD" / "BUL" / "CON" / "DEN" / "EDI" / "GRE" / "HOL" / "KIE" / "LON" / "LVP" / "MAR" / "MOS" / "MUN" / "NAP" / "NWY" / "PAR" / "POR" / "ROM" / "RUM" / "SER" / "SEV" / "SMY" / "SPA" / "STP" / "SWE" / "TRI" / "TUN" / "VEN" / "VIE" / "WAR"',
    "turn": 'season ws ~"\d{4}"',
    "season": '"SPR" / "SUM" / "FAL" / "AUT" / "WIN"',
    "lpar": '~"\s*\(\s*"',
    "rpar": '~"\s*\)\s*"',
    "ws": '~"\s+"',
}

# Peace and Alliances
LEVEL_10: GrammarDict = {
    "pce": '"PCE" lpar power (ws power)+ rpar',
    "ccl": '"CCL" lpar press_message rpar',
    "try": '"TRY" lpar try_tokens (ws try_tokens)* rpar',
    "huh": '"HUH" lpar press_message rpar',
    "prp": '"PRP" lpar arrangement rpar',
    "aly_vss": '"ALY" lpar power (ws power)* rpar "VSS" lpar power (ws power)* rpar',
    "slo": '"SLO" lpar power rpar',
    "not": '("NOT" lpar arrangement rpar)',
    "nar": '"NAR" lpar arrangement rpar',
    "drw": '"DRW" (lpar power (ws power)+ rpar)?',
    "yes": '"YES" lpar press_message rpar',
    "rej": '"REJ" lpar press_message rpar',
    "bwx": '"BWX" lpar press_message rpar',
    "fct": '("FCT" lpar arrangement rpar)',
    "frm": '"FRM" lpar power rpar lpar power (ws power)* rpar lpar message rpar',
    "reply": "yes / rej / bwx / huh",
    "message": "press_message / reply",
    "press_message": "prp / ccl / fct / try / frm",
    "arrangement": "pce / aly_vss / drw / slo / not / nar",
    "try_tokens": '"PRP" / "PCE" / "ALY" / "VSS" / "DRW" / "SLO" / "NOT" / "NAR" / "YES" / "REJ" / "BWX" / "FCT"',
}

# prov_no_coast: all province tokens without coasts
# province: all provinces including coasts

# Order Proposals
LEVEL_20: GrammarDict = {
    "xdo": '"XDO" lpar order rpar',
    "dmz": '"DMZ" lpar power (ws power)* rpar lpar province (ws province)* rpar',
    "arrangement": f"{TRAIL_TOKEN}xdo / dmz",
    "try_tokens": f'{TRAIL_TOKEN}"XDO" / "DMZ"',
}

# Multipart Arrangements
LEVEL_30: GrammarDict = {
    "and": '"AND" lpar sub_arrangement rpar (lpar sub_arrangement rpar)+',
    "orr": '"ORR" lpar sub_arrangement rpar (lpar sub_arrangement rpar)+',
    "sub_arrangement": "pce / aly_vss / drw / slo / not / nar / mto / xdo / dmz",
    "arrangement": f"{TRAIL_TOKEN}and / orr",
    "try_tokens": f'{TRAIL_TOKEN}"AND" / "ORR"',
}

# Sharing out Supply Centers
LEVEL_40: GrammarDict = {
    "scd": '"SCD" (lpar power ws supply_center (ws supply_center)* rpar)+',
    "occ": '"OCC" (lpar unit rpar)+',
    "arrangement": f"{TRAIL_TOKEN}scd / occ",
    "try_tokens": f'{TRAIL_TOKEN}"SCD" / "OCC"',
}

# Nested Multipart Arrangements
LEVEL_50: GrammarDict = {
    "and": '("AND" lpar sub_arrangement rpar (lpar sub_arrangement rpar)+) / ("AND" lpar arrangement rpar (lpar arrangement rpar)+)',
    "orr": '("ORR" lpar sub_arrangement rpar (lpar sub_arrangement rpar)+) / ("ORR" lpar arrangement rpar (lpar arrangement rpar)+)',
    "cho": '"CHO" lpar (~"\d+ \d+") rpar (lpar arrangement rpar)+',
    "arrangement": f"{TRAIL_TOKEN}cho",
    "try_tokens": f'{TRAIL_TOKEN}"CHO"',  # This isn't included in the original daide spec but I think they just forgot it.
}

# Queries and Insistencies
LEVEL_60: GrammarDict = {
    "ins": '"INS" lpar arrangement rpar',
    "qry": '"QRY" lpar arrangement rpar',
    "thk": '("THK" lpar arrangement rpar) / ("THK" lpar qry rpar) /  ("THK" lpar not rpar)',
    "idk": '"IDK" lpar qry rpar',
    "sug": '"SUG" lpar arrangement rpar',
    "fct": '("FCT" lpar arrangement rpar) / ("FCT" lpar qry rpar) / ("FCT" lpar not rpar)',
    "not": '("NOT" lpar arrangement rpar) / ("NOT" lpar qry rpar)',
    "reply": f"{TRAIL_TOKEN}fct / thk / idk",
    "try_tokens": f'{TRAIL_TOKEN}"INS" / "QRY" / "THK" / "IDK" / "SUG"',
    "press_message": f"{TRAIL_TOKEN}thk / ins / qry / sug",
}

# Requests for Suggestion
LEVEL_70: GrammarDict = {
    "wht": '"WHT" lpar unit rpar',
    "how": '("HOW" lpar province rpar) / ("HOW" lpar power rpar)',
    "try_tokens": f'{TRAIL_TOKEN}"HOW" / "WHT"',
    "press_message": f"{TRAIL_TOKEN}wht / how",
}

# Accusations
LEVEL_80: GrammarDict = {
    "exp": '"EXP" lpar turn rpar lpar message rpar',
    "idk": '("IDK" lpar exp rpar) / ("IDK" lpar qry rpar)',
    "sry": '"SRY" lpar exp rpar',
    "press_message": f"{TRAIL_TOKEN}exp",
    "try_tokens": f'{TRAIL_TOKEN}"EXP" / "SRY"',
}

# Future Discussions
LEVEL_90: GrammarDict = {
    "for": '("FOR" lpar turn rpar lpar arrangement rpar) / ("FOR" lpar (lpar turn rpar lpar turn rpar) rpar lpar arrangement rpar)',
    "arrangement": f"{TRAIL_TOKEN}for",
    "try_tokens": f'{TRAIL_TOKEN}"FOR"',
}

# Conditionals
LEVEL_100: GrammarDict = {
    "iff": '"IFF" lpar arrangement rpar "THN" lpar press_message rpar ("ELS" lpar press_message rpar)?',
    "press_message": f"{TRAIL_TOKEN}iff",
    "try_tokens": f'{TRAIL_TOKEN}"IFF"',
}

# Puppets and Favors
LEVEL_110: GrammarDict = {
    "xoy": '"XOY" lpar power rpar lpar power rpar',
    "ydo": '"YDO" lpar power rpar (lpar unit rpar)+',
    "arrangement": f"{TRAIL_TOKEN}xoy / ydo",
    "try_tokens": f'{TRAIL_TOKEN}"XOY" / "YDO"',
}

# Forwarding Press
LEVEL_120: GrammarDict = {
    "snd": '"SND" lpar power rpar lpar power (ws power)* rpar lpar message rpar',
    "fwd": '"FWD" lpar power (ws power)* rpar lpar power rpar lpar power rpar',
    "bcc": '"BCC" lpar power rpar lpar power (ws power)* rpar lpar power rpar',
    "arrangement": f"{TRAIL_TOKEN}snd / fwd / bcc",
    "try_tokens": f'{TRAIL_TOKEN}"SND" / "FWD" / "BCC"',
}

# Explanations
LEVEL_130: GrammarDict = {
    "fct_thk_prp_ins": "fct / thk / prp / ins",
    "qry_exp_wht_prp_ins_sug": "qry / exp / wht / prp / ins / sug",  # added sug because it looks like it's also supported at level 130
    "why": '"WHY" lpar fct_thk_prp_ins rpar',
    "pob": '"POB" lpar why rpar',
    "idk": '"IDK" lpar qry_exp_wht_prp_ins_sug rpar',
    "reply": f"{TRAIL_TOKEN}why / pob / idk",
    "try_tokens": f'{TRAIL_TOKEN}"WHY" / "POB"',
}

LEVELS: Tuple[GrammarDict] = (
    LEVEL_0,
    LEVEL_10,
    LEVEL_20,
    LEVEL_30,
    LEVEL_40,
    LEVEL_50,
    LEVEL_60,
    LEVEL_70,
    LEVEL_80,
    LEVEL_90,
    LEVEL_100,
    LEVEL_110,
    LEVEL_120,
    LEVEL_130,
)

GrammarDict = Dict[str, str]


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
