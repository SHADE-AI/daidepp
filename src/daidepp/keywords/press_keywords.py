from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Union

from daidepp.constants import *
from daidepp.keywords.base_keywords import *
from daidepp.keywords.daide_object import _DAIDEObject


@dataclass
class PCE(_DAIDEObject):
    powers: Tuple[Power]

    def __init__(self, *powers: Power):
        powers = tuple(sorted(powers))
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
    try_tokens: Tuple[TryTokens]

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

    def __post_init__(self):
        self.aly_powers = list(sorted(self.aly_powers))
        self.vss_powers = list(sorted(self.vss_powers))

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
    powers: Tuple[Power] = tuple()

    def __init__(self, *powers: Power):
        self.powers = tuple(sorted(powers))
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
    order: Command

    def __str__(self):
        return f"XDO ( {self.order} )"


@dataclass
class DMZ(_DAIDEObject):
    """This is an arrangement for the listed powers to remove all units from, and not order to, support to, convoy to, retreat to, or build any units in any of the list of provinces. Eliminated powers must not be included in the power list. The arrangement is continuous (i.e. it isn't just for the current turn)."""

    powers: List[Power]
    provinces: List[Location]
    exhaustive_provinces: List[Location] = field(init=False)

    def __post_init__(self):
        # This is helpful for checking if a move violates a DMZ order. All possible
        # location objects are included, so one can simply do something like
        # `assert order.loc not in dmz.exhaustive_provinces`
        exhaustive_provinces: List[Location] = []
        for province in self.provinces:
            if province == Location(province="STP"):
                exhaustive_provinces.append(Location(province="STP"))
                exhaustive_provinces.append(Location(province="STP", coast="NCS"))
                exhaustive_provinces.append(Location(province="STP", coast="SCS"))
            elif province == Location(province="SPA"):
                exhaustive_provinces.append(Location(province="SPA"))
                exhaustive_provinces.append(Location(province="SPA", coast="NCS"))
                exhaustive_provinces.append(Location(province="SPA", coast="SCS"))
            elif province == Location(province="BUL"):
                exhaustive_provinces.append(Location(province="BUL"))
                exhaustive_provinces.append(Location(province="BUL", coast="ECS"))
                exhaustive_provinces.append(Location(province="BUL", coast="SCS"))
            else:
                exhaustive_provinces.append(province)
        self.exhaustive_provinces = exhaustive_provinces
        self.powers = list(sorted(self.powers))

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
    arrangements: Tuple[Arrangement]

    def __init__(self, *arrangements: Arrangement):
        self.arrangements = arrangements
        self.__post_init__()

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangements]
        return f"AND " + " ".join(arr_str)


@dataclass
class ORR(_DAIDEObject):
    arrangements: Tuple[Arrangement]

    def __init__(self, *arrangements: Arrangement):
        self.arrangements = arrangements
        self.__post_init__()

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangements]
        return f"ORR " + " ".join(arr_str)


@dataclass
class PowerAndSupplyCenters:
    power: Power
    supply_centers: Tuple[Location]  # Supply centers

    def __init__(self, power, *supply_centers: Location):
        self.power = power
        self.supply_centers = supply_centers

    def __str__(self):
        return f"{self.power} " + " ".join(map(lambda x: str(x), self.supply_centers))


@dataclass
class SCD(_DAIDEObject):
    power_and_supply_centers: Tuple[PowerAndSupplyCenters]

    def __init__(self, *power_and_supply_centers: PowerAndSupplyCenters):
        self.power_and_supply_centers = power_and_supply_centers
        self.__post_init__()

    def __str__(self):
        pas_str = ["( " + str(pas) + " )" for pas in self.power_and_supply_centers]
        return f"SCD " + " ".join(pas_str)


@dataclass
class OCC(_DAIDEObject):
    units: Tuple[Unit]

    def __init__(self, *units: Unit):
        self.units = units
        self.__post_init__()

    def __str__(self):
        unit_str = ["( " + str(unit) + " )" for unit in self.units]
        return f"OCC " + " ".join(unit_str)


@dataclass
class CHO(_DAIDEObject):
    minimum: int
    maximum: int
    arrangements: Tuple[Arrangement]

    def __init__(self, minimum: int, maximum: int, *arrangements: Arrangement):
        self.minimum = minimum
        self.maximum = maximum
        self.arrangements = arrangements
        self.__post_init__()

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangements]

        return f"CHO ( {self.minimum} {self.maximum} ) " + " ".join(arr_str)


@dataclass
class INS(_DAIDEObject):
    arrangement: Arrangement

    def __str__(self):
        return f"INS ( {self.arrangement} )"


@dataclass
class QRY(_DAIDEObject):
    arrangement: Arrangement

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
    units: Tuple[Unit]

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

    def __post_init__(self):
        self.powers = sorted(self.powers)

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


@dataclass
class UHY(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"UHY ( {self.press_message} )"


@dataclass
class HPY(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"HPY ( {self.press_message} )"


@dataclass
class ANG(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"ANG ( {self.press_message} )"


@dataclass
class ROF(_DAIDEObject):
    def __str__(self):
        return f"ROF"


@dataclass
class ULB:
    power: Power
    float_val: float

    def __str__(self):
        return f"ULB ( {self.power} {self.float_val} )"


@dataclass
class UUB:
    power: Power
    float_val: float

    def __str__(self):
        return f"UUB ( {self.power} {self.float_val} )"


Reply = Union[YES, REJ, BWX, HUH, FCT, THK, IDK, WHY, POB, UHY, HPY, ANG]
PressMessage = Union[
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
]
Message = Union[PressMessage, Reply]
Arrangement = Union[
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
    ULB,
    UUB,
    ROF,
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
    SLO,
    NOT,
    NAR,
    OCC,
    SRY,
    UHY,
    HPY,
    ANG,
    ROF,
    ULB,
    UUB,
]
