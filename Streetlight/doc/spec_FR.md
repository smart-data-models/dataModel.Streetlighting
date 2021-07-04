Entité : Lampadaire  
===================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/Streetlight/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Un lampadaire**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `annotations`: Annotations sur l'élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `circuit`: Le circuit auquel ce lampadaire est connecté et qui l'alimente. Il contient généralement un identifiant qui permet d'obtenir plus d'informations sur ce circuit.  - `color`: La couleur du produit  - `controllingMethod`: La méthode utilisée pour contrôler ce lampadaire. Enum : "groupe, individuel".  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateLastLampChange`: Horodatage du dernier changement de lampe effectué  - `dateLastSwitchingOff`: Horodatage de la dernière mise hors tension  - `dateLastSwitchingOn`: Horodatage de la dernière mise sous tension  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateServiceStarted`: Date de mise en service du réverbère  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `illuminanceLevel`: Réglage du niveau d'éclairement relatif. Un nombre compris entre 0 et 1.  - `image`: Une URL contenant une photo du lampadaire  - `laternHeight`: Hauteur de la lanterne. Dans les colonnes à plusieurs bras, cela peut varier d'un lampadaire à l'autre. Les lampadaires muraux sont une autre source de variation de cette propriété.  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `locationCategory`: Catégorie de l'emplacement où est placé le lampadaire. Enum : 'pont, île centrale, façade, jardin, parc, parking, chemin piétonnier, aire de jeux, route, trottoir, tunnel'.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `powerState`: État de l'alimentation du lampadaire. Enum : 'bootingUp, low, off, on' (démarrage)  - `refDevice`: Référence au(x) dispositif(s) utilisé(s) pour surveiller ce streetligth. Liste des références aux entités de type Dispositif.  - `refStreetlightControlCabinet`: Si ce lampadaire est à commande individuelle, référence à l'armoire de commande en charge.  - `refStreetlightGroup`: Groupe du lampadaire, si ce lampadaire appartient à un groupe.  - `refStreetlightModel`: Modèle de lampadaire.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `status`: L'état général de ce lampadaire. Enum:'brokenLantern, columnIssue, defectiveLamp, ok'  - `type`: Type d'entité NGSI. Il doit s'agir de Streetlight    
Propriétés requises  
- `id`  - `location`  - `status`  - `type`    
Une entité de type `Streetlight` représente un lampadaire urbain. En fait, il y aura une entité de type `Streetlight` par lampadaire. Ainsi, si un poteau particulier contient plus d'une lanterne, il y aura autant d'entités streetlight que de lampes installées. Par conséquent, il peut y avoir plus d'une entité réverbère par emplacement. Une entité `Streetlight` ne contient pas d'attribut correspondant aux caractéristiques structurelles. De telles données sont capturées par des entités de type `StreetlightModel`.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Streetlight:    
  description: 'A Street light'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
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
      type: Geoproperty    
    locationCategory:    
      description: 'Category of the location where the streetlight is placed. Enum:''bridge, centralIsland, façade, garden, park, parking, pedestrianPath, playground, road, sidewalk, tunnel'''    
      enum:    
        - bridge    
        - centralIsland    
        - facade    
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
## Exemples de charges utiles  
#### Exemple de valeurs-clés NGSI-v2 pour les lampadaires.  
Voici un exemple de lampadaire au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Lampadaire NGSI-v2 normalisé Exemple  
Voici un exemple d'un lampadaire au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Exemple de valeurs clés de l'éclairage public NGSI-LD  
Voici un exemple de lampadaire au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Eclairage public NGSI-LD normalisé Exemple  
Voici un exemple de lampadaire au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
