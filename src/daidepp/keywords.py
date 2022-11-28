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
class Location:
    province: Union[str, Location]
    coast: Optional[str] = None

    def __post_init__(self):
        if isinstance(self.province, Location):
            self.province = self.province.province

    def __str__(self) -> str:
        if self.coast:
            return f"({self.province} {self.coast})"
        return self.province


@dataclass
class Unit(_DAIDEObject):
    power: Power
    unit_type: UnitType
    location: Location

    def __str__(self):
        return f"{self.power} {self.unit_type} {self.location}"


@dataclass
class HLD(_DAIDEObject):
    unit: Unit

    def __str__(self):
        return f"( {self.unit} ) HLD"


@dataclass
class MTO(_DAIDEObject):
    unit: Unit
    location: Location

    def __str__(self):
        return f"( {self.unit} ) MTO {self.location}"


@dataclass
class SUP:
    supporting_unit: Unit
    supported_unit: Unit
    province_no_coast: Optional[ProvinceNoCoast] = None

    def __str__(self):
        if not self.province_no_coast:
            return f"( {self.supporting_unit} ) SUP ( {self.supported_unit} )"
        else:
            return f"( {self.supporting_unit} ) SUP ( {self.supported_unit} ) MTO {self.province_no_coast}"


@dataclass
class CVY:
    convoying_unit: Unit
    convoyed_unit: Unit
    province: ProvinceNoCoast

    def __str__(self):
        return f"( {self.convoying_unit} ) CVY ( {self.convoyed_unit} ) CTO {self.province}"


@dataclass
class MoveByCVY(_DAIDEObject):
    unit: Unit
    province: Province
    province_seas: List[Location]

    def __init__(self, unit, province, *province_seas):
        self.unit = unit
        self.province = province
        self.province_seas = province_seas

    def __str__(self):
        return (
            f"( {self.unit} ) CTO {self.province} VIA ( "
            + " ".join(map(lambda x: str(x), self.province_seas))
            + " )"
        )


@dataclass
class RTO(_DAIDEObject):
    unit: Unit
    location: Location

    def __str__(self):
        return f"( {self.unit} ) RTO {self.location}"


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
    power: Power

    def __str__(self):
        return f"{self.power} WVE"


@dataclass
class Turn(_DAIDEObject):
    season: Season
    year: int

    def __str__(self):
        return f"{self.season} {self.year}"


@dataclass
class PCE(_DAIDEObject):
    powers: List[Power]

    def __init__(self, *powers):
        self.powers = powers
        self.__post_init__()

    def __str__(self):
        return "PCE ( " + " ".join(self.powers) + " )"


@dataclass
class CCL(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"CCL ( {self.press_message} )"


@dataclass
class TRY(_DAIDEObject):
    try_tokens: List[TryTokens]

    def __init__(self, *try_tokens):
        self.try_tokens = try_tokens
        self.__post_init__()

    def __str__(self):
        return "TRY ( " + " ".join(self.try_tokens) + " )"


@dataclass
class HUH(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"HUH ( {self.press_message} )"


@dataclass
class PRP(_DAIDEObject):
    arrangement: Arrangement

    def __str__(self):
        return f"PRP ( {self.arrangement} )"


@dataclass
class ALYVSS(_DAIDEObject):
    aly_powers: List[Power]
    vss_powers: List[Power]

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
    power: Power

    def __str__(self):
        return f"SLO ( {self.power} )"


@dataclass
class NOT(_DAIDEObject):
    arrangement_qry: Union[Arrangement, QRY]

    def __str__(self):
        return f"NOT ( {self.arrangement_qry} )"


@dataclass
class NAR(_DAIDEObject):
    arrangement: Arrangement

    def __str__(self):
        return f"NAR ( {self.arrangement} )"


@dataclass
class DRW(_DAIDEObject):
    powers: Optional[List[Power]] = None

    def __init__(self, *powers):
        self.powers = powers
        self.__post_init__()

    def __str__(self):
        if self.powers:
            return f"DRW ( " + " ".join(self.powers) + " )"
        else:
            return f"DRW"


@dataclass
class YES(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"YES ( {self.press_message} )"


@dataclass
class REJ(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"REJ ( {self.press_message} )"


@dataclass
class BWX(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"BWX ( {self.press_message} )"


@dataclass
class FCT(_DAIDEObject):
    arrangement_qry_not: Union[Arrangement, QRY, NOT]

    def __str__(self):
        return f"FCT ( {self.arrangement_qry_not} )"


@dataclass
class FRM(_DAIDEObject):
    frm_power: Power
    recv_powers: List[Power]
    message: Message

    def __str__(self):
        return (
            f"FRM ( {self.frm_power} ) ( "
            + " ".join(self.recv_powers)
            + f" ) ( {self.message} )"
        )


@dataclass
class XDO(_DAIDEObject):
    order: Order

    def __str__(self):
        return f"XDO ( {self.order} )"


@dataclass
class DMZ(_DAIDEObject):
    powers: List[Power]
    provinces: List[Location]

    def __str__(self):
        return (
            "DMZ ( "
            + " ".join(self.powers)
            + " ) ( "
            + " ".join(map(lambda x: str(x), self.provinces))
            + " )"
        )


@dataclass
class AND(_DAIDEObject):
    arrangments: List[Arrangement]

    def __init__(self, *arrangements):
        self.arrangements = arrangements
        self.__post_init__()

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangements]
        return f"AND " + " ".join(arr_str)


@dataclass
class ORR(_DAIDEObject):
    arrangments: List[Arrangement]

    def __init__(self, *arrangements):
        self.arrangements = arrangements
        self.__post_init__()

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangements]
        return f"ORR " + " ".join(arr_str)


@dataclass
class PowerAndSupplyCenters:
    power: Power
    supply_centers: List[Location]  # Supply centers

    def __init__(self, power, *supply_centers):
        self.power = power
        self.supply_centers = supply_centers

    def __str__(self):
        return f"{self.power} " + " ".join(map(lambda x: str(x), self.supply_centers))


@dataclass
class SCD(_DAIDEObject):
    power_and_supply_centers: List[PowerAndSupplyCenters]

    def __init__(self, *power_and_supply_centers):
        self.power_and_supply_centers = power_and_supply_centers
        self.__post_init__()

    def __str__(self):
        pas_str = ["( " + str(pas) + " )" for pas in self.power_and_supply_centers]
        return f"SCD " + " ".join(pas_str)


@dataclass
class OCC(_DAIDEObject):
    units: List[Unit]

    def __init__(self, *units):
        self.units = units
        self.__post_init__()

    def __str__(self):
        unit_str = ["( " + str(unit) + " )" for unit in self.units]
        return f"OCC " + " ".join(unit_str)


@dataclass
class CHO(_DAIDEObject):
    minimum: int
    maximum: int
    arrangments: List[Arrangement]

    def __init__(self, minimum, maximum, *arrangements):
        self.minimum = minimum
        self.maximum = maximum
        self.arrangements = arrangements
        self.__post_init__()

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangements]

        return f"CHO ( {self.minimum} {self.maximum} ) " + " ".join(arr_str)


@dataclass
class INS(_DAIDEObject):
    arrangment: Arrangement

    def __str__(self):
        return f"INS ( {self.arrangement} )"


@dataclass
class QRY(_DAIDEObject):
    arrangment: Arrangement

    def __str__(self):
        return f"QRY ( {self.arrangement} )"


@dataclass
class THK(_DAIDEObject):
    arrangement_qry_not: Union[Arrangement, QRY, NOT, None]

    def __str__(self):
        return f"THK ( {self.arrangement_qry_not} )"


@dataclass
class IDK(_DAIDEObject):
    qry_exp_wht_prp_ins_sug: Union[QRY, EXP, WHT, PRP, INS, SUG]

    def __str__(self):
        return f"IDK ( {self.qry_exp_wht_prp_ins_sug} )"


@dataclass
class SUG(_DAIDEObject):
    arrangement: Arrangement

    def __str__(self):
        return f"SUG ( {self.arrangement} )"


@dataclass
class WHT(_DAIDEObject):
    unit: Unit

    def __str__(self):
        return f"WHT ( {self.unit} )"


@dataclass
class HOW(_DAIDEObject):
    province_power: Union[Location, Power]

    def __str__(self):
        return f"HOW ( {self.province_power} )"


@dataclass
class EXP(_DAIDEObject):
    turn: Turn
    message: Message

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
    arrangement: Arrangement

    def __str__(self):
        if not self.end_turn:
            return f"FOR ( {self.start_turn} ) ( {self.arrangement} )"
        else:
            return f"FOR ( ( {self.start_turn} ) ( {self.end_turn} ) ) ( {self.arrangement} )"


@dataclass
class IFF(_DAIDEObject):
    arrangement: Arrangement
    press_message: PressMessage
    els_press_message: Optional[PressMessage] = None

    def __str__(self):
        if not self.els_press_message:
            return f"IFF ( {self.arrangement} ) THN ( {self.press_message} )"
        else:
            return f"IFF ( {self.arrangement} ) THN ( {self.press_message} ) ELS ( {self.els_press_message} )"


@dataclass
class XOY(_DAIDEObject):
    power_x: Power
    power_y: Power

    def __str__(self):
        return f"XOY ( {self.power_x} ) ( {self.power_y} )"


@dataclass
class YDO(_DAIDEObject):
    power: Power
    units: List[Unit]

    def __init__(self, power, *units):
        self.power = power
        self.units = units
        self.__post_init__()

    def __str__(self):
        unit_str = ["( " + str(unit) + " )" for unit in self.units]
        return f"YDO ( {self.power} ) " + " ".join(unit_str)


@dataclass
class SND(_DAIDEObject):
    power: Power
    recv_powers: List[Power]
    message: Message

    def __str__(self):
        return (
            f"SND ( {self.power} ) ( "
            + " ".join(self.recv_powers)
            + f" ) ( {self.message} )"
        )


@dataclass
class FWD(_DAIDEObject):
    powers: List[Power]
    power_1: Power
    power_2: Power

    def __str__(self):
        return (
            f"FWD ( "
            + " ".join(self.powers)
            + f" ) ( {self.power_1} ) ( {self.power_2} )"
        )


@dataclass
class BCC(_DAIDEObject):
    power_1: Power
    powers: List[Power]
    power_2: Power

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


Retreat = Union[RTO, DSB]
Build = Union[BLD, REM, WVE]
Order = Union[
    HLD,
    MTO,
    SUP,
    CVY,
    MoveByCVY,
]
Command = Union[Order, Retreat, Build]

Reply = Union[YES, REJ, BWX, HUH, FCT, THK, IDK, WHY, POB, IDK]
PressMessage = Union[PRP, CCL, FCT, TRY, FRM, THK, INS, QRY, SUG, HOW, WHT, EXP, IFF]
Message = Union[PressMessage, Reply]
Arrangement = Union[
    PCE, ALYVSS, DRW, XDO, DMZ, AND, ORR, SCD, CHO, FOR, XOY, YDO, SND, FWD, BCC
]

AnyDAIDEToken = Union[
    RTO,
    DSB,
    BLD,
    REM,
    WVE,
    HLD,
    MTO,
    SUP,
    CVY,
    MoveByCVY,
    YES,
    REJ,
    BWX,
    HUH,
    FCT,
    THK,
    IDK,
    WHY,
    POB,
    IDK,
    PRP,
    CCL,
    FCT,
    TRY,
    FRM,
    THK,
    INS,
    QRY,
    SUG,
    HOW,
    WHT,
    EXP,
    IFF,
    PCE,
    ALYVSS,
    DRW,
    XDO,
    DMZ,
    AND,
    ORR,
    SCD,
    CHO,
    FOR,
    XOY,
    YDO,
    SND,
    FWD,
    BCC,
]
