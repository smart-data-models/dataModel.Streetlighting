Entität: Straßenlaterne  
=======================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/Streetlight/LICENSE.md)  
Globale Beschreibung: **Eine Straßenleuchte**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift.  - `alternateName`: Ein alternativer Name für diesen Artikel  - `annotations`: Ein Feld, das für Anmerkungen (Vorkommnisse, Bemerkungen usw.) reserviert ist.  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `circuit`: Der Stromkreis, an den diese Straßenlaterne angeschlossen ist und von dem sie Strom bezieht. In der Regel enthält er eine Kennung, die es ermöglicht, weitere Informationen über diesen Stromkreis zu erhalten.  - `color`: Die Farbe des Produkts  - `controllingMethod`: Die Methode, die zur Steuerung dieser Straßenlaterne verwendet wird. Enum:'Gruppe, individuell'.  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateLastLampChange`: Zeitstempel des zuletzt durchgeführten Lampenwechsels  - `dateLastSwitchingOff`: Zeitstempel des letzten Ausschaltens  - `dateLastSwitchingOn`: Zeitstempel des letzten Einschaltens  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `dateServiceStarted`: Datum, an dem die Straßenlaterne ihren Betrieb aufgenommen hat  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `illuminanceLevel`: Einstellung der relativen Beleuchtungsstärke. Eine Zahl zwischen 0 und 1.  - `image`: Eine URL, die ein Foto der Straßenlaterne enthält  - `laternHeight`: Die Höhe der Laterne. Bei Säulen mit vielen Armen kann dies zwischen den Straßenleuchten variieren. Eine weitere Variationsquelle für diese Eigenschaft sind wandmontierte Straßenleuchten.  - `location`:   - `locationCategory`: Kategorie des Ortes, an dem die Straßenleuchte platziert ist. Enum:'Brücke, centralIsland, Fassade, Garten, Park, Parkplatz, pedestrianPath, Spielplatz, Straße, Gehweg, Tunnel'  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `powerState`: Stromversorgungszustand der Straßenlaterne. Enum:'bootingUp, low, off, on'  - `refDevice`: Verweis auf das/die Gerät(e), das/die zur Überwachung dieser Straßenlaterne verwendet wird/werden. Liste der Referenz auf die Entität(en) vom Typ Gerät.  - `refStreetlightControlCabinet`: Wenn diese Straßenleuchte individuell gesteuert wird, verweisen Sie auf den zuständigen Schaltschrank.  - `refStreetlightGroup`: Gruppe der Straßenlaterne, wenn diese Straßenlaterne zu einer Gruppe gehört.  - `refStreetlightModel`: Das Modell der Straßenlaterne.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `status`: Der Gesamtstatus dieser Straßenlaterne. Enum:'brokenLantern, columnIssue, defectiveLamp, ok'  - `type`: NGSI Entity-Typ. Es muss Streetlight sein    
Erforderliche Eigenschaften  
- `id`  - `location`  - `status`  - `type`    
Eine Entität vom Typ `Streetlight` repräsentiert eine städtische Straßenlaterne. Eigentlich gibt es pro Lampe eine Entität vom Typ `Streetlight`. Wenn also ein bestimmter Mast mehr als eine Laterne hält, gibt es so viele Streetlight-Entitäten wie installierte Lampen. Infolgedessen kann es mehr als eine Streetlight-Entität pro Standort geben. Eine "Streetlight"-Entität enthält kein Attribut, das den strukturellen Merkmalen entspricht. Solche Daten werden von Entitäten des Typs `StreetlightModel` erfasst.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Streetlight:    
  description: 'A Street light'    
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
      description: 'A field reserved for annotations (incidences, remarks, etc.).'    
      items:    
        type: string    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    circuit:    
      description: 'The circuit to which this streetlight connects to and gets power from. Typically it will contain an identifier that will allow to obtain more information about such circuit.'    
      type: Property    
    color:    
      description: 'The color of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
    controllingMethod:    
      description: 'The method used to control this streetlight. Enum:''group, individual''. '    
      enum:    
        - group    
        - individual    
      type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateLastLampChange:    
      description: 'Timestamp of the last change of lamp made'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateLastSwitchingOff:    
      description: 'Timestamp of the last switching off'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateLastSwitchingOn:    
      description: 'Timestamp of the last switching on'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateServiceStarted:    
      description: 'Date at which the streetlight started giving service'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Date    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &streetlight_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Relative illuminance level setting. A number between 0 and 1.'    
      maximum: 1    
      minimum: 0    
      type: Property    
    image:    
      description: 'A URL containing a photo of the streetlight'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/image    
    laternHeight:    
      description: 'Lantern''s height. In columns with many arms this can vary between streetlights. Another variation source of this property are wall-mounted streetlights.'    
      minimum: 0    
      type: Property    
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
    locationCategory:    
      description: 'Category of the location where the streetlight is placed. Enum:''bridge, centralIsland, façade, garden, park, parking, pedestrianPath, playground, road, sidewalk, tunnel'''    
      enum:    
        - bridge    
        - centralIsland    
        - façade    
        - garden    
        - park    
        - parking    
        - pedestrianPath    
        - playground    
        - road    
        - sidewalk    
        - tunnel    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *streetlight_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    powerState:    
      description: 'Streetlight''s power state. Enum:''bootingUp, low, off, on'''    
      enum:    
        - bootingUp    
        - low    
        - off    
        - on    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    refDevice:    
      description: 'Reference to the device(s) used to monitor this streetligth. List of Reference to entity(ies) of type Device.'    
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
      description: 'If this streetlight is individually controlled, reference to the control cabinet in charge of.'    
      type: Relationship    
    refStreetlightGroup:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Streetlight''s group, if this streetlight belongs to any group.'    
      type: Relationship    
    refStreetlightModel:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Streetlight''s model.'    
      type: Relationship    
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
    status:    
      description: 'The overall status of this street light. Enum:''brokenLantern, columnIssue, defectiveLamp, ok'''    
      enum:    
        - brokenLantern    
        - columnIssue    
        - defectiveLamp    
        - ok    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Streetlight'    
      enum:    
        - Streetlight    
      type: Property    
  required:    
    - id    
    - type    
    - location    
    - status    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### Straßenleuchte NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine Straßenlaterne im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "streetlight:guadalajara:4567",  
  "type": "Streetlight",  
  "location": {  
    "type": "Point",  
    "coordinates": [-3.164485591715449, 40.62785133667262]  
  },  
  "areaServed": "Roundabouts city entrance",  
  "status": "ok",  
  "refStreetlightGroup": "streetlightgroup:G345",  
  "refStreetlightModel": "streetlightmodel:STEEL_Tubular_10m",  
  "circuit": "C-456-A467",  
  "lanternHeight": 10,  
  "locationCategory": "centralIsland",  
  "powerState": "off",  
  "controllingMethod": "individual",  
  "dateLastLampChange": "2016-07-08T08:02:21.753Z"  
}  
```  
#### Straßenleuchte NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine Straßenlaterne im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "streetlight:guadalajara:4567",  
  "type": "Streetlight",  
  "location": {  
    "value": {  
      "type": "Point",  
      "coordinates": [-3.164485591715449, 40.62785133667262]  
    },  
    "type": "geo:json"  
  },  
  "areaServed": {  
    "value": "Roundabouts city entrance"  
  },  
  "status": {  
    "value": "ok"  
  },  
  "refStreetlightGroup": {  
    "value": "streetlightgroup:G345",  
    "type": "Relationship"  
  },  
  "refStreetlightModel": {  
    "value": "streetlightmodel:STEEL_Tubular_10m",  
    "type": "Relationship"  
  },  
  "circuit": {  
    "value": "C-456-A467"  
  },  
  "lanternHeight": {  
    "value": 10  
  },  
  "locationCategory": {  
    "value": "centralIsland"  
  },  
  "powerState": {  
    "value": "off"  
  },  
  "controllingMethod": {  
    "value": "individual"  
  },  
  "dateLastLampChange": {  
    "value": "2016-07-08T08:02:21.753Z",  
    "type": "DateTime"  
  }  
}  
```  
#### Straßenleuchte NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine Straßenlaterne im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Streetlight:streetlight:guadalajara:4567",  
  "type": "Streetlight",  
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
  "areaServed": {  
    "type": "Property",  
    "value": "Roundabouts city entrance"  
  },  
  "status": {  
    "type": "Property",  
    "value": "ok"  
  },  
  "refStreetlightGroup": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:G345"  
  },  
  "refStreetlightModel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:StreetlightModel:streetlightmodel:STEEL_Tubular_10m"  
  },  
  "circuit": {  
    "type": "Property",  
    "value": "C-456-A467"  
  },  
  "lanternHeight": {  
    "type": "Property",  
    "value": 10  
  },  
  "locationCategory": {  
    "type": "Property",  
    "value": "centralIsland"  
  },  
  "powerState": {  
    "type": "Property",  
    "value": "off"  
  },  
  "controllingMethod": {  
    "type": "Property",  
    "value": "individual"  
  },  
  "dateLastLampChange": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-07-08T08:02:21.753Z"  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Straßenleuchte NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine Straßenlaterne im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "areaServed": "Roundabouts city entrance",  
  "circuit": "C-456-A467",  
  "controllingMethod": "individual",  
  "dateLastLampChange": {  
    "@type": "DateTime",  
    "@value": "2016-07-08T08:02:21.753Z"  
  },  
  "id": "urn:ngsi-ld:Streetlight:streetlight:guadalajara:4567",  
  "lanternHeight": 10,  
  "location": {  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ],  
    "type": "Point"  
  },  
  "locationCategory": "centralIsland",  
  "powerState": "off",  
  "refStreetlightGroup": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:G345",  
  "refStreetlightModel": "urn:ngsi-ld:StreetlightModel:streetlightmodel:STEEL_Tubular_10m",  
  "status": "ok",  
  "type": "Streetlight"  
}  
```  
