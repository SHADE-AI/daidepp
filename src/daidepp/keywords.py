from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Union

from daidepp.constants import *


@dataclass
class Unit:
    power: POWER
    unit_type: UNIT_TYPE
    province: PROVINCE

    def __str__(self):
        return f"{self.power} {self.unit_type} {self.province}"


@dataclass
class HLD:
    unit: Unit

    def __str__(self):
        return f"( {self.unit} ) HLD"


@dataclass
class MTO:
    unit: Unit
    province: PROVINCE

    def __str__(self):
        return f"( {self.unit} ) MTO {self.province}"


@dataclass
class SUP:
    supporting_unit: Unit
    supported_unit: Unit
    province_no_coast: Optional[PROVINCE_NO_COAST] = None

    def __str__(self):
        if not self.province_no_coast:
            return f"( {self.supporting_unit} ) SUP ( {self.supported_unit} )"
        else:
            return f"( {self.supporting_unit} ) SUP ( {self.supported_unit} ) MTO {self.province_no_coast}"


@dataclass
class CVY:
    convoying_unit: Unit
    convoyed_unit: Unit
    province: PROVINCE

    def __str__(self):
        return f"( {self.convoying_unit} ) CVY ( {self.convoyed_unit} ) CTO {self.province}"


@dataclass
class MoveByCVY:
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
class RTO:
    unit: Unit
    province: PROVINCE

    def __str__(self):
        return f"( {self.unit} ) RTO {self.province}"


@dataclass
class DSB:
    unit: Unit

    def __str__(self):
        return f"( {self.unit} ) DSB"


@dataclass
class BLD:
    unit: Unit

    def __str__(self):
        return f"( {self.unit} ) BLD"


@dataclass
class REM:
    unit: Unit

    def __str__(self):
        return f"( {self.unit} ) REM"


@dataclass
class WVE:
    power: POWER

    def __str__(self):
        return f"{self.power} WVE"


@dataclass
class Turn:
    season: SEASON
    year: int

    def __str__(self):
        return f"{self.season} {self.year}"


@dataclass
class PCE:
    powers: List[POWER]

    def __init__(self, *powers):
        self.powers = powers

    def __str__(self):
        return "PCE ( " + " ".join(self.powers) + " )"


@dataclass
class CCL:
    press_message: PRESS_MESSAGE

    def __str__(self):
        return f"CCL ( {self.press_message} )"


@dataclass
class TRY:
    try_tokens: List[TRY_TOKENS]

    def __init__(self, *try_tokens):
        self.try_tokens = try_tokens

    def __str__(self):
        return "TRY ( " + " ".join(self.try_tokens) + " )"


@dataclass
class HUH:
    press_message: PRESS_MESSAGE

    def __str__(self):
        return f"HUH ( {self.press_message} )"


@dataclass
class PRP:
    arrangement: ARRANGEMENT

    def __str__(self):
        return f"PRP ( {self.arrangement} )"


@dataclass
class ALYVSS:
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
class SLO:
    power: POWER

    def __str__(self):
        return f"SLO ( {self.power} )"


@dataclass
class NOT:
    arrangement_qry: Union[ARRANGEMENT, QRY]

    def __str__(self):
        return f"NOT ( {self.arrangement_qry} )"


@dataclass
class NAR:
    arrangement: ARRANGEMENT

    def __str__(self):
        return f"NAR ( {self.arrangement} )"


@dataclass
class DRW:
    powers: Optional[List[POWER]] = None

    def __init__(self, *powers):
        self.powers = powers

    def __str__(self):
        if self.powers:
            return f"DRW ( " + " ".join(self.powers) + " )"
        else:
            return f"DRW"


@dataclass
class YES:
    press_message: PRESS_MESSAGE

    def __str__(self):
        return f"YES ( {self.press_message} )"


@dataclass
class REJ:
    press_message: PRESS_MESSAGE

    def __str__(self):
        return f"REJ ( {self.press_message} )"


@dataclass
class BWX:
    press_message: PRESS_MESSAGE

    def __str__(self):
        return f"BWX ( {self.press_message} )"


@dataclass
class FCT:
    arrangement_qry_not: Union[ARRANGEMENT, QRY, NOT]

    def __str__(self):
        return f"FCT ( {self.arrangement_qry_not} )"


@dataclass
class FRM:
    frm_power: POWER
    recv_powers: List[POWER]
    message: MESSAGE

    def __str__(self):
        return (
            f"FRM ( {self.frm_power} ) ( "
            + " ".join(self.recv_powers)
            + f" ) ( {self.message} )"
        )


@dataclass
class XDO:
    order: ORDER

    def __str__(self):
        return f"XDO ( {self.order} )"


@dataclass
class DMZ:
    powers: List[POWER]
    provinces: List[PROVINCE]

    def __str__(self):
        return (
            "DMZ ( " + " ".join(self.powers) + " ) ( " + " ".join(self.provinces) + " )"
        )


@dataclass
class AND:
    arrangements: List[ARRANGEMENT]

    def __init__(self, *arrangements):
        self.arrangements = arrangements

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangements]
        return f"AND " + " ".join(arr_str)


@dataclass
class ORR:
    arrangements: List[ARRANGEMENT]

    def __init__(self, *arrangements):
        self.arrangements = arrangements

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangements]
        return f"ORR " + " ".join(arr_str)


@dataclass
class PowerAndSupplyCenters:
    power: POWER
    supply_centers: List[SUPPLY_CENTER]

    def __init__(self, power, *supply_centers):
        self.power = power
        self.supply_centers = supply_centers

    def __str__(self):
        return f"{self.power} " + " ".join(self.supply_centers)


@dataclass
class SCD:
    power_and_supply_centers: List[PowerAndSupplyCenters]

    def __init__(self, *power_and_supply_centers):
        self.power_and_supply_centers = power_and_supply_centers

    def __str__(self):
        pas_str = ["( " + str(pas) + " )" for pas in self.power_and_supply_centers]
        return f"SCD " + " ".join(pas_str)


@dataclass
class OCC:
    units: List[Unit]

    def __init__(self, *units):
        self.units = units

    def __str__(self):
        unit_str = ["( " + str(unit) + " )" for unit in self.units]
        return f"OCC ( " + " ".join(unit_str) + " )"


@dataclass
class CHO:
    min_choice: int
    max_choice: int
    arrangements: List[ARRANGEMENT]

    def __init__(self, start_year, end_year, *arrangements):
        self.min_choice = start_year
        self.max_choice = end_year
        self.arrangements = arrangements

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangements]

        return f"CHO ( {self.min_choice} {self.max_choice} ) " + " ".join(arr_str)


@dataclass
class INS:
    arrangement: ARRANGEMENT

    def __str__(self):
        return f"INS ( {self.arrangement} )"


@dataclass
class QRY:
    arrangement: ARRANGEMENT

    def __str__(self):
        return f"QRY ( {self.arrangement} )"


@dataclass
class THK:
    arrangement_qry_not: Union[ARRANGEMENT, QRY, NOT, None]

    def __str__(self):
        return f"THK ( {self.arrangement_qry_not} )"


@dataclass
class IDK:
    qry_exp_wht_prp_ins_sug: Union[QRY, EXP, WHT, PRP, INS, SUG]

    def __str__(self):
        return f"IDK ( {self.qry_exp_wht_prp_ins_sug} )"


@dataclass
class SUG:
    arrangement: ARRANGEMENT

    def __str__(self):
        return f"SUG ( {self.arrangement} )"


@dataclass
class WHT:
    unit: Unit

    def __str__(self):
        return f"WHT ( {self.unit} )"


@dataclass
class HOW:
    province_power: Union[PROVINCE, POWER]

    def __str__(self):
        return f"HOW ( {self.province_power} )"


@dataclass
class EXP:
    turn: Turn
    message: MESSAGE

    def __str__(self):
        return f"EXP ( {self.turn} ) ( {self.message} )"


@dataclass
class SRY:
    exp: EXP

    def __str__(self):
        return f"SRY ( {self.exp} )"


@dataclass
class FOR:
    start_turn: Turn
    end_turn: Optional[Turn]
    arrangement: ARRANGEMENT

    def __str__(self):
        if not self.end_turn:
            return f"FOR ( {self.start_turn} ) ( {self.arrangement} )"
        else:
            return f"FOR ( ( {self.start_turn} ) ( {self.end_turn} ) ) ( {self.arrangement} )"


@dataclass
class IFF:
    arrangement: ARRANGEMENT
    press_message: PRESS_MESSAGE
    els_press_message: Optional[PRESS_MESSAGE] = None

    def __str__(self):
        if not self.els_press_message:
            return f"IFF ( {self.arrangement} ) THN ( {self.press_message} )"
        else:
            return f"IFF ( {self.arrangement} ) THN ( {self.press_message} ) ELS ( {self.els_press_message} )"


@dataclass
class XOY:
    power_x: POWER
    power_y: POWER

    def __str__(self):
        return f"XOY ( {self.power_x} ) ( {self.power_y} )"


@dataclass
class YDO:
    power: POWER
    units: List[Unit]

    def __init__(self, power, *units):
        self.power = power
        self.units = units

    def __str__(self):
        unit_str = ["( " + str(unit) + " )" for unit in self.units]
        return f"YDO ( {self.power} ) " + " ".join(unit_str)


@dataclass
class SND:
    power: POWER
    recv_powers: List[POWER]
    message: MESSAGE

    def __str__(self):
        return (
            f"SND ( {self.power} ) ( "
            + " ".join(self.recv_powers)
            + f" ) ( {self.message} )"
        )


@dataclass
class FWD:
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
class BCC:
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
class WHY:
    fct_thk_prp_ins: Union[FCT, THK, PRP, INS]

    def __str__(self):
        return f"WHY ( {self.fct_thk_prp_ins} )"


@dataclass
class POB:
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
