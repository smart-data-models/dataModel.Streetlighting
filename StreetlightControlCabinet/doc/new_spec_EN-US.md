Entity: StreetlightControlCabinet  
=================================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **A Streetlight control cabinet**  

## List of properties  

- `activePowerR`:   - `activePowerS`:   - `activePowerT`:   - `address`: The mailing address.  - `alternateName`: An alternative name for this item  - `annotations`:   - `areaServed`:   - `brandName`:   - `color`: The color of the product.  - `compliantWith`:   - `cosPhi`:   - `cupboardMadeOf`:   - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateLastProgramming`:   - `dateMeteringStarted`:   - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `dateServiceStarted`:   - `description`:   - `energyConsumed`:   - `energyCost`:   - `features`:   - `frequency`:   - `id`:   - `image`: An image of the item.  - `intensityR`:   - `intensityS`:   - `intensityT`:   - `lastMeterReading`:   - `location`:   - `manufacturerName`:   - `maximumPowerAvailable`:   - `meterReadingPeriod`:   - `modelName`:   - `name`: The name of this item.  - `nextActuationDeadline`:   - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `powerFactorR`:   - `powerFactorS`:   - `powerFactorT`:   - `reactiveEnergyConsumed`:   - `reactivePowerR`:   - `reactivePowerS`:   - `reactivePowerT`:   - `refDevice`:   - `refStreetlightGroup`:   - `responsible`:   - `seeAlso`:   - `serialNumber`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `thdrIntensityR`:   - `thdrIntensityS`:   - `thdrIntensityT`:   - `thdrVoltageR`:   - `thdrVoltageS`:   - `thdrVoltageT`:   - `totalActivePower`:   - `totalReactivePower`:   - `type`:   - `voltageR`:   - `voltageS`:   - `voltageT`:   - `workingMode`:   ## Data Model description of properties  
Sorted alphabetically  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StreetlightControlCabinet:    
  description: 'A Streetlight control cabinet'    
  properties:    
    activePowerR:    
      minimum: 0    
      type: number    
    activePowerS:    
      minimum: 0    
      type: number    
    activePowerT:    
      minimum: 0    
      type: number    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      items:    
        type: string    
      type: array    
    areaServed:    
      type: string    
    brandName:    
      type: string    
    color:    
      description: 'The color of the product.'    
      type: string    
    compliantWith:    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
    cosPhi:    
      maximum: 1    
      minimum: -1    
      type: number    
    cupboardMadeOf:    
      enum:    
        - plastic    
        - metal    
        - concrete    
        - other    
      type: string    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateLastProgramming:    
      format: date-time    
      type: string    
    dateMeteringStarted:    
      format: date-time    
      type: string    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateServiceStarted:    
      format: date-time    
      type: string    
    description:    
      type: string    
    energyConsumed:    
      minimum: 0    
      type: number    
    energyCost:    
      minimum: 0    
      type: number    
    features:    
      items:    
        enum:    
          - astronomicalClock    
          - individualControl    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
    frequency:    
      minimum: 0    
      type: number    
    id:    
      anyOf: &streetlightcontrolcabinet_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    image:    
      description: 'An image of the item.'    
      format: uri    
      type: string    
    intensityR:    
      minimum: 0    
      type: number    
    intensityS:    
      minimum: 0    
      type: number    
    intensityT:    
      minimum: 0    
      type: number    
    lastMeterReading:    
      minimum: 0    
      type: number    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    manufacturerName:    
      type: string    
    maximumPowerAvailable:    
      minimum: 0    
      type: number    
    meterReadingPeriod:    
      minimum: 0    
      type: number    
    modelName:    
      type: string    
    name:    
      description: 'The name of this item.'    
      type: Property    
    nextActuationDeadline:    
      format: date-time    
      type: string    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *streetlightcontrolcabinet_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    powerFactorR:    
      maximum: 1    
      minimum: -1    
      type: number    
    powerFactorS:    
      maximum: 1    
      minimum: -1    
      type: number    
    powerFactorT:    
      maximum: 1    
      minimum: -1    
      type: number    
    reactiveEnergyConsumed:    
      minimum: 0    
      type: number    
    reactivePowerR:    
      minimum: 0    
      type: number    
    reactivePowerS:    
      minimum: 0    
      type: number    
    reactivePowerT:    
      minimum: 0    
      type: number    
    refDevice:    
      items:    
        anyOf: *streetlightcontrolcabinet_-_properties_-_owner_-_items_-_anyof    
      minItems: 1    
      type: array    
      uniqueItems: true    
    refStreetlightGroup:    
      items:    
        anyOf: *streetlightcontrolcabinet_-_properties_-_owner_-_items_-_anyof    
      minItems: 1    
      type: array    
      uniqueItems: true    
    responsible:    
      type: string    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    serialNumber:    
      type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    thdrIntensityR:    
      maximum: 1    
      minimum: 0    
      type: number    
    thdrIntensityS:    
      maximum: 1    
      minimum: 0    
      type: number    
    thdrIntensityT:    
      maximum: 1    
      minimum: 0    
      type: number    
    thdrVoltageR:    
      maximum: 1    
      minimum: 0    
      type: number    
    thdrVoltageS:    
      maximum: 1    
      minimum: 0    
      type: number    
    thdrVoltageT:    
      maximum: 1    
      minimum: 0    
      type: number    
    totalActivePower:    
      minimum: 0    
      type: number    
    totalReactivePower:    
      minimum: 0    
      type: number    
    type:    
      enum:    
        - StreetlightControlCabinet    
      type: string    
    voltageR:    
      minimum: 0    
      type: number    
    voltageS:    
      minimum: 0    
      type: number    
    voltageT:    
      minimum: 0    
      type: number    
    workingMode:    
      enum:    
        - automatic    
        - manual    
        - semiautomatic    
      type: string    
  required:    
    - id    
    - type    
    - location    
    - refStreetlightGroup    
    - workingMode    
  type: object    
```  
</details>    
#### StreetlightControlCabinet NGSI V2 key-values Example    
Here is an example of a StreetlightControlCabinet in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "streetlightcontrolcabinet:A45HGJK",  
  "type": "StreetlightControlCabinet",  
  "location": {  
    "type": "Point",  
    "coordinates": [-3.164485591715449, 40.62785133667262]  
  },  
  "cupboardMadeOf": "plastic",  
  "brandName": "Siemens",  
  "modelName": "Simatic S7 1200",  
  "refStreetlightGroup": ["streetlightgroup:BG678", "streetlightgroup:789"],  
  "compliantWith": ["IP54"],  
  "dateLastProgramming": "2016-07-08T16:04:30.201Z",  
  "maximumPowerAvailable": 10,  
  "energyConsumed": 162456,  
  "dateMeteringStarted": "2013-07-07T15:05:59.408Z",  
  "lastMeterReading": 161237,  
  "meterReadingPeriod": 60,  
  "intensityR": 20.1,  
  "intensityS": 14.4,  
  "intensityT": 22,  
  "reactivePowerR": 45,  
  "reactivePowerS": 43.5,  
  "reactivePowerT": 42,  
  "workingMode": "automatic"  
}  
```  
#### StreetlightControlCabinet NGSI V2 normalized Example    
Here is an example of a StreetlightControlCabinet in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "streetlightcontrolcabinet:A45HGJK",  
  "type": "StreetlightControlCabinet",  
  "modelName": {  
    "value": "Simatic S7 1200"  
  },  
  "lastMeterReading": {  
    "value": 161237  
  },  
  "dateMeteringStarted": {  
    "type": "DateTime",  
    "value": "2013-07-07T15:05:59.408Z"  
  },  
  "dateLastProgramming": {  
    "type": "DateTime",  
    "value": "2016-07-08T16:04:30.201Z"  
  },  
  "refStreetlightGroup": {  
    "type": "Relationship",  
    "value": ["streetlightgroup:BG678", "streetlightgroup:789"]  
  },  
  "compliantWith": {  
    "value": ["IP54"]  
  },  
  "intensityR": {  
    "type": "Number",  
    "value": 20.1  
  },  
  "intensityS": {  
    "type": "Number",  
    "value": 14.4  
  },  
  "intensityT": {  
    "type": "Number",  
    "value": 22  
  },  
  "workingMode": {  
    "value": "automatic"  
  },  
  "energyConsumed": {  
    "value": 162456  
  },  
  "meterReadingPeriod": {  
    "value": 60  
  },  
  "cupboardMadeOf": {  
    "value": "plastic"  
  },  
  "brandName": {  
    "value": "Siemens"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-3.164485591715449, 40.62785133667262]  
    }  
  },  
  "reactivePowerR": {  
    "type": "Number",  
    "value": 45  
  },  
  "reactivePowerS": {  
    "type": "Number",  
    "value": 43.5  
  },  
  "reactivePowerT": {  
    "type": "Number",  
    "value": 42  
  },  
  "maximumPowerAvailable": {  
    "value": 10  
  }  
}  
```  
#### StreetlightControlCabinet NGSI-LD key-values Example    
Here is an example of a StreetlightControlCabinet in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "brandName": "Siemens",  
 "compliantWith": ["IP54"],  
 "cupboardMadeOf": "plastic",  
 "dateLastProgramming": {"@type": "DateTime",  
                         "@value": "2016-07-08T16:04:30.201Z"},  
 "dateMeteringStarted": {"@type": "DateTime",  
                         "@value": "2013-07-07T15:05:59.408Z"},  
 "energyConsumed": 162456,  
 "id": "urn:ngsi-ld:StreetlightControlCabinet:streetlightcontrolcabinet:A45HGJK",  
 "intensityR": 20.1,  
 "intensityS": 14.4,  
 "intensityT": 22,  
 "lastMeterReading": 161237,  
 "location": {"coordinates": [-3.164485591715449, 40.62785133667262],  
              "type": "Point"},  
 "maximumPowerAvailable": 10,  
 "meterReadingPeriod": 60,  
 "modelName": "Simatic S7 1200",  
 "reactivePowerR": 45,  
 "reactivePowerS": 43.5,  
 "reactivePowerT": 42,  
 "refStreetlightGroup": ["urn:ngsi-ld:StreetlightGroup:streetlightgroup:BG678",  
                         "urn:ngsi-ld:StreetlightGroup:streetlightgroup:789"],  
 "type": "StreetlightControlCabinet",  
 "workingMode": "automatic"}  
```  
#### StreetlightControlCabinet NGSI-LD normalized Example    
Here is an example of a StreetlightControlCabinet in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:StreetlightControlCabinet:streetlightcontrolcabinet:A45HGJK",  
    "type": "StreetlightControlCabinet",  
    "modelName": {  
        "type": "Property",  
        "value": "Simatic S7 1200"  
    },  
    "lastMeterReading": {  
        "type": "Property",  
        "value": 161237  
    },  
    "dateMeteringStarted": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2013-07-07T15:05:59.408Z"  
        }  
    },  
    "dateLastProgramming": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-07-08T16:04:30.201Z"  
        }  
    },  
    "refStreetlightGroup": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:StreetlightGroup:streetlightgroup:BG678",  
            "urn:ngsi-ld:StreetlightGroup:streetlightgroup:789"  
        ]  
    },  
    "compliantWith": {  
        "type": "Property",  
        "value": [  
            "IP54"  
        ]  
    },  
    "intensityR": {  
        "type": "Property",  
        "value": 20.1  
    },  
    "intensityS": {  
        "type": "Property",  
        "value": 14.4  
    },  
    "intensityT": {  
        "type": "Property",  
        "value": 22  
    },  
    "workingMode": {  
        "type": "Property",  
        "value": "automatic"  
    },  
    "energyConsumed": {  
        "type": "Property",  
        "value": 162456  
    },  
    "meterReadingPeriod": {  
        "type": "Property",  
        "value": 60  
    },  
    "cupboardMadeOf": {  
        "type": "Property",  
        "value": "plastic"  
    },  
    "brandName": {  
        "type": "Property",  
        "value": "Siemens"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -3.164485591715449,  
                40.62785133667262  
            ]  
        }  
    },  
    "reactivePowerR": {  
        "type": "Property",  
        "value": 45  
    },  
    "reactivePowerS": {  
        "type": "Property",  
        "value": 43.5  
    },  
    "reactivePowerT": {  
        "type": "Property",  
        "value": 42  
    },  
    "maximumPowerAvailable": {  
        "type": "Property",  
        "value": 10  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
