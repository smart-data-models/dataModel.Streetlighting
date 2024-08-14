from __future__ import annotations

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


class CategoryEnum(Enum):
    bollard = 'bollard'
    flashingBeacon = 'flashingBeacon'
    lamppost = 'lamppost'
    lightTower = 'lightTower'
    ornamentalLantern = 'ornamentalLantern'
    postTop = 'postTop'
    sideEntry = 'sideEntry'
    signLight = 'signLight'


class ColumnMadeOf(Enum):
    steel = 'steel'
    aluminium = 'aluminium'
    wood = 'wood'
    other = 'other'


class LampTechnology(Enum):
    LED = 'LED'
    LPS = 'LPS'
    HPS = 'HPS'


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


class Type6(Enum):
    StreetlightModel = 'StreetlightModel'


class StreetlightModel(BaseModel):
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
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description="Type of asset which implements the street light. Enum:'`postTop, bollard, lamppost, lightTower, flashingBeacon, sideEntry, signLight, ornamentalLantern'. Or any other value not defined above and meaningful for the application",
        min_length=1,
    )
    color: Optional[str] = Field(None, description='The color of the product')
    colorRenderingIndex: Optional[float] = Field(
        None, description='Color rendering index of the lamp'
    )
    colorTemperature: Optional[confloat(ge=0.0)] = Field(
        None, description='Correlated color temperature of the lamp'
    )
    columnBrandName: Optional[str] = Field(
        None, description="Name of the column's brand"
    )
    columnColor: Optional[str] = Field(
        None,
        description="Column's painting color. Allowed Values: A color keyword as specified by [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords). A color value as specified by [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)",
    )
    columnMadeOf: Optional[ColumnMadeOf] = Field(
        None,
        description="Material column is made of. Enum:'steel, aluminium, wood, other'",
    )
    columnManufacturerName: Optional[str] = Field(
        None, description="Name of the column's manufacturer"
    )
    columnModelName: Optional[str] = Field(
        None, description="Name of the column's model"
    )
    compliantWith: Optional[List[str]] = Field(
        None,
        description='A list of standards to which this streetlight model is compliant with',
        min_length=1,
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
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
    image: Optional[AnyUrl] = Field(None, description='An image of the item')
    lampBrandName: Optional[str] = Field(None, description="Name of the lamp's brand")
    lampManufacturerName: Optional[str] = Field(
        None, description="Name of the lamp's manufacturer"
    )
    lampModelName: Optional[str] = Field(None, description="Name of the lamp's model")
    lampTechnology: Optional[LampTechnology] = Field(
        None,
        description="Technology used by the lamp. Enum:'LED, LPS, HPS'. Or any other value not covered by the above list and meaningful to the application",
    )
    lampWeight: Optional[str] = Field(None, description="Lamp's weight")
    lanternBrandName: Optional[str] = Field(
        None, description="Name of the lantern's brand"
    )
    lanternManufacturerName: Optional[str] = Field(
        None, description="Name of the lantern's manufacturer"
    )
    lanternModelName: Optional[str] = Field(
        None, description="Name of the lantern's model"
    )
    lanternWeight: Optional[confloat(ge=0.0)] = Field(
        None, description="Lantern's weight"
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    luminousFlux: Optional[confloat(ge=0.0)] = Field(
        None, description='Maximum light output which can be provided by the lamp'
    )
    maxPowerConsumption: Optional[confloat(ge=0.0)] = Field(
        None, description='Maximum power consumption supported by the lantern'
    )
    minPowerConsumption: Optional[confloat(ge=0.0)] = Field(
        None, description='Minimum power consumption supported by the lantern'
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
    powerConsumption: Optional[confloat(ge=0.0)] = Field(
        None, description='(Nominal) power consumption made by the lamp'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be StreetlightModel'
    )
    workingLife: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The estimated number of hours working (the lamp) without failure',
    )
