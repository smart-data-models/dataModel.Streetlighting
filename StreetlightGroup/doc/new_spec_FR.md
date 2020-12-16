Entité : StreetlightGroup  
=========================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightGroup/LICENSE.md)  
Description globale : **Un groupe d'éclairage public**  

## Liste des biens  

- `activeProgramId`: Identifiant du programme actif pour ce groupe de streetlight  - `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `annotations`: Un champ réservé aux annotations (incidences, remarques, etc.).  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `color`: La couleur du produit  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateLastSwitchingOff`: Horodatage de la dernière extinction  - `dateLastSwitchingOn`: Horodatage de la dernière mise sous tension  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `illuminanceLevel`: Réglage du niveau d'éclairement relatif pour le groupe. Valeurs autorisées : Un nombre entre 0 et 1  - `image`: Une image de l'objet  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `powerState`: L'état de pouvoir du groupe Streetlight. Enum : "on, off, low, bootingUp".  - `refStreetlight`: Liste des entités de lampadaires appartenant à ce groupe. Liste des références aux entités du type Streetlight. Valeurs autorisées : Il doit y avoir une intégrité topographique entre l'emplacement du groupe et celui des différents lampadaires.  - `refStreetlightControlCabinet`: Cabinet de contrôle du groupe Streetlight  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `switchingMode`: Horodatage du dernier changement de lampe effectué. Enum:' nuit-ON, nuit-OFF, nuit-LOW, toujours-ON, jour-ON, jour-OFF, jour-LOW'.  - `switchingOnHours`: Mise en marche des heures. Il sert normalement à établir des horaires spéciaux pour certaines dates.  - `type`: Type d'entité NGSI. Il doit s'agir de StreetlightGroup    
Propriétés requises  
- `id`  - `location`  - `type`    
Une entité de type "StreetlightGroup" représente un groupe de lampadaires. Ils peuvent être contrôlés ensemble par le même système automatisé (contrôleur de cabinet).  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### StreetlightGroup NGSI V2 valeurs clés Exemple  
Voici un exemple de StreetlightGroup en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### StreetlightGroup NGSI V2 normalisé Exemple  
Voici un exemple de StreetlightGroup au format JSON tel que normalisé. Il est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### StreetlightGroup NGSI-LD valeurs clés Exemple  
Voici un exemple de StreetlightGroup au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "areaServed": "Calle Comercial Centro",  
 "circuitId": "C-456-A467",  
 "dateLastSwitchingOff": {"@type": "DateTime",  
                          "@value": "2016-07-07T07:59:06.618Z"},  
 "dateLastSwitchingOn": {"@type": "DateTime",  
                         "@value": "2016-07-07T19:59:06.618Z"},  
 "id": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:mycity:A12",  
 "location": {"coordinates": [[[100.0, 0.0], [101.0, 1.0]],  
                              [[102.0, 2.0], [103.0, 3.0]]],  
              "type": "MultiLineString"},  
 "powerState": "on",  
 "refStreetlightCabinetController": "urn:ngsi-ld:StreetlightCabinetController:cabinetcontroller:CC45A34",  
 "switchingOnHours": [{"description": "Christmas",  
                       "from": "--11-30",  
                       "hours": "Mo,Su 16:00-02:00",  
                       "to": "--01-07"}],  
 "type": "StreetlightGroup"}  
```  
#### StreetlightGroup NGSI-LD normalisé Exemple  
Voici un exemple de StreetlightGroup au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
