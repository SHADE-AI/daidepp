from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from daidepp.constants import *
from daidepp.keywords.base_keywords import *
from daidepp.keywords.daide_object import _DAIDEObject

if TYPE_CHECKING:
    from typing import Iterable, List, Optional, Tuple, Union


@dataclass(eq=True, frozen=True)
class PCE(_DAIDEObject):
    powers: Tuple[Power]

    def __init__(self, *powers: Power):
        object.__setattr__(self, "powers", tuple(sorted(set(powers))))
        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if len(self.powers) < 2:
            raise ValueError("A peace must have at least 2 powers.")

    def __str__(self):
        return "PCE ( " + " ".join(self.powers) + " )"


@dataclass(eq=True, frozen=True)
class CCL(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"CCL ( {self.press_message} )"


@dataclass(eq=True, frozen=True)
class TRY(_DAIDEObject):
    try_tokens: Tuple[TryTokens]

    def __init__(self, *try_tokens):
        object.__setattr__(self, "try_tokens", tuple(sorted(set(try_tokens))))
        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if not self.try_tokens:
            raise ValueError("A TRY message must have at least 1 token.")

    def __str__(self):
        return "TRY ( " + " ".join(self.try_tokens) + " )"


@dataclass(eq=True, frozen=True)
class HUH(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"HUH ( {self.press_message} )"


@dataclass(eq=True, frozen=True)
class PRP(_DAIDEObject):
    arrangement: Arrangement

    def __str__(self):
        return f"PRP ( {self.arrangement} )"


@dataclass(eq=True, frozen=True)
class ALYVSS(_DAIDEObject):
    aly_powers: Tuple[Power]
    vss_powers: Tuple[Power]

    def __init__(self, aly_powers: Iterable[Power], vss_powers: Iterable[Power]):
        object.__setattr__(self, "aly_powers", tuple(sorted(set(aly_powers))))
        object.__setattr__(self, "vss_powers", tuple(sorted(set(vss_powers))))
        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if len(self.aly_powers) < 2:
            raise ValueError("An alliance must have at least 2 allies.")
        if len(self.vss_powers) < 1:
            raise ValueError("An alliance must have at least 1 enemy.")

    def __str__(self):
        return (
            "ALY ( "
            + " ".join(self.aly_powers)
            + " ) VSS ( "
            + " ".join(self.vss_powers)
            + " )"
        )


@dataclass(eq=True, frozen=True)
class SLO(_DAIDEObject):
    power: Power

    def __str__(self):
        return f"SLO ( {self.power} )"


@dataclass(eq=True, frozen=True)
class NOT(_DAIDEObject):
    arrangement_qry: Union[Arrangement, QRY]

    def __str__(self):
        return f"NOT ( {self.arrangement_qry} )"


@dataclass(eq=True, frozen=True)
class NAR(_DAIDEObject):
    arrangement: Arrangement

    def __str__(self):
        return f"NAR ( {self.arrangement} )"


@dataclass(eq=True, frozen=True)
class DRW(_DAIDEObject):
    powers: Tuple[Power]

    def __init__(self, *powers: Power):
        object.__setattr__(self, "powers", tuple(sorted(set(powers))))
        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if len(self.powers) == 1:
            raise ValueError("A draw cannot involve only a single power.")

    def __str__(self):
        if self.powers:
            return f"DRW ( " + " ".join(self.powers) + " )"
        else:
            return f"DRW"


@dataclass(eq=True, frozen=True)
class YES(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"YES ( {self.press_message} )"


@dataclass(eq=True, frozen=True)
class REJ(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"REJ ( {self.press_message} )"


@dataclass(eq=True, frozen=True)
class BWX(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"BWX ( {self.press_message} )"


@dataclass(eq=True, frozen=True)
class FCT(_DAIDEObject):
    arrangement_qry_not: Union[Arrangement, QRY, NOT]

    def __str__(self):
        return f"FCT ( {self.arrangement_qry_not} )"


@dataclass(eq=True, frozen=True)
class FRM(_DAIDEObject):
    frm_power: Power
    recv_powers: Tuple[Power]
    message: Message

    def __init__(
        self, frm_power: Power, recv_powers: Iterable[Power], message: Message
    ):
        object.__setattr__(self, "frm_power", frm_power)
        object.__setattr__(self, "recv_powers", tuple(sorted(set(recv_powers))))
        object.__setattr__(self, "message", message)
        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if not self.recv_powers:
            raise ValueError("A FRM must have at least 1 receiving power.")

    def __str__(self):
        return (
            f"FRM ( {self.frm_power} ) ( "
            + " ".join(self.recv_powers)
            + f" ) ( {self.message} )"
        )


@dataclass(eq=True, frozen=True)
class XDO(_DAIDEObject):
    order: Command

    def __str__(self):
        return f"XDO ( {self.order} )"


@dataclass(eq=True, frozen=True)
class DMZ(_DAIDEObject):
    """This is an arrangement for the listed powers to remove all units from, and not order to, support to, convoy to, retreat to, or build any units in any of the list of provinces. Eliminated powers must not be included in the power list. The arrangement is continuous (i.e. it isn't just for the current turn)."""

    powers: Tuple[Power]
    provinces: Tuple[Location]
    exhaustive_provinces: Tuple[Location] = field(init=False)

    def __init__(self, powers: Iterable[Power], provinces: Iterable[Location]):
        object.__setattr__(self, "powers", tuple(sorted(set(powers))))
        object.__setattr__(self, "provinces", tuple(sorted(set(provinces))))

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

        object.__setattr__(
            self, "exhaustive_provinces", tuple(sorted(set(exhaustive_provinces)))
        )

        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if not self.powers:
            raise ValueError("A DMZ must involve at least 1 power.")
        if not self.provinces:
            raise ValueError("A DMZ must include at least 1 province.")

    def __str__(self):
        return (
            "DMZ ( "
            + " ".join(self.powers)
            + " ) ( "
            + " ".join(map(lambda x: str(x), self.provinces))
            + " )"
        )


@dataclass(eq=True, frozen=True)
class AND(_DAIDEObject):
    arrangements: Tuple[Arrangement]

    def __init__(self, *arrangements: Arrangement):
        object.__setattr__(
            self, "arrangements", tuple(sorted(set(arrangements), key=str))
        )
        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if len(self.arrangements) < 2:
            raise ValueError("An AND must have at least 2 arrangements.")

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangements]
        return f"AND " + " ".join(arr_str)


@dataclass(eq=True, frozen=True)
class ORR(_DAIDEObject):
    arrangements: Tuple[Arrangement]

    def __init__(self, *arrangements: Arrangement):
        object.__setattr__(
            self, "arrangements", tuple(sorted(set(arrangements), key=str))
        )
        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if len(self.arrangements) < 2:
            raise ValueError("An ORR must have at least 2 arrangements.")

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangements]
        return f"ORR " + " ".join(arr_str)


@dataclass(eq=True, frozen=True)
class PowerAndSupplyCenters:
    power: Power
    supply_centers: Tuple[Location]  # Supply centers

    def __init__(self, power, *supply_centers: Location):
        object.__setattr__(self, "power", power)
        object.__setattr__(self, "supply_centers", tuple(sorted(set(supply_centers))))
        self.__post_init__()

    def __post_init__(self):
        if not self.supply_centers:
            raise ValueError(
                "A PowerAndSupplyCenters must have at least 1 supply center."
            )

    def __str__(self):
        return f"{self.power} " + " ".join(map(lambda x: str(x), self.supply_centers))


@dataclass(eq=True, frozen=True)
class SCD(_DAIDEObject):
    power_and_supply_centers: Tuple[PowerAndSupplyCenters]

    def __init__(self, *power_and_supply_centers: PowerAndSupplyCenters):
        object.__setattr__(
            self,
            "power_and_supply_centers",
            tuple(sorted(set(power_and_supply_centers), key=str)),
        )
        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if not self.power_and_supply_centers:
            raise ValueError("An SCD must have at least 1 power and supply center.")

    def __str__(self):
        pas_str = ["( " + str(pas) + " )" for pas in self.power_and_supply_centers]
        return f"SCD " + " ".join(pas_str)


@dataclass(eq=True, frozen=True)
class OCC(_DAIDEObject):
    units: Tuple[Unit]

    def __init__(self, *units: Unit):
        object.__setattr__(self, "units", tuple(sorted(set(units), key=str)))
        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if not self.units:
            raise ValueError("An OCC must have at least 1 unit.")

    def __str__(self):
        unit_str = ["( " + str(unit) + " )" for unit in self.units]
        return f"OCC " + " ".join(unit_str)


@dataclass(eq=True, frozen=True)
class CHO(_DAIDEObject):
    minimum: int
    maximum: int
    arrangements: Tuple[Arrangement]

    def __init__(self, minimum: int, maximum: int, *arrangements: Arrangement):
        object.__setattr__(self, "minimum", minimum)
        object.__setattr__(self, "maximum", maximum)
        object.__setattr__(
            self, "arrangements", tuple(sorted(set(arrangements), key=str))
        )
        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if not self.arrangements:
            raise ValueError("A CHO must have at least 1 arrangement.")

    def __str__(self):
        arr_str = ["( " + str(arr) + " )" for arr in self.arrangements]

        return f"CHO ( {self.minimum} {self.maximum} ) " + " ".join(arr_str)


@dataclass(eq=True, frozen=True)
class INS(_DAIDEObject):
    arrangement: Arrangement

    def __str__(self):
        return f"INS ( {self.arrangement} )"


@dataclass(eq=True, frozen=True)
class QRY(_DAIDEObject):
    arrangement: Arrangement

    def __str__(self):
        return f"QRY ( {self.arrangement} )"


@dataclass(eq=True, frozen=True)
class THK(_DAIDEObject):
    arrangement_qry_not: Union[Arrangement, QRY, NOT, None]

    def __str__(self):
        return f"THK ( {self.arrangement_qry_not} )"


@dataclass(eq=True, frozen=True)
class IDK(_DAIDEObject):
    qry_exp_wht_prp_ins_sug: Union[QRY, EXP, WHT, PRP, INS, SUG]

    def __str__(self):
        return f"IDK ( {self.qry_exp_wht_prp_ins_sug} )"


@dataclass(eq=True, frozen=True)
class SUG(_DAIDEObject):
    arrangement: Arrangement

    def __str__(self):
        return f"SUG ( {self.arrangement} )"


@dataclass(eq=True, frozen=True)
class WHT(_DAIDEObject):
    unit: Unit

    def __str__(self):
        return f"WHT ( {self.unit} )"


@dataclass(eq=True, frozen=True)
class HOW(_DAIDEObject):
    province_power: Union[Location, Power]

    def __str__(self):
        return f"HOW ( {self.province_power} )"


@dataclass(eq=True, frozen=True)
class EXP(_DAIDEObject):
    turn: Turn
    message: Message

    def __str__(self):
        return f"EXP ( {self.turn} ) ( {self.message} )"


@dataclass(eq=True, frozen=True)
class SRY(_DAIDEObject):
    exp: EXP

    def __str__(self):
        return f"SRY ( {self.exp} )"


@dataclass(eq=True, frozen=True)
class FOR(_DAIDEObject):
    start_turn: Turn
    end_turn: Optional[Turn]
    arrangement: Arrangement

    def __str__(self):
        if not self.end_turn:
            return f"FOR ( {self.start_turn} ) ( {self.arrangement} )"
        else:
            return f"FOR ( ( {self.start_turn} ) ( {self.end_turn} ) ) ( {self.arrangement} )"


@dataclass(eq=True, frozen=True)
class IFF(_DAIDEObject):
    arrangement: Arrangement
    press_message: PressMessage
    els_press_message: Optional[PressMessage] = None

    def __str__(self):
        if not self.els_press_message:
            return f"IFF ( {self.arrangement} ) THN ( {self.press_message} )"
        else:
            return f"IFF ( {self.arrangement} ) THN ( {self.press_message} ) ELS ( {self.els_press_message} )"


@dataclass(eq=True, frozen=True)
class XOY(_DAIDEObject):
    power_x: Power
    power_y: Power

    def __str__(self):
        return f"XOY ( {self.power_x} ) ( {self.power_y} )"


@dataclass(eq=True, frozen=True)
class YDO(_DAIDEObject):
    power: Power
    units: Tuple[Unit]

    def __init__(self, power, *units):
        object.__setattr__(self, "power", power)
        object.__setattr__(self, "units", tuple(sorted(set(units), key=str)))
        self.__post_init__()

    def __str__(self):
        unit_str = ["( " + str(unit) + " )" for unit in self.units]
        return f"YDO ( {self.power} ) " + " ".join(unit_str)


@dataclass(eq=True, frozen=True)
class SND(_DAIDEObject):
    power: Power
    recv_powers: Tuple[Power]
    message: Message

    def __init__(self, power: Power, recv_powers: Iterable[Power], message: Message):
        object.__setattr__(self, "power", power)
        object.__setattr__(self, "recv_powers", tuple(sorted(set(recv_powers))))
        object.__setattr__(self, "message", message)
        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if not self.recv_powers:
            raise ValueError("A SND must have at least 1 receiving power.")

    def __str__(self):
        return (
            f"SND ( {self.power} ) ( "
            + " ".join(self.recv_powers)
            + f" ) ( {self.message} )"
        )


@dataclass(eq=True, frozen=True)
class FWD(_DAIDEObject):
    powers: Tuple[Power]
    power_1: Power
    power_2: Power

    def __init__(self, powers: Iterable[Power], power_1: Power, power_2: Power):
        object.__setattr__(self, "powers", tuple(sorted(set(powers))))
        object.__setattr__(self, "power_1", power_1)
        object.__setattr__(self, "power_2", power_2)
        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if not self.powers:
            raise ValueError("A FWD must have at least 1 receiving power.")

    def __str__(self):
        return (
            f"FWD ( "
            + " ".join(self.powers)
            + f" ) ( {self.power_1} ) ( {self.power_2} )"
        )


@dataclass(eq=True, frozen=True)
class BCC(_DAIDEObject):
    power_1: Power
    powers: Tuple[Power]
    power_2: Power

    def __init__(self, power_1: Power, powers: Iterable[Power], power_2: Power):
        object.__setattr__(self, "power_1", power_1)
        object.__setattr__(self, "powers", tuple(sorted(set(powers))))
        object.__setattr__(self, "power_2", power_2)
        self.__post_init__()

    def __post_init__(self):
        super().__post_init__()
        if not self.powers:
            raise ValueError("A BCC must have at least 1 receiving power.")

    def __str__(self):
        return (
            f"BCC ( {self.power_1} ) ( "
            + " ".join(self.powers)
            + f" ) ( {self.power_2} )"
        )


@dataclass(eq=True, frozen=True)
class WHY(_DAIDEObject):
    fct_thk_prp_ins: Union[FCT, THK, PRP, INS]

    def __str__(self):
        return f"WHY ( {self.fct_thk_prp_ins} )"


@dataclass(eq=True, frozen=True)
class POB(_DAIDEObject):
    why: WHY

    def __str__(self):
        return f"POB ( {self.why} )"


@dataclass(eq=True, frozen=True)
class UHY(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"UHY ( {self.press_message} )"


@dataclass(eq=True, frozen=True)
class HPY(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"HPY ( {self.press_message} )"


@dataclass(eq=True, frozen=True)
class ANG(_DAIDEObject):
    press_message: PressMessage

    def __str__(self):
        return f"ANG ( {self.press_message} )"


@dataclass(eq=True, frozen=True)
class ROF(_DAIDEObject):
    def __str__(self):
        return f"ROF"


@dataclass(eq=True, frozen=True)
class ULB(_DAIDEObject):
    power: Power
    float_val: float

    def __str__(self):
        return f"ULB ( {self.power} {self.float_val} )"


@dataclass(eq=True, frozen=True)
class UUB(_DAIDEObject):
    power: Power
    float_val: float

    def __str__(self):
        return f"UUB ( {self.power} {self.float_val} )"

@dataclass
class PTC:
    int_val: int
    powers: List[Power]

    def __str__(self):
        return f"PTC {self.int_val} ( " + " ".join(self.powers) + " )"

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
    PTC,
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
    PTC,
]
