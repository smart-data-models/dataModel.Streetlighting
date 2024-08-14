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


class CupboardMadeOf(Enum):
    concrete = 'concrete'
    metal = 'metal'
    other = 'other'
    plastic = 'plastic'


class Feature(Enum):
    astronomicalClock = 'astronomicalClock'
    individualControl = 'individualControl'


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
    StreetlightControlCabinet = 'StreetlightControlCabinet'


class WorkingMode(Enum):
    automatic = 'automatic'
    manual = 'manual'
    semiautomatic = 'semiautomatic'


class StreetlightControlCabinet(BaseModel):
    activePowerR: Optional[confloat(ge=0.0)] = Field(
        None, description='Active power consumed in R phase'
    )
    activePowerS: Optional[confloat(ge=0.0)] = Field(
        None, description='Active power consumed in S phase'
    )
    activePowerT: Optional[confloat(ge=0.0)] = Field(
        None, description='Active power consumed in T phase'
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
    brandName: Optional[str] = Field(None, description="Name of the cabinet's brand")
    color: Optional[str] = Field(None, description='The color of the product')
    compliantWith: Optional[List[str]] = Field(
        None,
        description='A list of standards to which the cabinet controller is compliant with (ex. IP54)',
        min_length=1,
    )
    cosPhi: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Cosine of phi parameter'
    )
    cupboardMadeOf: Optional[CupboardMadeOf] = Field(
        None,
        description="Material the cabinet's cupboard is made of. Enum:'concrete, metal, other, plastic'",
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateLastProgramming: Optional[AwareDatetime] = Field(
        None,
        description='Date at which there was a programming operation over the cabinet',
    )
    dateMeteringStarted: Optional[AwareDatetime] = Field(
        None, description='The starting date for metering energy consumed'
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateServiceStarted: Optional[AwareDatetime] = Field(
        None, description='Date at which the cabinet controller started giving service'
    )
    description: Optional[str] = Field(None, description='A description of this item')
    energyConsumed: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Energy consumed by the circuits controlled since metering started (since dateMeteringStarted)',
    )
    energyCost: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Cost of the energy consumed by the circuits controlled since the metering start date',
    )
    features: Optional[List[Feature]] = Field(
        None,
        description='A list of cabinet controller features.  Those technical values considered meaningful by applications. `astronomicalClock`. The control cabinet includes an astronomical clock to deal with switching hours. `individualControl`. The control cabinet allows to control street lights individually',
        min_length=1,
    )
    frequency: Optional[confloat(ge=0.0)] = Field(
        None, description='The working frequency of the circuit'
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
    image: Optional[AnyUrl] = Field(None, description='An image of the item')
    intensityR: Optional[confloat(ge=0.0)] = Field(
        None, description='Electric intensity in R phase'
    )
    intensityS: Optional[confloat(ge=0.0)] = Field(
        None, description='Electric intensity in S phase'
    )
    intensityT: Optional[confloat(ge=0.0)] = Field(
        None, description=' Electric intensity in T phase'
    )
    lastMeterReading: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Value of the last reading obtained from the energy consumed metering system',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    manufacturerName: Optional[str] = Field(
        None, description="Name of the cabinet's manufacturer"
    )
    maximumPowerAvailable: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The maximum power available (by contract) for the circuits controlled by this cabinet',
    )
    meterReadingPeriod: Optional[confloat(ge=0.0)] = Field(
        None, description='The periodicity of energy consumed meter readings in days'
    )
    modelName: Optional[str] = Field(None, description="Name of the cabinet's model")
    name: Optional[str] = Field(None, description='The name of this item')
    nextActuationDeadline: Optional[AwareDatetime] = Field(
        None,
        description='Deadline for next actuation to be performed (programming, testing, etc.)',
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
    powerFactorR: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None,
        description='Power factor for phase R. Allowed values: A number between -1 and 1',
    )
    powerFactorS: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None,
        description='Power factor for phase S. Allowed values: A number between -1 and 1',
    )
    powerFactorT: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None,
        description='Power factor for phase T. Allowed values: A number between -1 and 1',
    )
    reactiveEnergyConsumed: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Energy consumed (with regards to reactive power) by circuits since the metering start date',
    )
    reactivePowerR: Optional[confloat(ge=0.0)] = Field(
        None, description='Reactive power in R phase'
    )
    reactivePowerS: Optional[confloat(ge=0.0)] = Field(
        None, description='Reactive power in S phase'
    )
    reactivePowerT: Optional[confloat(ge=0.0)] = Field(
        None, description='Reactive power in T phase'
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
        description='Reference to the device(s) used to monitor this control cabinet',
    )
    refStreetlightGroup: Optional[
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
        description='Streetlight group(s) controlled. List of references to entities of type StreetlightGroup',
    )
    responsible: Optional[str] = Field(
        None,
        description='Responsible for the cabinet controller, i.e. entity in charge of actuating (programming, etc.)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    serialNumber: Optional[str] = Field(
        None, description='Serial number of the container'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    thdrIntensityR: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Total harmonic distortion (R) of intensity in phase R. Allowed values: A number between 0 and 1',
    )
    thdrIntensityS: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Total harmonic distortion (S) of intensity in phase S. Allowed values: A number between 0 and 1',
    )
    thdrIntensityT: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Total harmonic distortion (T) of intensity in phase T. Allowed values: A number between 0 and 1',
    )
    thdrVoltageR: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Total harmonic distortion (R) of voltage in phase R. Allowed values: A number between 0 and 1',
    )
    thdrVoltageS: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Total harmonic distortion (S) of voltage in phase S. Allowed values: A number between 0 and 1',
    )
    thdrVoltageT: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Total harmonic distortion (T) of voltage in phase T. Allowed values: A number between 0 and 1',
    )
    totalActivePower: Optional[confloat(ge=0.0)] = Field(
        None, description='Active power currently consumed (counting all phases)'
    )
    totalReactivePower: Optional[confloat(ge=0.0)] = Field(
        None, description='Reactive power currently consumed (counting all phases)'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be StreetlightControlCabinet'
    )
    voltageR: Optional[confloat(ge=0.0)] = Field(
        None, description='Electric tension in phase R'
    )
    voltageS: Optional[confloat(ge=0.0)] = Field(
        None, description='Electric tension in phase S'
    )
    voltageT: Optional[confloat(ge=0.0)] = Field(
        None, description='Electric tension in phase T'
    )
    workingMode: Optional[WorkingMode] = Field(
        None,
        description='Working mode for this cabinet controller.  `automatic` : The cabinet controller decides automatically when light groups are switched on and off. Manual operation is not allowed. `manual` : Human intervention is required for switching on and off. `semiautomatic` : The same as `automatic` but in this case manual intervention is allowed',
    )
