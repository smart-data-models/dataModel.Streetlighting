<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: StreetlightModel  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightModel/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Un modelo de farola**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `annotations[array]`: Anotaciones sobre el artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: Tipo de bien que implementa la luz de la calle. Enum:'`postTop, bollard, lamppost, lightTower, flashingBeacon, sideEntry, signLight, ornamentalLantern'. O cualquier otro valor no definido anteriormente y significativo para la aplicación  - `color[string]`: El color del producto  . Model: [https://schema.org/color](https://schema.org/color)- `colorRenderingIndex[number]`: Índice de reproducción cromática de la lámpara  . Model: [https://schema.org/Number](https://schema.org/Number)- `colorTemperature[number]`: Temperatura de color correlativa de la lámpara  . Model: [https://schema.org/Number](https://schema.org/Number)- `columnBrandName[string]`: Nombre de la marca de la columna  . Model: [https://schema.org/brand.](https://schema.org/brand.)- `columnColor[string]`: Color de pintura de la columna. Valores permitidos: Una palabra clave de color como se especifica en [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords). Un valor de color como se especifica en [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)  . Model: [https://schema.org/color](https://schema.org/color)- `columnMadeOf[string]`: La columna de material está hecha. Enum:'acero, aluminio, madera, otros'  . Model: [https://schema.org/Text](https://schema.org/Text)- `columnManufacturerName[string]`: Nombre del fabricante de la columna  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `columnModelName[string]`: Nombre del modelo de la columna  . Model: [https://schema.org/model](https://schema.org/model)- `compliantWith[array]`: Lista de normas que cumple este modelo de farola  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `image[string]`: Una imagen del artículo  . Model: [https://schema.org/URL](https://schema.org/URL)- `lampBrandName[string]`: Nombre de la marca de la lámpara  . Model: [https://schema.org/brand](https://schema.org/brand)- `lampManufacturerName[string]`: Nombre del fabricante de la lámpara.  - `lampModelName[string]`: Nombre del modelo de lámpara  . Model: [https://schema.org/model](https://schema.org/model)- `lampTechnology[string]`: Tecnología utilizada por la lámpara. Enum:'LED, LPS, HPS'. O cualquier otro valor no contemplado en la lista anterior y significativo para la aplicación.  - `lampWeight[string]`: Peso de la lámpara  . Model: [Kilograms (kg)](Kilograms (kg))- `lanternBrandName[string]`: Nombre de la marca de la linterna  . Model: [https://schema.org/brand](https://schema.org/brand)- `lanternManufacturerName[string]`: Nombre del fabricante de la linterna  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `lanternModelName[string]`: Nombre del modelo de linterna  . Model: [https://schema.org/Text](https://schema.org/Text)- `lanternWeight[number]`: Peso de la linterna  . Model: [https://schema.org/weight](https://schema.org/weight)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `luminousFlux[number]`: Máxima potencia lumínica que puede proporcionar la lámpara  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxPowerConsumption[number]`: Consumo máximo de energía soportado por la linterna  . Model: [https://schema.org/Number](https://schema.org/Number)- `minPowerConsumption[number]`: Consumo mínimo de energía soportado por la linterna  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: El nombre de este artículo.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `powerConsumption[number]`: Consumo de energía (nominal) realizado por la lámpara  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser StreetlightModel  - `workingLife[number]`: El número estimado de horas de funcionamiento (de la lámpara) sin fallos  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Representa un modelo de farola compuesto por un modelo de estructura de soporte específico, un modelo de farola y un modelo de lámpara. Una instancia de farola se basará en un determinado modelo de farola.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StreetlightModel:    
  description: 'A Street light model'    
  properties:    
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
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    colorRenderingIndex:    
      description: 'Color rendering index of the lamp'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    colorTemperature:    
      description: 'Correlated color temperature of the lamp'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kelvin degrees (K)'    
    columnBrandName:    
      description: 'Name of the column''s brand'    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand.    
        type: Property    
    columnColor:    
      description: "Column's painting color. Allowed Values: A color keyword as specified by [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords). A color value as specified by [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    columnMadeOf:    
      description: 'Material column is made of. Enum:''steel, aluminium, wood, other'''    
      enum:    
        - steel    
        - aluminium    
        - wood    
        - other    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    columnManufacturerName:    
      description: 'Name of the column''s manufacturer'    
      type: string    
      x-ngsi:    
        model: https://schema.org/manufacturer    
        type: Property    
    columnModelName:    
      description: 'Name of the column''s model'    
      type: string    
      x-ngsi:    
        model: https://schema.org/model    
        type: Property    
    compliantWith:    
      description: 'A list of standards to which this streetlight model is compliant with'    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    lampBrandName:    
      description: 'Name of the lamp''s brand'    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
    lampManufacturerName:    
      description: 'Name of the lamp''s manufacturer.'    
      type: string    
      x-ngsi:    
        type: Property    
    lampModelName:    
      description: 'Name of the lamp''s model'    
      type: string    
      x-ngsi:    
        model: https://schema.org/model    
        type: Property    
    lampTechnology:    
      description: 'Technology used by the lamp. Enum:''LED, LPS, HPS''. Or any other value not covered by the above list and meaningful to the application.'    
      enum:    
        - LED    
        - LPS    
        - HPS    
      type: string    
      x-ngsi:    
        type: Property    
    lampWeight:    
      description: 'Lamp''s weight'    
      type: string    
      x-ngsi:    
        model: 'Kilograms (kg)'    
        type: Property    
        units: 'Kilograms (kg)'    
    lanternBrandName:    
      description: 'Name of the lantern''s brand'    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
    lanternManufacturerName:    
      description: 'Name of the lantern''s manufacturer'    
      type: string    
      x-ngsi:    
        model: https://schema.org/manufacturer    
        type: Property    
    lanternModelName:    
      description: 'Name of the lantern''s model'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    lanternWeight:    
      description: 'Lantern''s weight'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weight    
        type: Property    
        units: 'Kilograms (kg)'    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      x-ngsi:    
        type: Geoproperty    
    luminousFlux:    
      description: 'Maximum light output which can be provided by the lamp'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Lumens (lm)'    
    maxPowerConsumption:    
      description: 'Maximum power consumption supported by the lantern'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Watts (W).'    
    minPowerConsumption:    
      description: 'Minimum power consumption supported by the lantern'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Watts (W).'    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *streetlightmodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    powerConsumption:    
      description: '(Nominal) power consumption made by the lamp'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Watts (W)'    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be StreetlightModel'    
      enum:    
        - StreetlightModel    
      type: string    
      x-ngsi:    
        type: Property    
    workingLife:    
      description: 'The estimated number of hours working (the lamp) without failure'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Hours    
  required:    
    - id    
    - type    
    - name    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/StreetlightModel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Streetlighting/Streetlight/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### StreetlightModel NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un StreetlightModel en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### StreetlightModel NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un StreetlightModel en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### StreetlightModel NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un StreetlightModel en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:StreetlightModel:streetlightmodel:TubularNumana:ASR42CG:HPS:100",  
    "type": "StreetlightModel",  
    "category": [  
        "postTop"  
    ],  
    "colorRenderingIndex": 25,  
    "colorTemperature": 3000,  
    "columnColor": "green",  
    "columnModelName": "01 TUBULAR P/T 6M NUMANA",  
    "lampBrandName": "Philips",  
    "lampModelName": "SON-T",  
    "lampTechnology": "HPS",  
    "lanternManufacturerName": "Indal WRTL",  
    "lanternModelName": "ASR42CG",  
    "luminousFlux": 2300,  
    "name": "Tubular Numana 6M - ASR42CG - Son-T 100",  
    "powerConsumption": 100,  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### StreetlightModel NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un StreetlightModel en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
    "colorTemperature": {  
        "type": "Property",  
        "value": 3000  
    },  
    "columnColor": {  
        "type": "Property",  
        "value": "green"  
    },  
    "columnModelName": {  
        "type": "Property",  
        "value": "01 TUBULAR P/T 6M NUMANA"  
    },  
    "lampBrandName": {  
        "type": "Property",  
        "value": "Philips"  
    },  
    "lampModelName": {  
        "type": "Property",  
        "value": "SON-T"  
    },  
    "lampTechnology": {  
        "type": "Property",  
        "value": "HPS"  
    },  
    "lanternManufacturerName": {  
        "type": "Property",  
        "value": "Indal WRTL"  
    },  
    "lanternModelName": {  
        "type": "Property",  
        "value": "ASR42CG"  
    },  
    "luminousFlux": {  
        "type": "Property",  
        "value": 2300  
    },  
    "name": {  
        "type": "Property",  
        "value": "Tubular Numana 6M - ASR42CG - Son-T 100"  
    },  
    "powerConsumption": {  
        "type": "Property",  
        "value": 100  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
