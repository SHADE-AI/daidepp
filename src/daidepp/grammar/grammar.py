"""
For now this grammar assumes NO PDA games
"""

from __future__ import annotations

from typing import Dict, Tuple

from typing_extensions import Literal

DAIDELevel = Literal[
    0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160
]

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
    "prov_sea": '"ADR" / "AEG" / "BAL" / "BAR" / "BLA" / "GOB" / "EAS" / "ECH" / "HEL" / "ION" / "IRI" / "GOL" / "MAO" / "NAO" / "NTH" / "NWG" / "SKA" / "TYS" / "WES"',
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
    "aly_vss": '"ALY" lpar power (ws power)+ rpar "VSS" lpar power (ws power)* rpar',
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

# "dmz": '"DMZ" lpar power (ws power)* rpar lpar prov_no_coast (ws prov_no_coast)* rpar',
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
    "why_param": "fct / thk / prp / ins",
    "idk_param": "qry / exp / wht / prp / ins / sug",  # added sug because it looks like it's also supported at level 130
    "why": '"WHY" lpar why_param rpar',
    "pob": '"POB" lpar why rpar',
    "idk": '"IDK" lpar idk_param rpar',
    "reply": f"{TRAIL_TOKEN}why / pob / idk",
    "try_tokens": f'{TRAIL_TOKEN}"WHY" / "POB"',
}


# Sending Emotional State
LEVEL_140: GrammarDict = {
    "uhy": '"UHY" lpar press_message rpar',
    "hpy": '"HPY" lpar press_message rpar',
    "ang": '"ANG" lpar press_message rpar',
    "reply": f"{TRAIL_TOKEN}hpy / uhy / ang",
    "try_tokens": f'{TRAIL_TOKEN}"UHY" / "HPY" / "ANG"',
}


# Requesting and Demanding Offer
LEVEL_150: GrammarDict = {
    "rof": '"ROF"',
    "arrangement": f"{TRAIL_TOKEN}rof",
    "try_tokens": f'{TRAIL_TOKEN}"ROF"',
}

# Utilities
LEVEL_160: GrammarDict = {
    "float": 'ws*~"[-+]?((\d*\.\d+)|(\d+\.?))([Ee][+-]?\d+)?"',
    "ulb": '"ULB" lpar power float rpar',
    "uub": '"UUB" lpar power float rpar',
    "arrangement": f"{TRAIL_TOKEN}ulb / uub",
    "try_tokens": f'{TRAIL_TOKEN}"ULB" / "UUB"',
}

LEVELS: Tuple[GrammarDict, ...] = (
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
    LEVEL_140,
    LEVEL_150,
    LEVEL_160,
)

GrammarDict = Dict[str, str]
