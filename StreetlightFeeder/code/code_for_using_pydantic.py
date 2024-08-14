from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


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


class DeviceModel(BaseModel):
    brandName: Optional[str] = Field(
        None,
        description='Name of the brand associated with an entity, e.g., sensor, device etc',
    )
    manufacturerName: Optional[str] = Field(
        None,
        description='Name of the manufacturer associated with an entity, e.g., sensor, device etc',
    )
    modelName: Optional[str] = Field(
        None,
        description='Name of a specific model associated with an entity, e.g., sensor, device etc',
    )
    modelURL: Optional[str] = Field(
        None,
        description='URL providing further information of a specific model associated with an entity, e.g., sensor, device etc',
    )


class DeviceInfo(BaseModel):
    deviceBatteryStatus: Optional[str] = Field(
        None,
        description='Gives the Battery charging status of the reporting device(Connected, Disconnected)',
    )
    deviceId: Optional[str] = Field(
        None,
        description='Device ID of the physical sensor/ measurement station corresponding to this observation',
    )
    deviceModel: Optional[DeviceModel] = Field(
        None,
        description='Describes the information of the device, sensor or system in consideration',
    )
    deviceName: Optional[str] = Field(
        None,
        description='Device Name or Station name of the sensor device/station corresponding to this observation',
    )
    deviceSimNumber: Optional[str] = Field(
        None,
        description='Gives the sim number of the device in the waste management vehicle',
    )
    measurand: Optional[str] = Field(
        None, description='Property/properties sensed/observed/measured by the device'
    )
    rfId: Optional[str] = Field(None, description='Gives the ID of the RFID reader')


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
    StreetlightFeeder = 'StreetlightFeeder'


class StreetlightFeeder(BaseModel):
    activePower: Optional[List[float]] = Field(
        None,
        description='Active power consumed per phase. Ordered triple comprising of active power from three phases in the following order: [R Y B]',
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
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
    deviceInfo: Optional[DeviceInfo] = Field(
        None,
        description='Information about the device associated with the observations',
    )
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
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    numStreetlight: Optional[float] = Field(
        None,
        description='Describes the total number of streetlights connected to the feeder panel corresponding to this observation',
    )
    observationDateTime: Optional[AwareDatetime] = Field(
        None, description='Last reported time of observation'
    )
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
    phaseCurrent: Optional[List[float]] = Field(
        None,
        description='Current per phase. Ordered triple comprising of active power from three phases in the following order: [R Y B]',
    )
    phaseVoltage: Optional[List[float]] = Field(
        None,
        description='Voltage per phase. Ordered triple comprising of active power from three phases in the following order: [R Y B]',
    )
    powerState: Optional[str] = Field(
        None, description='Indicates the current status of the streetlight feeder panel'
    )
    reactivePower: Optional[List[float]] = Field(
        None,
        description='Reactive power consumed per phase. Ordered triple comprising of active power from three phases in the following order: [R Y B]',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    totalActivePower: Optional[float] = Field(
        None, description='Total active power consumed by all phases'
    )
    totalReactivePower: Optional[float] = Field(
        None, description='Total reactive power for all phases'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI entity type. It has to be StreetlightFeeder'
    )
