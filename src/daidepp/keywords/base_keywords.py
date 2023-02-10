from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Union

from typing_extensions import get_args

from daidepp.constants import *
from daidepp.keywords.daide_object import _DAIDEObject

_prov_no_coast = [prov for lit in get_args(ProvinceNoCoast) for prov in get_args(lit)]


@dataclass
class Location:
    province: ProvinceNoCoast
    coast: Optional[Coast] = None

    def __init__(
        self, province: Union[ProvinceNoCoast, Location], coast: Optional[Coast] = None
    ) -> None:
        if isinstance(province, Location):
            self.province = province.province
        else:
            self.province = province
        self.coast = coast

    def __str__(self) -> str:
        if self.coast:
            return f"({self.province} {self.coast})"
        return self.province

    def __hash__(self) -> int:
        return hash(str(self))


@dataclass
class Unit(_DAIDEObject):
    power: Power
    unit_type: UnitType
    location: Location

    def __post_init__(self):
        if isinstance(self.location, str):
            assert self.location in _prov_no_coast
            self.location = Location(province=self.location)

    def __str__(self):
        return f"{self.power} {self.unit_type} {self.location}"


@dataclass
class HLD(_DAIDEObject):
    unit: Unit

    def __str__(self):
        return f"( {self.unit} ) HLD"

    @property
    def location(self) -> Location:
        return self.unit.location


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

    @property
    def unit(self) -> Unit:
        """Unit attribute to keep API consistent

        Returns:
            Unit: The supporting unit (i.e. the one executing the order)
        """
        return self.supporting_unit

    @property
    def province_no_coast_location(self) -> Optional[Location]:
        if self.province_no_coast == None:
            return self.province_no_coast
        else:
            return Location(self.province_no_coast)

    @property
    def location(self) -> Location:
        return self.unit.location

    def __str__(self):
        if not self.province_no_coast:
            return f"( {self.supporting_unit} ) SUP ( {self.supported_unit} )"
        else:
            return f"( {self.supporting_unit} ) SUP ( {self.supported_unit} ) MTO {self.province_no_coast}"


@dataclass
class CVY:
    convoying_unit: Unit
    convoyed_unit: Unit
    province: Location

    def __post_init__(self):
        if isinstance(self.province, str):
            assert self.province in _prov_no_coast
            self.province = Location(province=self.province)

    def __str__(self):
        return f"( {self.convoying_unit} ) CVY ( {self.convoyed_unit} ) CTO {self.province.province}"

    @property
    def unit(self) -> Unit:
        """Unit attribute to keep API consistent

        Returns:
            Unit: The convoying unit (i.e. the fleet)
        """
        return self.convoying_unit

    @property
    def location(self) -> Location:
        return self.unit.location


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

    @property
    def location(self) -> Location:
        return self.province


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

    @property
    def location(self) -> None:
        return None


@dataclass
class BLD(_DAIDEObject):
    unit: Unit

    def __str__(self):
        return f"( {self.unit} ) BLD"

    @property
    def location(self) -> Location:
        return self.unit.location


@dataclass
class REM(_DAIDEObject):
    unit: Unit

    def __str__(self):
        return f"( {self.unit} ) REM"

    @property
    def location(self) -> None:
        return None


@dataclass
class WVE(_DAIDEObject):
    """Wave a build"""

    power: Power

    def __str__(self):
        return f"{self.power} WVE"

    @property
    def location(self) -> None:
        return None


@dataclass
class Turn(_DAIDEObject):
    season: Season
    year: int

    def __str__(self):
        return f"{self.season} {self.year}"


Order = Union[
    HLD,
    MTO,
    SUP,
    CVY,
    MoveByCVY,
]
Build = Union[BLD, REM, WVE]
Retreat = Union[RTO, DSB]

Command = Union[Order, Retreat, Build]
