<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: StreetlightGroup  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightGroup/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Eine Gruppe von Straßenlampen**  
Version: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `activeProgramId[string]`: Kennung des aktiven Programms für diese Straßenlampengruppe  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `annotations[array]`: Ein Feld, das für Anmerkungen (Vorkommnisse, Bemerkungen usw.) reserviert ist.  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: Die Farbe des Produkts  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateLastSwitchingOff[date-time]`: Zeitstempel des letzten Ausschaltens  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateLastSwitchingOn[date-time]`: Zeitstempel des letzten Einschaltens  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `illuminanceLevel[number]`: Einstellung der relativen Beleuchtungsstärke für die Gruppe. Erlaubte Werte: Eine Zahl zwischen 0 und 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `image[uri]`: Ein Bild des Artikels  . Model: [https://schema.org/URL](https://schema.org/URL)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `powerState[string]`: Stromversorgungszustand der Straßenleuchtengruppe. Enum:'on, off, low, bootingUp'. Enum:'bootingUp, niedrig, aus, an'  . Model: [htts://schema.org/Text](htts://schema.org/Text)- `refStreetlight[array]`: Liste der Straßenlaternen-Entitäten, die zu dieser Gruppe gehören. Liste der Verweise auf Entitäten des Typs Straßenlaterne. Erlaubte Werte: Zwischen dem Standort der Gruppe und dem der einzelnen Straßenlaternen muss topografische Integrität bestehen  - `refStreetlightControlCabinet[*]`: Schaltschrank der Straßenbeleuchtungsgruppe  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `switchingMode[array]`: Zeitstempel des zuletzt vorgenommenen Lampenwechsels. Enum:' night-ON, night-OFF, night-LOW, always-ON, day-ON, day-OFF, day-LOW'  - `switchingOnHours[array]`: Einschaltzeiten. Sie wird normalerweise verwendet, um spezielle Zeitpläne für bestimmte Daten festzulegen  - `type[string]`: NGSI-Entitätstyp. Es muss StreetlightGroup sein  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Ein Objekt des Typs `StreetlightGroup` stellt eine Gruppe von Straßenleuchten dar. Sie können gemeinsam von demselben automatischen System (Schaltschranksteuerung) gesteuert werden.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StreetlightGroup:    
  description: A Street light group    
  properties:    
    activeProgramId:    
      description: Identifier of the active program for this streetlight group    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: Annotations about the item    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    color:    
      description: The color of the product    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateLastSwitchingOff:    
      description: Timestamp of the last switching off    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateLastSwitchingOn:    
      description: Timestamp of the last switching on    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    illuminanceLevel:    
      description: 'Relative illuminance level setting for the group. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    image:    
      description: An image of the item    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    powerState:    
      description: 'Streetlight group''s power state. Enum:''on, off, low, bootingUp''. Enum:''bootingUp, low, off, on'''    
      enum:    
        - bootingUp    
        - low    
        - off    
        - on    
      type: string    
      x-ngsi:    
        model: htts://schema.org/Text    
        type: Property    
    refStreetlight:    
      description: 'List of streetlight entities belonging to this group. List of references to entities fo type Streetlight. Allowed values: There must topographical integrity between the location of the group and of the individual streetlights'    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Relationship    
    refStreetlightControlCabinet:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Streetlight group's control cabinet    
      x-ngsi:    
        type: Relationship    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
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
      type: array    
      x-ngsi:    
        type: Property    
    switchingOnHours:    
      description: Switching on hours. It is used normally to set special schedules for certain dates    
      items:    
        properties:    
          description:    
            description: Timestamp of the last change of lamp made    
            type: string    
            x-ngsi:    
              type: Property    
          from:    
            anyOf:    
              - format: date    
              - pattern: ^--((0[13578]|1[02])-31|(0[1,3-9]|1[0-2])-30|(0\d|1[0-2])-([0-2]\d))$    
                type: string    
            type: string    
          hours:    
            description: Timestamp of the last change of lamp made    
            type: string    
            x-ngsi:    
              type: Property    
          to:    
            anyOf:    
              - format: date    
              - pattern: ^--((0[13578]|1[02])-31|(0[1,3-9]|1[0-2])-30|(0\d|1[0-2])-([0-2]\d))$    
                type: string    
            description: Ending date (it can be yearless)    
            type: string    
            x-ngsi:    
              type: Property    
        required:    
          - from    
          - to    
          - hours    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be StreetlightGroup    
      enum:    
        - StreetlightGroup    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/StreetlightGroup/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Streetlighting/Streetlight/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### StreetlightGroup NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine StreetlightGroup im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "streetlightgroup:mycity:A12",  
  "type": "StreetlightGroup",  
  "location": {  
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
</details>  
#### StreetlightGroup NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine StreetlightGroup im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "streetlightgroup:mycity:A12",  
  "type": "StreetlightGroup",  
  "circuitId": {  
    "type": "Text",  
    "value": "C-456-A467"  
  },  
  "powerState": {  
    "type": "Text",  
    "value": "on"  
  },  
  "dateLastSwitchingOn": {  
    "type": "DateTime",  
    "value": "2016-07-07T19:59:06.618Z"  
  },  
  "refStreetlightCabinetController": {  
    "type": "Text",  
    "value": "cabinetcontroller:CC45A34"  
  },  
  "dateLastSwitchingOff": {  
    "type": "DateTime",  
    "value": "2016-07-07T07:59:06.618Z"  
  },  
  "switchingOnHours": {  
    "type": "StructuredValue",  
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
    "type": "Text",  
    "value": "Calle Comercial Centro"  
  }  
}  
```  
</details>  
#### StreetlightGroup NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine StreetlightGroup im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:mycity:A12",  
  "type": "StreetlightGroup",  
  "areaServed": "Calle Comercial Centro",  
  "circuitId": "C-456-A467",  
  "dateLastSwitchingOff": "2016-07-07T07:59:06.618Z",  
  "dateLastSwitchingOn": "2016-07-07T19:59:06.618Z",  
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
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### StreetlightGroup NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine StreetlightGroup im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:mycity:A12",  
  "type": "StreetlightGroup",  
  "areaServed": {  
    "type": "Property",  
    "value": "Calle Comercial Centro"  
  },  
  "circuitId": {  
    "type": "Property",  
    "value": "C-456-A467"  
  },  
  "dateLastSwitchingOff": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-07-07T07:59:06.618Z"  
    }  
  },  
  "dateLastSwitchingOn": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-07-07T19:59:06.618Z"  
    }  
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
  "powerState": {  
    "type": "Property",  
    "value": "on"  
  },  
  "refStreetlightCabinetController": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:StreetlightCabinetController:cabinetcontroller:CC45A34"  
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
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
