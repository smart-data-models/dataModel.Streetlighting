Entité : StreetlightModel  
=========================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightModel/LICENSE.md)  
Description globale : **Un modèle de lampadaire**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `annotations`: Annotations sur le sujet  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `category`: Type de bien qui met en œuvre le lampadaire. Enum : "poteauTop, borne, lampadaire, tour d'éclairage, gyrophare, entrée latérale, panneauLumière, lanterne ornementale". Ou toute autre valeur non définie ci-dessus et significative pour l'application  - `color`: La couleur du produit  - `colorRenderingIndex`: Indice de rendu des couleurs de la lampe  - `colorTemperature`: Corrélation entre la température de couleur de la lampe  - `columnBrandName`: Nom de la marque de la colonne  - `columnColor`: La colonne est en couleur de peinture. Valeurs autorisées : Un mot-clé de couleur tel que spécifié par [W3C Color Keywords] (https://www.w3.org/TR/SVG/types.html#ColorKeywords). Une valeur de couleur telle que spécifiée par [W3C Color Data Type] (https://www.w3.org/TR/SVG/types.html#BasicDataTypes)  - `columnMadeOf`: La colonne des matériaux est faite de. Enum : "acier, aluminium, bois, autres".  - `columnManufacturerName`: Nom du fabricant de la colonne  - `columnModelName`: Nom du modèle de la colonne  - `compliantWith`: Une liste des normes auxquelles ce modèle de réverbère est conforme  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `image`: Une image de l'objet  - `lampBrandName`: Nom de la marque de la lampe  - `lampManufacturerName`: Nom du fabricant de la lampe.  - `lampModelName`: Nom du modèle de la lampe  - `lampTechnology`: Technologie utilisée par la lampe. Enum : "LED, LPS, HPS". Ou toute autre valeur non couverte par la liste ci-dessus et significative pour l'application.  - `lampWeight`: Poids de la lampe  - `lanternBrandName`: Nom de la marque de la lanterne  - `lanternManufacturerName`: Nom du fabricant de la lanterne  - `lanternModelName`: Nom du modèle de la lanterne  - `lanternWeight`: Le poids de la lanterne  - `location`:   - `luminousFlux`: Rendement lumineux maximal pouvant être fourni par la lampe  - `maxPowerConsumption`: Consommation électrique maximale supportée par la lanterne  - `minPowerConsumption`: Consommation électrique minimale supportée par la lanterne  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `powerConsumption`: Consommation électrique (nominale) de la lampe  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type d'entité NGSI. Il doit s'agir de StreetlightModel  - `workingLife`: Le nombre estimé d'heures de travail (la lampe) sans défaillance    
Propriétés requises  
- `id`  - `name`  - `type`    
Il représente un modèle de réverbère composé d'un modèle de structure de support spécifique, d'un modèle de lanterne et d'un modèle de lampe. Une instance de lampadaire sera basée sur un certain modèle de lampadaire.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### StreetlightModel NGSI V2 valeurs clés Exemple  
Voici un exemple de StreetlightModel au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### StreetlightModel NGSI V2 normalisé Exemple  
Voici un exemple de StreetlightModel au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### StreetlightModel NGSI-LD valeurs clés Exemple  
Voici un exemple de StreetlightModel au format JSON-LD comme valeurs clés. Ce modèle est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### StreetlightModel NGSI-LD normalisé Exemple  
Voici un exemple de StreetlightModel au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
