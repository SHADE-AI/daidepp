from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Union

from daidepp.constants import *
from daidepp.grammar import create_daide_grammar

_grammar = create_daide_grammar(130, string_type="all")


@dataclass
class _DAIDEObject(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    def __post_init__(self):
        _grammar.parse(str(self))


@dataclass
class Unit(_DAIDEObject):
    power: POWER
    unit_type: UNIT_TYPE
    province: PROVINCE

    def __str__(self):
        return f"{self.power} {self.unit_type} {self.province}"


@dataclass
class HLD(_DAIDEObject):
    unit: Unit

    def __str__(self):
        return f"( {self.unit} ) HLD"


@dataclass
class MTO(_DAIDEObject):
    unit: Unit
    province: PROVINCE

    def __str__(self):
        return f"( {self.unit} ) MTO {self.province}"


@dataclass
class SUP(_DAIDEObject):
    unit_1: Unit
    unit_2: Unit
    province_no_coast: Optional[PROVINCE_NO_COAST] = None

    def __str__(self):
        if not self.province_no_coast:
            return f"( {self.unit_1} ) SUP ( {self.unit_2} )"
        else:
            return (
                f"( {self.unit_1} ) SUP ( {self.unit_2} ) MTO {self.province_no_coast}"
            )


@dataclass
class CVY(_DAIDEObject):
    unit_1: Unit
    unit_2: Unit
    province: PROVINCE

    def __str__(self):
        return f"( {self.unit_1} ) CVY ( {self.unit_2} ) CTO {self.province}"


@dataclass
class MoveByCVY(_DAIDEObject):
    unit: Unit
    province: PROVINCE
    province_seas: List[PROVINCE_SEA]

    def __init__(self, unit, province, *province_seas):
        self.unit = unit
        self.province = province
        self.province_seas = province_seas

    def __str__(self):
        return (
            f"( {self.unit} ) CTO {self.province} VIA ( "
            + " ".join(self.province_seas)
            + " )"
        )


@dataclass
class RTO(_DAIDEObject):
    unit: Unit
    province: PROVINCE

    def __str__(self):
        return f"( {self.unit} ) RTO {self.province}"


@dataclass
class DSB(_DAIDEObject):
    unit: Unit

    def __str__(self):
        return f"( {self.unit} ) DSB"


@dataclass
class BLD(_DAIDEObject):
    unit: Unit

    def __str__(self):
        return f"( {self.unit} ) BLD"


@dataclass
class REM(_DAIDEObject):
    unit: Unit

    def __str__(self):
        return f"( {self.unit} ) REM"


@dataclass
class WVE(_DAIDEObject):
    power: POWER

    def __str__(self):
        return f"{self.power} WVE"


@dataclass
class Turn(_DAIDEObject):
    season: SEASON
    year: int

    def __str__(self):
        return f"{self.season} {self.year}"


@dataclass
class PCE(_DAIDEObject):
    powers: List[POWER]

    def __init__(self, *powers):
        self.powers = powers

    def __str__(self):
        return "PCE ( " + " ".join(self.powers) + " )"


@dataclass
class CCL(_DAIDEObject):
    press_message: PRESS_MESSAGE

    def __str__(self):
        return f"CCL ( {self.press_message} )"


@dataclass
class TRY(_DAIDEObject):
    try_tokens: List[TRY_TOKENS]

    def __init__(self, *try_tokens):
        self.try_tokens = try_tokens

    def __str__(self):
        return "TRY ( " + " ".join(self.try_tokens) + " )"


@dataclass
class HUH(_DAIDEObject):
    press_message: PRESS_MESSAGE

    def __str__(self):
        return f"HUH ( {self.press_message} )"


@dataclass
class PRP(_DAIDEObject):
    arrangement: ARRANGEMENT

    def __str__(self):
        return f"PRP ( {self.arrangement} )"


@dataclass
class ALYVSS(_DAIDEObject):
    aly_powers: List[POWER]
    vss_powers: List[POWER]

    def __str__(self):
        return (
            "ALY ( "
            + " ".join(self.aly_powers)
            + " ) VSS ( "
            + " ".join(self.vss_powers)
            + " )"
        )


@dataclass
class SLO(_DAIDEObject):
    power: POWER

    def __str__(self):
        return f"SLO ( {self.power} )"


@dataclass
class NOT(_DAIDEObject):
    arrangement_qry: Union[ARRANGEMENT, QRY]

    def __str__(self):
        return f"NOT ( {self.arrangement_qry} )"


@dataclass
class NAR(_DAIDEObject):
    arrangement: ARRANGEMENT

    def __str__(self):
        return f"NAR ( {self.arrangement} )"


@dataclass
class DRW(_DAIDEObject):
    powers: Optional[List[POWER]] = None

    def __init__(self, *powers):
        self.powers = powers

    def __str__(self):
        if self.powers:
            return f"DRW ( " + " ".join(self.powers) + " )"
        else:
            return f"DRW"


@dataclass
class YES(_DAIDEObject):
    press_message: PRESS_MESSAGE

    def __str__(self):
        return f"YES ( {self.press_message} )"


@dataclass
class REJ(_DAIDEObject):
    press_message: PRESS_MESSAGE

    def __str__(self):
        return f"REJ ( {self.press_message} )"


@dataclass
class BWX(_DAIDEObject):
    press_message: PRESS_MESSAGE

    def __str__(self):
        return f"BWX ( {self.press_message} )"


@dataclass
class FCT(_DAIDEObject):
    arrangement_qry_not: Union[ARRANGEMENT, QRY, NOT]

    def __str__(self):
        return f"FCT ( {self.arrangement_qry_not} )"


@dataclass
class FRM(_DAIDEObject):
    frm_power: POWER
    to_powers: List[POWER]
    message: MESSAGE

    def __str__(self):
        return (
            f"FRM ( {self.frm_power} ) ( "
            + " ".join(self.to_powers)
            + f" ) ( {self.message} )"
        )


@dataclass
class XDO(_DAIDEObject):
    order: ORDER

    def __str__(self):
        return f"XDO ( {self.order} )"


@dataclass
class DMZ(_DAIDEObject):
    powers: List[POWER]
    provinces: List[PROVINCE]

    def __str__(self):
        return (
            "DMZ ( " + " ".join(self.powers) + " ) ( " + " ".join(self.provinces) + " )"
        )


@dataclass
class AND(_DAIDEObject):
    arrangments: List[ARRANGEMENT]

    def __init__(self, *arrangements):
        self.arrangments = arrangements

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangments]
        return f"AND " + " ".join(arr_str)


@dataclass
class ORR(_DAIDEObject):
    arrangments: List[ARRANGEMENT]

    def __init__(self, *arrangements):
        self.arrangments = arrangements

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangments]
        return f"ORR " + " ".join(arr_str)


@dataclass
class SCD(_DAIDEObject):
    power: POWER
    supply_centers: List[SUPPLY_CENTER]

    def __init__(self, power, *supply_centers):
        self.power = power
        self.supply_centers = supply_centers

    def __str__(self):
        return f"SCD ( {self.power} " + " ".join(self.supply_centers) + " )"


@dataclass
class OCC(_DAIDEObject):
    units: List[Unit]

    def __init__(self, *units):
        self.units = units

    def __str__(self):
        unit_str = ["( " + str(unit) + " )" for unit in self.units]
        return f"OCC ( " + " ".join(unit_str) + " )"


@dataclass
class CHO(_DAIDEObject):
    start_year: int
    end_year: int
    arrangments: List[ARRANGEMENT]

    def __init__(self, start_year, end_year, *arrangements):
        self.start_year = start_year
        self.end_year = end_year
        self.arrangments = arrangements

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangments]

        return f"CHO ( {self.start_year} {self.end_year} ) " + " ".join(arr_str)


@dataclass
class INS(_DAIDEObject):
    arrangment: ARRANGEMENT

    def __str__(self):
        return f"INS ( {self.arrangment} )"


@dataclass
class QRY(_DAIDEObject):
    arrangment: ARRANGEMENT

    def __str__(self):
        return f"QRY ( {self.arrangment} )"


@dataclass
class THK(_DAIDEObject):
    arrangement_qry_not: Union[ARRANGEMENT, QRY, NOT, None]

    def __str__(self):
        return f"THK ( {self.arrangement_qry_not} )"


@dataclass
class IDK(_DAIDEObject):
    qry_exp_wht_prp_ins_sug: Union[QRY, EXP, WHT, PRP, INS, SUG]

    def __str__(self):
        return f"IDK ( {self.qry_exp_wht_prp_ins_sug} )"


@dataclass
class SUG(_DAIDEObject):
    arrangement: ARRANGEMENT

    def __str__(self):
        return f"SUG ( {self.arrangement} )"


@dataclass
class WHT(_DAIDEObject):
    unit: Unit

    def __str__(self):
        return f"WHT ( {self.unit} )"


@dataclass
class HOW(_DAIDEObject):
    province_power: Union[PROVINCE, POWER]

    def __str__(self):
        return f"HOW ( {self.province_power} )"


@dataclass
class EXP(_DAIDEObject):
    turn: Turn
    message: MESSAGE

    def __str__(self):
        return f"EXP ( {self.turn} ) ( {self.message} )"


@dataclass
class SRY(_DAIDEObject):
    exp: EXP

    def __str__(self):
        return f"SRY ( {self.exp} )"


@dataclass
class FOR(_DAIDEObject):
    start_turn: Turn
    end_turn: Optional[Turn]
    arrangement: ARRANGEMENT

    def __str__(self):
        if not self.end_turn:
            return f"FOR ( {self.start_turn} ) ( {self.arrangement} )"
        else:
            return f"FOR ( ( {self.start_turn} ) ( {self.end_turn} ) ) ( {self.arrangement} )"


@dataclass
class IFF(_DAIDEObject):
    arrangement: ARRANGEMENT
    press_message: PRESS_MESSAGE
    els_press_message: Optional[PRESS_MESSAGE] = None

    def __str__(self):
        if not self.els_press_message:
            return f"IFF ( {self.arrangement} ) THN ( {self.press_message} )"
        else:
            return f"IFF ( {self.arrangement} ) THN ( {self.press_message} ) ELS ( {self.els_press_message} )"


@dataclass
class XOY(_DAIDEObject):
    power_1: POWER
    power_2: POWER

    def __str__(self):
        return f"XOY ( {self.power_1} ) ( {self.power_2} )"


@dataclass
class YDO(_DAIDEObject):
    power: POWER
    units: List[Unit]

    def __init__(self, power, *units):
        self.power = power
        self.units = units

    def __str__(self):
        unit_str = ["( " + str(unit) + " )" for unit in self.units]
        return f"YDO ( {self.power} ) " + " ".join(unit_str)


@dataclass
class SND(_DAIDEObject):
    power: POWER
    powers: List[POWER]
    message: MESSAGE

    def __str__(self):
        return (
            f"SND ( {self.power} ) ( "
            + " ".join(self.powers)
            + f" ) ( {self.message} )"
        )


@dataclass
class FWD(_DAIDEObject):
    powers: List[POWER]
    power_1: POWER
    power_2: POWER

    def __str__(self):
        return (
            f"FWD ( "
            + " ".join(self.powers)
            + f" ) ( {self.power_1} ) ( {self.power_2} )"
        )


@dataclass
class BCC(_DAIDEObject):
    power_1: POWER
    powers: List[POWER]
    power_2: POWER

    def __str__(self):
        return (
            f"BCC ( {self.power_1} ) ( "
            + " ".join(self.powers)
            + f" ) ( {self.power_2} )"
        )


@dataclass
class WHY(_DAIDEObject):
    fct_thk_prp_ins: Union[FCT, THK, PRP, INS]

    def __str__(self):
        return f"WHY ( {self.fct_thk_prp_ins} )"


@dataclass
class POB(_DAIDEObject):
    why: WHY

    def __str__(self):
        return f"POB ( {self.why} )"


RETREAT = Union[RTO, DSB]
BUILD = Union[BLD, REM, WVE]
ORDER = Union[
    HLD,
    MTO,
    SUP,
    CVY,
    MoveByCVY,
]
REPLY = Union[YES, REJ, BWX, HUH, FCT, THK, IDK, WHY, POB, IDK]
PRESS_MESSAGE = Union[PRP, CCL, FCT, TRY, FRM, THK, INS, QRY, SUG, HOW, WHT, EXP, IFF]
MESSAGE = Union[PRESS_MESSAGE, REPLY]
ARRANGEMENT = Union[
    PCE, ALYVSS, DRW, XDO, DMZ, AND, ORR, SCD, CHO, FOR, XOY, YDO, SND, FWD, BCC
]
