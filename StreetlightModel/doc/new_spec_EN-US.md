Entity: StreetlightModel  
========================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **A Street light model**  

## List of properties  

`address`: The mailing address.  `alternateName`:   `annotations`:   `areaServed`: The geographic area where a service or offered item is provided.  `category`:   `color`: The color of the product.  `colorRenderingIndex`:   `colorTemperature`:   `columnBrandName`:   `columnColor`:   `columnMadeOf`:   `columnManufacturerName`:   `columnModelName`:   `compliantWith`:   `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  `description`:   `id`:   `image`:   `lampBrandName`:   `lampManufacturerName`:   `lampModelName`:   `lampTechnology`:   `lampWeight`:   `lanternBrandName`:   `lanternManufacturerName`:   `lanternModelName`:   `lanternWeight`:   `location`:   `luminousFlux`:   `maxPowerConsumption`:   `minPowerConsumption`:   `name`:   `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  `powerConsumption`:   `seeAlso`:   `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  `type`:   `workingLife`:   ## Data Model description of properties  
Sorted alphabetically  
```yaml  
StreetlightModel:    
  description: 'A Street light model'    
  properties:    
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
      type: string    
    annotations:    
      items:    
        type: string    
      type: array    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    category:    
      items:    
        enum:    
          - postTop    
          - bollard    
          - lamppost    
          - lightTower    
          - flashingBeacon    
          - sideEntry    
          - signLight    
          - ornamentalLantern    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
    color:    
      description: 'The color of the product.'    
      type: string    
    colorRenderingIndex:    
      type: number    
    colorTemperature:    
      minimum: 0    
      type: number    
    columnBrandName:    
      type: string    
    columnColor:    
      type: string    
    columnMadeOf:    
      enum:    
        - steel    
        - aluminium    
        - wood    
        - other    
      type: string    
    columnManufacturerName:    
      type: string    
    columnModelName:    
      type: string    
    compliantWith:    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      type: string    
    id:    
      anyOf: &streetlightmodel_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    image:    
      format: uri    
      type: string    
    lampBrandName:    
      type: string    
    lampManufacturerName:    
      type: string    
    lampModelName:    
      type: string    
    lampTechnology:    
      enum:    
        - LED    
        - LPS    
        - HPS    
      type: string    
    lampWeight:    
      type: string    
    lanternBrandName:    
      type: string    
    lanternManufacturerName:    
      type: string    
    lanternModelName:    
      type: string    
    lanternWeight:    
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
    luminousFlux:    
      minimum: 0    
      type: number    
    maxPowerConsumption:    
      minimum: 0    
      type: number    
    minPowerConsumption:    
      minimum: 0    
      type: number    
    name:    
      type: string    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *streetlightmodel_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    powerConsumption:    
      minimum: 0    
      type: number    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      enum:    
        - StreetlightModel    
      type: string    
    workingLife:    
      minimum: 0    
      type: number    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
Here is an example of a StreetlightModel in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "streetlightmodel:TubularNumana:ASR42CG:HPS:100",  
  "type": "StreetlightModel",  
  "name": "Tubular Numana 6M - ASR42CG - Son-T 100",  
  "columnModelName": "01 TUBULAR P/T 6M NUMANA",  
  "columnColor": "green",  
  "lanternModelName": "ASR42CG",  
  "lanternManufacturerName": "Indal WRTL",  
  "lampModelName": "SON-T",  
  "lampBrandName": "Philips",  
  "lampTechnology": "HPS",  
  "powerConsumption": 100,  
  "colorTemperature": 3000,  
  "colorRenderingIndex": 25,  
  "luminousFlux": 2300,  
  "category": ["postTop"]  
}  
```  
Here is an example of a StreetlightModel in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "streetlightmodel:TubularNumana:ASR42CG:HPS:100",  
  "type": "StreetlightModel",  
  "category": {  
    "value": ["postTop"]  
  },  
  "colorRenderingIndex": {  
    "value": 25  
  },  
  "columnColor": {  
    "value": "green"  
  },  
  "name": {  
    "value": "Tubular Numana 6M - ASR42CG - Son-T 100"  
  },  
  "powerConsumption": {  
    "value": 100  
  },  
  "lanternManufacturerName": {  
    "value": "Indal WRTL"  
  },  
  "luminousFlux": {  
    "value": 2300  
  },  
  "lampTechnology": {  
    "value": "HPS"  
  },  
  "colorTemperature": {  
    "value": 3000  
  },  
  "lanternModelName": {  
    "value": "ASR42CG"  
  },  
  "columnModelName": {  
    "value": "01 TUBULAR P/T 6M NUMANA"  
  },  
  "lampModelName": {  
    "value": "SON-T"  
  },  
  "lampBrandName": {  
    "value": "Philips"  
  }  
}  
```  
Here is an example of a StreetlightModel in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "category": ["postTop"],  
 "colorRenderingIndex": 25,  
 "colorTemperature": 3000,  
 "columnColor": "green",  
 "columnModelName": "01 TUBULAR P/T 6M NUMANA",  
 "id": "urn:ngsi-ld:StreetlightModel:streetlightmodel:TubularNumana:ASR42CG:HPS:100",  
 "lampBrandName": "Philips",  
 "lampModelName": "SON-T",  
 "lampTechnology": "HPS",  
 "lanternManufacturerName": "Indal WRTL",  
 "lanternModelName": "ASR42CG",  
 "luminousFlux": 2300,  
 "name": "Tubular Numana 6M - ASR42CG - Son-T 100",  
 "powerConsumption": 100,  
 "type": "StreetlightModel"}  
```  
Here is an example of a StreetlightModel in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:StreetlightModel:streetlightmodel:TubularNumana:ASR42CG:HPS:100",  
    "type": "StreetlightModel",  
    "category": {  
        "type": "Property",  
        "value": [  
            "postTop"  
        ]  
    },  
    "colorRenderingIndex": {  
        "type": "Property",  
        "value": 25  
    },  
    "columnColor": {  
        "type": "Property",  
        "value": "green"  
    },  
    "name": {  
        "type": "Property",  
        "value": "Tubular Numana 6M - ASR42CG - Son-T 100"  
    },  
    "powerConsumption": {  
        "type": "Property",  
        "value": 100  
    },  
    "lanternManufacturerName": {  
        "type": "Property",  
        "value": "Indal WRTL"  
    },  
    "luminousFlux": {  
        "type": "Property",  
        "value": 2300  
    },  
    "lampTechnology": {  
        "type": "Property",  
        "value": "HPS"  
    },  
    "colorTemperature": {  
        "type": "Property",  
        "value": 3000  
    },  
    "lanternModelName": {  
        "type": "Property",  
        "value": "ASR42CG"  
    },  
    "columnModelName": {  
        "type": "Property",  
        "value": "01 TUBULAR P/T 6M NUMANA"  
    },  
    "lampModelName": {  
        "type": "Property",  
        "value": "SON-T"  
    },  
    "lampBrandName": {  
        "type": "Property",  
        "value": "Philips"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
