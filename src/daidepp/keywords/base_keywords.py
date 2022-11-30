from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Union

from daidepp.constants import *
from daidepp.keywords.daide_object import _DAIDEObject


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
    province: Location
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
