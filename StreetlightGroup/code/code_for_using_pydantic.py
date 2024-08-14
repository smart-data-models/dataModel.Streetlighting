from __future__ import annotations

from datetime import date
from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class PowerState(Enum):
    bootingUp = 'bootingUp'
    low = 'low'
    off = 'off'
    on = 'on'


class SwitchingModeEnum(Enum):
    night_ON = 'night-ON'
    night_OFF = 'night-OFF'
    night_LOW = 'night-LOW'
    always_ON = 'always-ON'
    day_ON = 'day-ON'
    day_OFF = 'day-OFF'
    day_LOW = 'day-LOW'


class SwitchingOnHour(BaseModel):
    description: Optional[str] = Field(
        None, description='Timestamp of the last change of lamp made'
    )
    from_: Union[
        date,
        constr(
            pattern=r'^--((0[13578]|1[02])-31|(0[1,3-9]|1[0-2])-30|(0\\d|1[0-2])-([0-2]\\d))$'
        ),
    ] = Field(..., alias='from')
    hours: str = Field(..., description='Timestamp of the last change of lamp made')
    to: Union[
        date,
        constr(
            pattern=r'^--((0[13578]|1[02])-31|(0[1,3-9]|1[0-2])-30|(0\\d|1[0-2])-([0-2]\\d))$'
        ),
    ] = Field(..., description='Ending date (it can be yearless)')


class Type6(Enum):
    StreetlightGroup = 'StreetlightGroup'


class StreetlightGroup(BaseModel):
    activeProgramId: Optional[str] = Field(
        None, description='Identifier of the active program for this streetlight group'
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    annotations: Optional[List[str]] = Field(
        None, description='Annotations about the item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    circuitId: Optional[str] = Field(
        None, description='Identifier of the circuit the group is connected to'
    )
    color: Optional[str] = Field(None, description='The color of the product')
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateLastSwitchingOff: Optional[AwareDatetime] = Field(
        None, description='Timestamp of the last switching off'
    )
    dateLastSwitchingOn: Optional[AwareDatetime] = Field(
        None, description='Timestamp of the last switching on'
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    illuminanceLevel: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Relative illuminance level setting for the group. Allowed values: A number between 0 and 1',
    )
    image: Optional[AnyUrl] = Field(None, description='An image of the item')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    powerState: Optional[PowerState] = Field(
        None,
        description="Streetlight group's power state. Enum:'on, off, low, bootingUp'. Enum:'bootingUp, low, off, on'",
    )
    refStreetlight: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='List of streetlight entities belonging to this group. List of references to entities fo type Streetlight. Allowed values: There must topographical integrity between the location of the group and of the individual streetlights',
    )
    refStreetlightControlCabinet: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description="Streetlight group's control cabinet")
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    switchingMode: Optional[List[SwitchingModeEnum]] = Field(
        None,
        description="Timestamp of the last change of lamp made. Enum:' night-ON, night-OFF, night-LOW, always-ON, day-ON, day-OFF, day-LOW'",
    )
    switchingOnHours: Optional[List[SwitchingOnHour]] = Field(
        None,
        description='Switching on hours. It is used normally to set special schedules for certain dates',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be StreetlightGroup'
    )
