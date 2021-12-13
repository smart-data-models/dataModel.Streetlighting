Entità: StreetlightModel  
========================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightModel/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Un modello di luce stradale**  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `annotations`: Annotazioni sull'elemento  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `category`: Tipo di risorsa che implementa l'illuminazione stradale. Enum:'`postTop, bollard, lamppost, lightTower, flashingBeacon, sideEntry, signLight, ornamentalLantern'. O qualsiasi altro valore non definito sopra e significativo per l'applicazione  - `color`: Il colore del prodotto  - `colorRenderingIndex`: Indice di resa dei colori della lampada  - `colorTemperature`: Temperatura di colore correlata della lampada  - `columnBrandName`: Nome del marchio della colonna  - `columnColor`: Colore di pittura della colonna. Valori consentiti: Una parola chiave di colore come specificato da [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords). Un valore di colore come specificato da [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)  - `columnMadeOf`: La colonna è fatta di materiale. Enum:'acciaio, alluminio, legno, altro'.  - `columnManufacturerName`: Nome del produttore della colonna  - `columnModelName`: Nome del modello della colonna  - `compliantWith`: Un elenco delle norme alle quali questo modello di lampione è conforme  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `image`: Un'immagine dell'oggetto  - `lampBrandName`: Nome della marca della lampada  - `lampManufacturerName`: Nome del produttore della lampada.  - `lampModelName`: Nome del modello della lampada  - `lampTechnology`: Tecnologia utilizzata dalla lampada. Enum:'LED, LPS, HPS'. O qualsiasi altro valore non coperto dalla lista precedente e significativo per l'applicazione.  - `lampWeight`: Peso della lampada  - `lanternBrandName`: Nome della marca della lanterna  - `lanternManufacturerName`: Nome del produttore della lanterna  - `lanternModelName`: Nome del modello della lanterna  - `lanternWeight`: Peso della lanterna  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `luminousFlux`: Potenza luminosa massima che può essere fornita dalla lampada  - `maxPowerConsumption`: Consumo massimo di energia supportato dalla lanterna  - `minPowerConsumption`: Consumo minimo di energia supportato dalla lanterna  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `powerConsumption`: Consumo di energia (nominale) fatto dalla lampada  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `type`: Tipo di entità NGSI. Deve essere StreetlightModel  - `workingLife`: Il numero stimato di ore di lavoro (della lampada) senza guasti    
Proprietà richieste  
- `id`  - `name`  - `type`    
Rappresenta un modello di lampione composto da un modello specifico di struttura di supporto, un modello di lanterna e un modello di lampada. Un'istanza di lampione sarà basata su un certo modello di lampione.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempio di payloads  
#### StreetlightModel NGSI-v2 valori chiave Esempio  
Ecco un esempio di uno StreetlightModel in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### StreetlightModel NGSI-v2 normalizzato Esempio  
Ecco un esempio di uno StreetlightModel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### StreetlightModel NGSI-LD valori chiave Esempio  
Ecco un esempio di uno StreetlightModel in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### StreetlightModel NGSI-LD normalizzato Esempio  
Ecco un esempio di uno StreetlightModel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza