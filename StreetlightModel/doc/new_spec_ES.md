Entidad: StreetlightModel  
=========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightModel/LICENSE.md)  
Descripción global: **Modelo de luz de la calle**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `annotations`: Anotaciones sobre el artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `category`: Tipo de activo que implementa la luz de la calle. Enum: "poste, bolardo, farola, torre, faro intermitente, faro lateral, luz de señalización, linterna ornamental". O cualquier otro valor no definido anteriormente y significativo para la aplicación  - `color`: El color del producto  - `colorRenderingIndex`: Índice de reproducción de color de la lámpara  - `colorTemperature`: La temperatura de color de la lámpara está correlacionada  - `columnBrandName`: El nombre de la marca de la columna  - `columnColor`: El color de la pintura de la columna. Valores permitidos: Una palabra clave de color según lo especificado por [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords). Un valor de color según lo especificado por [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)  - `columnMadeOf`: La columna de material está hecha de. Enum:'acero, aluminio, madera, otros'.  - `columnManufacturerName`: Nombre del fabricante de la columna  - `columnModelName`: Nombre del modelo de la columna  - `compliantWith`: Una lista de normas a las que este modelo de farola cumple  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `image`: Una imagen del artículo  - `lampBrandName`: El nombre de la marca de la lámpara  - `lampManufacturerName`: El nombre del fabricante de la lámpara.  - `lampModelName`: Nombre del modelo de la lámpara  - `lampTechnology`: La tecnología usada por la lámpara. Enum:'LED, LPS, HPS'. O cualquier otro valor no cubierto por la lista anterior y significativo para la aplicación.  - `lampWeight`: El peso de la lámpara  - `lanternBrandName`: El nombre de la marca de la linterna  - `lanternManufacturerName`: Nombre del fabricante de la linterna  - `lanternModelName`: Nombre del modelo de la linterna  - `lanternWeight`: El peso de la linterna  - `location`:   - `luminousFlux`: La máxima salida de luz que puede proporcionar la lámpara  - `maxPowerConsumption`: Consumo máximo de energía soportado por la linterna  - `minPowerConsumption`: Consumo mínimo de energía apoyado por la linterna  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `powerConsumption`: El consumo de energía (nominal) de la lámpara  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `type`: Tipo de entidad NGSI. Tiene que ser StreetlightModel  - `workingLife`: El número estimado de horas de trabajo (la lámpara) sin fallas    
Propiedades requeridas  
- `id`  - `name`  - `type`    
Representa un modelo de farola compuesto por un modelo de estructura de soporte específico, un modelo de linterna y un modelo de lámpara. Una instancia de farola se basará en un determinado modelo de farola.  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StreetlightModel:    
  description: 'A Street light model'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    category:    
      description: 'Type of asset which implements the street light. Enum:''`postTop, bollard, lamppost, lightTower, flashingBeacon, sideEntry, signLight, ornamentalLantern''. Or any other value not defined above and meaningful for the application'    
      items:    
        enum:    
          - bollard    
          - flashingBeacon    
          - lamppost    
          - lightTower    
          - ornamentalLantern    
          - postTop    
          - sideEntry    
          - signLight    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
    color:    
      description: 'The color of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
    colorRenderingIndex:    
      description: 'Color rendering index of the lamp'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    colorTemperature:    
      description: 'Correlated color temperature of the lamp'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Kelvin degrees (K)'    
    columnBrandName:    
      description: 'Name of the column''s brand'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/brand.    
    columnColor:    
      description: "Column's painting color. Allowed Values: A color keyword as specified by [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords). A color value as specified by [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)"    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
    columnMadeOf:    
      description: 'Material column is made of. Enum:''steel, aluminium, wood, other'''    
      enum:    
        - steel    
        - aluminium    
        - wood    
        - other    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    columnManufacturerName:    
      description: 'Name of the column''s manufacturer'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/manufacturer    
    columnModelName:    
      description: 'Name of the column''s model'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/model    
    compliantWith:    
      description: 'A list of standards to which this streetlight model is compliant with'    
      items:    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'A description of this item'    
      type: Property    
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
      description: 'Unique identifier of the entity'    
      type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    lampBrandName:    
      description: 'Name of the lamp''s brand'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/brand    
    lampManufacturerName:    
      description: 'Name of the lamp''s manufacturer.'    
      type: Property    
    lampModelName:    
      description: 'Name of the lamp''s model'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/model    
    lampTechnology:    
      description: 'Technology used by the lamp. Enum:''LED, LPS, HPS''. Or any other value not covered by the above list and meaningful to the application.'    
      enum:    
        - LED    
        - LPS    
        - HPS    
      type: Property    
    lampWeight:    
      description: 'Lamp''s weight'    
      type: Property    
      x-ngsi:    
        model: 'Kilograms (kg)'    
        units: 'Kilograms (kg)'    
    lanternBrandName:    
      description: 'Name of the lantern''s brand'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/brand    
    lanternManufacturerName:    
      description: 'Name of the lantern''s manufacturer'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/manufacturer    
    lanternModelName:    
      description: 'Name of the lantern''s model'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    lanternWeight:    
      description: 'Lantern''s weight'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/weight    
        units: 'Kilograms (kg)'    
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
      description: 'Maximum light output which can be provided by the lamp'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Lumens (lm)'    
    maxPowerConsumption:    
      description: 'Maximum power consumption supported by the lantern'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Watts (W).'    
    minPowerConsumption:    
      description: 'Minimum power consumption supported by the lantern'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Watts (W).'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *streetlightmodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    powerConsumption:    
      description: '(Nominal) power consumption made by the lamp'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Watts (W)'    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be StreetlightModel'    
      enum:    
        - StreetlightModel    
      type: Property    
    workingLife:    
      description: 'The estimated number of hours working (the lamp) without failure'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Hours    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### StreetlightModel NGSI V2 key-values Example  
Aquí hay un ejemplo de un StreetlightModel en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### StreetlightModel NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un StreetlightModel en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### StreetlightModel NGSI-LD key-values Example  
Aquí hay un ejemplo de un StreetlightModel en formato JSON-LD como valores clave. Es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### StreetlightModel NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un StreetlightModel en formato JSON-LD normalizado. Es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
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
