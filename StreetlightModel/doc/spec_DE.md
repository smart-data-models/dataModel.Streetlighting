Entität: StreetlightModel  
=========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightModel/LICENSE.md)  
Globale Beschreibung: **Ein Straßenlampenmodell**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift.  - `alternateName`: Ein alternativer Name für diesen Artikel  - `annotations`: Anmerkungen zum Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `category`: Typ der Kühlstelle, die die Straßenleuchte implementiert. Enum:'`PostTop, Poller, Laternenpfahl, LightTower, Blinkleuchte, SideEntry, SignLight, OrnamentalLantern'. Oder jeder andere Wert, der oben nicht definiert und für die Anwendung sinnvoll ist  - `color`: Die Farbe des Produkts  - `colorRenderingIndex`: Farbwiedergabe-Index der Lampe  - `colorTemperature`: Korrelierte Farbtemperatur der Lampe  - `columnBrandName`: Name der Marke der Säule  - `columnColor`: Die Farbe der Spalte. Erlaubte Werte: Ein Farbschlüsselwort, wie in [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords) angegeben. Ein Farbwert, wie in [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes) angegeben.  - `columnMadeOf`: Material, aus dem die Säule besteht. Enum:'Stahl, Aluminium, Holz, andere'  - `columnManufacturerName`: Name des Herstellers der Säule  - `columnModelName`: Name des Modells der Spalte  - `compliantWith`: Eine Liste der Normen, mit denen dieses Straßenleuchtenmodell konform ist  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `image`: Ein Bild des Artikels  - `lampBrandName`: Name der Marke der Lampe  - `lampManufacturerName`: Name des Herstellers der Lampe.  - `lampModelName`: Name des Modells der Lampe  - `lampTechnology`: Von der Lampe verwendete Technologie. Enum:'LED, LPS, HPS'. Oder jeder andere Wert, der nicht durch die obige Liste abgedeckt und für die Anwendung sinnvoll ist.  - `lampWeight`: Gewicht der Lampe  - `lanternBrandName`: Name der Marke der Laterne  - `lanternManufacturerName`: Name des Herstellers der Laterne  - `lanternModelName`: Name des Modells der Laterne  - `lanternWeight`: Gewicht der Laterne  - `location`:   - `luminousFlux`: Maximale Lichtleistung, die von der Lampe erbracht werden kann  - `maxPowerConsumption`: Maximale Leistungsaufnahme, die von der Laterne unterstützt wird  - `minPowerConsumption`: Minimale Leistungsaufnahme, die von der Laterne unterstützt wird  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `powerConsumption`: (Nenn-)Leistungsaufnahme der Lampe  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `type`: NGSI Entity-Typ. Es muss StreetlightModel sein  - `workingLife`: Die geschätzte Anzahl der Betriebsstunden (der Lampe) ohne Ausfall    
Erforderliche Eigenschaften  
- `id`  - `name`  - `type`    
Es stellt ein Modell einer Straßenlaterne dar, das aus einem spezifischen Tragwerksmodell, einem Laternenmodell und einem Lampenmodell besteht. Eine Straßenlaterneninstanz wird auf einem bestimmten Straßenlaternenmodell basieren.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### StreetlightModel NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein StreetlightModel im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### StreetlightModel NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein StreetlightModel im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
#### StreetlightModel NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein StreetlightModel im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### StreetlightModel NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein StreetlightModel im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "category": [  
    "postTop"  
  ],  
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
  "type": "StreetlightModel"  
}  
```  
