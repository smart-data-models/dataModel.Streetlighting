Entité : Éclairage public  
=========================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **A Street light**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `annotations`:   - `areaServed`:   - `circuit`:   - `color`: La couleur du produit.  - `controllingMethod`:   - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateLastLampChange`:   - `dateLastSwitchingOff`:   - `dateLastSwitchingOn`:   - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateServiceStarted`:   - `description`:   - `id`:   - `illuminanceLevel`:   - `image`:   - `laternHeight`:   - `location`:   - `locationCategory`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `powerState`:   - `refDevice`:   - `refStreetlightControlCabinet`:   - `refStreetlightGroup`:   - `refStreetlightModel`:   - `seeAlso`:   - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `status`:   - `type`:   ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Streetlight:    
  description: 'A Street light'    
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
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      items:    
        type: string    
      type: array    
    areaServed:    
      type: string    
    circuit:    
      type: string    
    color:    
      description: 'The color of the product.'    
      type: string    
    controllingMethod:    
      enum:    
        - group    
        - individual    
      type: string    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateLastLampChange:    
      format: date-time    
      type: string    
    dateLastSwitchingOff:    
      format: date-time    
      type: string    
    dateLastSwitchingOn:    
      format: date-time    
      type: string    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateServiceStarted:    
      format: date-time    
      type: string    
    description:    
      type: string    
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
    illuminanceLevel:    
      maximum: 1    
      minimum: 0    
      type: number    
    image:    
      format: uri    
      type: string    
    laternHeight:    
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
    locationCategory:    
      enum:    
        - façade    
        - sidewalk    
        - pedestrianPath    
        - road    
        - playground    
        - park    
        - garden    
        - bridge    
        - tunnel    
        - parking    
        - centralIsland    
      type: string    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *streetlight_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    powerState:    
      enum:    
        - on    
        - off    
        - low    
        - bootingUp    
      type: string    
    refDevice:    
      items:    
        anyOf: *streetlight_-_properties_-_owner_-_items_-_anyof    
      minItems: 1    
      type: array    
      uniqueItems: true    
    refStreetlightControlCabinet:    
      anyOf: *streetlight_-_properties_-_owner_-_items_-_anyof    
    refStreetlightGroup:    
      anyOf: *streetlight_-_properties_-_owner_-_items_-_anyof    
    refStreetlightModel:    
      anyOf: *streetlight_-_properties_-_owner_-_items_-_anyof    
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
    status:    
      enum:    
        - ok    
        - defectiveLamp    
        - columnIssue    
        - brokenLantern    
      type: string    
    type:    
      enum:    
        - Streetlight    
      type: string    
  required:    
    - id    
    - type    
    - location    
    - status    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Streetlight NGSI V2 valeurs clés Exemple  
Voici un exemple de Streetlight au format JSON comme valeurs clés. Il est compatible avec la version 2 du NGSI lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### Streetlight NGSI V2 normalisé Exemple  
Voici un exemple d'un lampadaire au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
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
#### Streetlight NGSI-LD valeurs clés Exemple  
Voici un exemple de Streetlight au format JSON-LD comme valeurs clés. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "areaServed": "Roundabouts city entrance",  
 "circuit": "C-456-A467",  
 "controllingMethod": "individual",  
 "dateLastLampChange": {"@type": "DateTime",  
                        "@value": "2016-07-08T08:02:21.753Z"},  
 "id": "urn:ngsi-ld:Streetlight:streetlight:guadalajara:4567",  
 "lanternHeight": 10,  
 "location": {"coordinates": [-3.164485591715449, 40.62785133667262],  
              "type": "Point"},  
 "locationCategory": "centralIsland",  
 "powerState": "off",  
 "refStreetlightGroup": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:G345",  
 "refStreetlightModel": "urn:ngsi-ld:StreetlightModel:streetlightmodel:STEEL_Tubular_10m",  
 "status": "ok",  
 "type": "Streetlight"}  
```  
#### L'éclairage public NGSI-LD normalisé Exemple  
Voici un exemple d'un lampadaire au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
