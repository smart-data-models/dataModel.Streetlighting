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


class ControllingMethod(Enum):
    group = 'group'
    individual = 'individual'


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
    RFId: Optional[str] = Field(None, description='Gives the ID of the RFID reader')
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


class LocationCategory(Enum):
    bridge = 'bridge'
    centralIsland = 'centralIsland'
    facade = 'facade'
    garden = 'garden'
    park = 'park'
    parking = 'parking'
    pedestrianPath = 'pedestrianPath'
    playground = 'playground'
    road = 'road'
    sidewalk = 'sidewalk'
    tunnel = 'tunnel'


class MunicipalityInfo(BaseModel):
    cityId: Optional[str] = Field(
        None, description='City ID corresponding to this observation'
    )
    cityName: Optional[str] = Field(
        None, description='City name corresponding to this observation'
    )
    district: Optional[str] = Field(
        None, description='District name corresponding to this observation'
    )
    stateName: Optional[str] = Field(
        None, description='Name of the state corresponding to this observation'
    )
    ulbName: Optional[str] = Field(None, description='')
    wardNum: Optional[float] = Field(
        None, description='Ward number corresponding to this observation'
    )
    zoneId: Optional[str] = Field(
        None, description='Zone ID corresponding to this observation'
    )


class PowerState(Enum):
    bootingUp = 'bootingUp'
    low = 'low'
    off = 'off'
    on = 'on'


class Status(Enum):
    brokenLantern = 'brokenLantern'
    columnIssue = 'columnIssue'
    defectiveLamp = 'defectiveLamp'
    ok = 'ok'


class Type6(Enum):
    Streetlight = 'Streetlight'


class Streetlight(BaseModel):
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
    circuit: Optional[str] = Field(
        None,
        description='The circuit to which this streetlight connects to and gets power from. Typically it will contain an identifier that will allow to obtain more information about such circuit',
    )
    color: Optional[str] = Field(None, description='The color of the product')
    controllingMethod: Optional[ControllingMethod] = Field(
        None,
        description="The method used to control this streetlight. Enum:'group, individual'. ",
    )
    current: Optional[float] = Field(
        None,
        description='Current value of the streetlight corresponding to this observation',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateLastLampChange: Optional[AwareDatetime] = Field(
        None, description='Timestamp of the last change of lamp made'
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
    dateServiceStarted: Optional[AwareDatetime] = Field(
        None, description='Date at which the streetlight started giving service'
    )
    description: Optional[str] = Field(None, description='A description of this item')
    deviceInfo: Optional[DeviceInfo] = Field(
        None,
        description='Information about the device associated with the observations',
    )
    feederID: Optional[Union[str, AnyUrl]] = Field(
        None,
        description='Unique ID of the streetlight feeder panel associated with the streetlight corresponding to this observation',
    )
    feederPillarNum: Optional[str] = Field(
        None,
        description='Streetlight feeder pillar information associated with the streetlight corresponding to this observation',
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
    illuminanceLevel: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Relative illuminance level setting. A number between 0 and 1'
    )
    image: Optional[AnyUrl] = Field(None, description='An image of the item')
    lanternHeight: Optional[confloat(ge=0.0)] = Field(
        None,
        description="Lantern's height. In columns with many arms this can vary between streetlights. Another variation source of this property are wall-mounted streetlights",
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    locationCategory: Optional[LocationCategory] = Field(
        None,
        description="Category of the location where the streetlight is placed. Enum:'bridge, centralIsland, facade, garden, park, parking, pedestrianPath, playground, road, sidewalk, tunnel'",
    )
    municipalityInfo: Optional[MunicipalityInfo] = Field(
        None, description='Municipality information corresponding to this observation'
    )
    name: Optional[str] = Field(None, description='The name of this item')
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
    powerConsumption: Optional[float] = Field(
        None,
        description='Power consumed by the LED or the streetlight bulb corresponding to this observation',
    )
    powerFactor: Optional[float] = Field(
        None,
        description='Power factor or the ratio of working power of the streetlight corresponding to this observation',
    )
    powerRating: Optional[float] = Field(
        None,
        description='Power rating of the LED or the streetlight bulb corresponding to this observation',
    )
    powerState: Optional[PowerState] = Field(
        None, description="Streetlight's power state. Enum:'bootingUp, low, off, on'"
    )
    refDevice: Optional[
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
        description='Reference to the device(s) used to monitor this streetligth. List of Reference to entity(ies) of type Device',
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
    ] = Field(
        None,
        description='If this streetlight is individually controlled, reference to the control cabinet in charge of',
    )
    refStreetlightGroup: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description="Streetlight's group, if this streetlight belongs to any group",
    )
    refStreetlightModel: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description="Streetlight's model")
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    status: Optional[Status] = Field(
        None,
        description="The overall status of this street light. Enum:'brokenLantern, columnIssue, defectiveLamp, ok'",
    )
    streetPoleNum: Optional[str] = Field(
        None,
        description='Street pole information associated with the streetlight corresponding to this observation',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be Streetlight'
    )
    voltage: Optional[float] = Field(
        None,
        description='Voltage value of the streetlight corresponding to this observation',
    )
