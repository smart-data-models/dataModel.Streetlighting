Entity: StreetlightGroup  
========================  
[Open License](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightGroup/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **A Street light group**  

## List of properties  

- `activeProgramId`: Identifier of the active program for this streetlight group  - `address`: The mailing address  - `alternateName`: An alternative name for this item  - `annotations`: A field reserved for annotations (incidences, remarks, etc.).  - `areaServed`: The geographic area where a service or offered item is provided  - `color`: The color of the product  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateLastSwitchingOff`: Timestamp of the last switching off  - `dateLastSwitchingOn`: Timestamp of the last switching on  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `id`: Unique identifier of the entity  - `illuminanceLevel`: Relative illuminance level setting for the group. Allowed values: A number between 0 and 1  - `image`: An image of the item  - `location`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `powerState`: Streetlight group's power state. Enum:'on, off, low, bootingUp'  - `refStreetlight`: List of streetlight entities belonging to this group. List of references to entities fo type Streetlight. Allowed values: There must topographical integrity between the location of the group and of the individual streetlights.  - `refStreetlightControlCabinet`: Streetlight group's control cabinet  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `switchingMode`: Timestamp of the last change of lamp made. Enum:' night-ON, night-OFF, night-LOW, always-ON, day-ON, day-OFF, day-LOW'  - `switchingOnHours`: Switching on hours. It is used normally to set special schedules for certain dates.  - `type`: NGSI Entity type. It has to be StreetlightGroup    
Required properties  
- `id`  - `location`  - `type`    
An entity of type `StreetlightGroup` represents a group of streetlights. They might be controlled together by the same automated system (cabinet controller).  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StreetlightGroup:    
  description: 'A Street light group'    
  properties:    
    activeProgramId:    
      description: 'Identifier of the active program for this streetlight group'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      description: 'A field reserved for annotations (incidences, remarks, etc.).'    
      items:    
        type: string    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    color:    
      description: 'The color of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateLastSwitchingOff:    
      description: 'Timestamp of the last switching off'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateLastSwitchingOn:    
      description: 'Timestamp of the last switching on'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &streetlightgroup_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    illuminanceLevel:    
      description: 'Relative illuminance level setting for the group. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *streetlightgroup_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    powerState:    
      description: 'Streetlight group''s power state. Enum:''on, off, low, bootingUp'''    
      enum:    
        - on    
        - off    
        - low    
        - bootingUp    
      type: Property    
      x-ngsi:    
        model: htts://schema.org/Text    
    refStreetlight:    
      description: 'List of streetlight entities belonging to this group. List of references to entities fo type Streetlight. Allowed values: There must topographical integrity between the location of the group and of the individual streetlights.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      minItems: 1    
      type: Relationship    
      uniqueItems: true    
    refStreetlightControlCabinet:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Streetlight group''s control cabinet'    
      type: Relationship    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    switchingMode:    
      description: 'Timestamp of the last change of lamp made. Enum:'' night-ON, night-OFF, night-LOW, always-ON, day-ON, day-OFF, day-LOW'''    
      items:    
        enum:    
          - night-ON    
          - night-OFF    
          - night-LOW    
          - always-ON    
          - day-ON    
          - day-OFF    
          - day-LOW    
        type: string    
      type: Property    
    switchingOnHours:    
      description: 'Switching on hours. It is used normally to set special schedules for certain dates.'    
      items:    
        properties:    
          description:    
            description: 'Property. Timestamp of the last change of lamp made'    
            type: string    
          from:    
            oneOf:    
              - format: date    
              - pattern: ^--((0[13578]|1[02])-31|(0[1,3-9]|1[0-2])-30|(0\d|1[0-2])-([0-2]\d))$    
                type: string    
            type: string    
          hours:    
            description: 'Property. Timestamp of the last change of lamp made'    
            type: string    
          to:    
            description: 'Property. Ending date (it can be yearless)'    
            oneOf:    
              - format: date    
              - pattern: ^--((0[13578]|1[02])-31|(0[1,3-9]|1[0-2])-30|(0\d|1[0-2])-([0-2]\d))$    
                type: string    
            type: string    
        required:    
          - from    
          - to    
          - hours    
        type: object    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be StreetlightGroup'    
      enum:    
        - StreetlightGroup    
      type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
```  
</details>    
## Example payloads    
#### StreetlightGroup NGSI-v2 key-values Example    
Here is an example of a StreetlightGroup in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "streetlightgroup:mycity:A12",  
  "type": "StreetlightGroup",  
  "location": {  
    "type": "MultiLineString",  
    "coordinates": [[[100.0, 0.0], [101.0, 1.0]], [[102.0, 2.0], [103.0, 3.0]]]  
  },  
  "powerState": "on",  
  "areaServed": "Calle Comercial Centro",  
  "circuitId": "C-456-A467",  
  "dateLastSwitchingOn": "2016-07-07T19:59:06.618Z",  
  "dateLastSwitchingOff": "2016-07-07T07:59:06.618Z",  
  "refStreetlightCabinetController": "cabinetcontroller:CC45A34",  
  "switchingOnHours": [  
    {  
      "from": "--11-30",  
      "to": "--01-07",  
      "hours": "Mo,Su 16:00-02:00",  
      "description": "Christmas"  
    }  
  ]  
}  
```  
#### StreetlightGroup NGSI-v2 normalized Example    
Here is an example of a StreetlightGroup in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "streetlightgroup:mycity:A12",  
  "type": "StreetlightGroup",  
  "circuitId": {  
    "value": "C-456-A467"  
  },  
  "powerState": {  
    "value": "on"  
  },  
  "dateLastSwitchingOn": {  
    "type": "DateTime",  
    "value": "2016-07-07T19:59:06.618Z"  
  },  
  "refStreetlightCabinetController": {  
    "type": "Relationship",  
    "value": "cabinetcontroller:CC45A34"  
  },  
  "dateLastSwitchingOff": {  
    "type": "DateTime",  
    "value": "2016-07-07T07:59:06.618Z"  
  },  
  "switchingOnHours": {  
    "value": [  
      {  
        "hours": "Mo,Su 16:00-02:00",  
        "to": "--01-07",  
        "from": "--11-30",  
        "description": "Christmas"  
      }  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "MultiLineString",  
      "coordinates": [  
        [[100.0, 0.0], [101.0, 1.0]],  
        [[102.0, 2.0], [103.0, 3.0]]  
      ]  
    }  
  },  
  "areaServed": {  
    "value": "Calle Comercial Centro"  
  }  
}  
```  
#### StreetlightGroup NGSI-LD key-values Example    
Here is an example of a StreetlightGroup in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:mycity:A12",  
  "type": "StreetlightGroup",  
  "circuitId": {  
    "type": "Property",  
    "value": "C-456-A467"  
  },  
  "powerState": {  
    "type": "Property",  
    "value": "on"  
  },  
  "dateLastSwitchingOn": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-07-07T19:59:06.618Z"  
    }  
  },  
  "refStreetlightCabinetController": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:StreetlightCabinetController:cabinetcontroller:CC45A34"  
  },  
  "dateLastSwitchingOff": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-07-07T07:59:06.618Z"  
    }  
  },  
  "switchingOnHours": {  
    "type": "Property",  
    "value": [  
      {  
        "hours": "Mo,Su 16:00-02:00",  
        "to": "--01-07",  
        "from": "--11-30",  
        "description": "Christmas"  
      }  
    ]  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "MultiLineString",  
      "coordinates": [  
        [  
          [  
            100.0,  
            0.0  
          ],  
          [  
            101.0,  
            1.0  
          ]  
        ],  
        [  
          [  
            102.0,  
            2.0  
          ],  
          [  
            103.0,  
            3.0  
          ]  
        ]  
      ]  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Calle Comercial Centro"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### StreetlightGroup NGSI-LD normalized Example    
Here is an example of a StreetlightGroup in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "areaServed": "Calle Comercial Centro",  
  "circuitId": "C-456-A467",  
  "dateLastSwitchingOff": {  
    "@type": "DateTime",  
    "@value": "2016-07-07T07:59:06.618Z"  
  },  
  "dateLastSwitchingOn": {  
    "@type": "DateTime",  
    "@value": "2016-07-07T19:59:06.618Z"  
  },  
  "id": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:mycity:A12",  
  "location": {  
    "coordinates": [  
      [  
        [  
          100.0,  
          0.0  
        ],  
        [  
          101.0,  
          1.0  
        ]  
      ],  
      [  
        [  
          102.0,  
          2.0  
        ],  
        [  
          103.0,  
          3.0  
        ]  
      ]  
    ],  
    "type": "MultiLineString"  
  },  
  "powerState": "on",  
  "refStreetlightCabinetController": "urn:ngsi-ld:StreetlightCabinetController:cabinetcontroller:CC45A34",  
  "switchingOnHours": [  
    {  
      "description": "Christmas",  
      "from": "--11-30",  
      "hours": "Mo,Su 16:00-02:00",  
      "to": "--01-07"  
    }  
  ],  
  "type": "StreetlightGroup"  
}  
```  
