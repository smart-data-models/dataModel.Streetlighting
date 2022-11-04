<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Lampadaire  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/Streetlight/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Un lampadaire**  
version : 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `annotations[array]`: Annotations sur l'élément  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `circuit[string]`: Le circuit auquel ce lampadaire est connecté et qui l'alimente. Il contient généralement un identifiant qui permet d'obtenir plus d'informations sur ce circuit.  - `color[string]`: La couleur du produit  . Model: [https://schema.org/color](https://schema.org/color)- `controllingMethod[string]`: La méthode utilisée pour contrôler ce lampadaire. Enum : "groupe, individuel".  - `current[number]`: Valeur actuelle du lampadaire correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateLastLampChange[string]`: Horodatage du dernier changement de lampe effectué  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastSwitchingOff[string]`: Horodatage de la dernière mise hors tension  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastSwitchingOn[string]`: Horodatage de la dernière mise sous tension  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateServiceStarted[string]`: Date de mise en service du réverbère  . Model: [https://schema.org/Date](https://schema.org/Date)- `description[string]`: Une description de cet article  - `deviceInfo[object]`: Informations sur le dispositif associé aux observations.  . Model: [https://schema.org/Text](https://schema.org/Text)- `feederID[*]`: ID unique du panneau d'alimentation du lampadaire associé au lampadaire correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `feederPillarNum[string]`: Informations sur le pilier d'alimentation du réverbère associé au réverbère correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Identifiant unique de l'entité  - `illuminanceLevel[number]`: Réglage du niveau d'éclairement relatif. Un nombre compris entre 0 et 1.  - `image[string]`: Une URL contenant une photo du lampadaire  . Model: [https://schema.org/image](https://schema.org/image)- `lanternHeight[number]`: Hauteur de la lanterne. Dans les colonnes à plusieurs bras, cela peut varier d'un lampadaire à l'autre. Les lampadaires muraux sont une autre source de variation de cette propriété.  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `locationCategory[string]`: Catégorie de l'emplacement où est placé le lampadaire. Enum : 'pont, île centrale, façade, jardin, parc, parking, chemin piétonnier, aire de jeux, route, trottoir, tunnel'.  - `municipalityInfo[object]`: Informations sur la municipalité correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Le nom de cet élément.  - `observationDateTime[string]`: Dernière heure d'observation signalée.  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `powerConsumption[number]`: Puissance consommée par la LED ou l'ampoule du lampadaire correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `powerFactor[number]`: Le facteur de puissance ou le rapport de la puissance de fonctionnement du lampadaire correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `powerRating[number]`: Puissance de la LED ou de l'ampoule du lampadaire correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `powerState[string]`: État de l'alimentation du lampadaire. Enum : 'bootingUp, low, off, on' (démarrage)  . Model: [https://schema.org/Text](https://schema.org/Text)- `refDevice[array]`: Référence au(x) dispositif(s) utilisé(s) pour surveiller ce streetligth. Liste des références aux entités de type Dispositif.  - `refStreetlightControlCabinet[*]`: Si ce lampadaire est à commande individuelle, référence à l'armoire de commande en charge.  - `refStreetlightGroup[*]`: Groupe du lampadaire, si ce lampadaire appartient à un groupe.  - `refStreetlightModel[*]`: Modèle de lampadaire.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `status[string]`: L'état général de ce lampadaire. Enum:'brokenLantern, columnIssue, defectiveLamp, ok'  - `streetPoleNum[string]`: Informations sur le poteau de rue associé au lampadaire correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Type d'entité NGSI. Il doit s'agir de Streetlight  - `voltage[number]`: Valeur de la tension du lampadaire correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `location`  - `status`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Une entité de type `Streetlight` représente un lampadaire urbain. En fait, il y aura une entité de type `Streetlight` par lampadaire. Ainsi, si un poteau particulier contient plus d'une lanterne, il y aura autant d'entités streetlight que de lampes installées. Par conséquent, il peut y avoir plus d'une entité lampadaire par emplacement. Une entité `Streetlight` ne contient pas d'attribut correspondant aux caractéristiques structurelles. De telles données sont capturées par des entités de type `StreetlightModel`.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
    circuit:    
      description: 'The circuit to which this streetlight connects to and gets power from. Typically it will contain an identifier that will allow to obtain more information about such circuit.'    
      type: string    
      x-ngsi:    
        type: Property    
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    controllingMethod:    
      description: 'The method used to control this streetlight. Enum:''group, individual''. '    
      enum:    
        - group    
        - individual    
      type: string    
      x-ngsi:    
        type: Property    
    current:    
      description: 'Current value of the streetlight corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    dateLastLampChange:    
      description: 'Timestamp of the last change of lamp made'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateLastSwitchingOff:    
      description: 'Timestamp of the last switching off'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateLastSwitchingOn:    
      description: 'Timestamp of the last switching on'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateServiceStarted:    
      description: 'Date at which the streetlight started giving service'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Date    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    deviceInfo:    
      description: 'Information about the device associated with the observations.'    
      properties:    
        RFId:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the ID of the RFID reader.'    
          type: string    
        deviceBatteryStatus:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the Battery charging status of the reporting device(Connected, Disconnected).'    
          type: string    
        deviceId:    
          description: 'Property. Model:''https://schema.org/Text''. Device ID of the physical sensor/ measurement station corresponding to this observation.'    
          type: string    
        deviceModel:    
          description: 'Property. Model:''https://schema.org/Text''. Describes the information of the device, sensor or system in consideration.'    
          properties:    
            brandName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of the brand associated with an entity, e.g., sensor, device etc.'    
              type: string    
            manufacturerName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of the manufacturer associated with an entity, e.g., sensor, device etc.'    
              type: string    
            modelName:    
              description: 'Property. Model:''https://schema.org/Text''. Name of a specific model associated with an entity, e.g., sensor, device etc.'    
              type: string    
            modelURL:    
              description: 'Property. Model:''https://schema.org/Text''. URL providing further information of a specific model associated with an entity, e.g., sensor, device etc.'    
              type: string    
          type: object    
        deviceName:    
          description: 'Property. Model:''https://schema.org/Text''. Device Name or Station name of the sensor device/station corresponding to this observation.'    
          type: string    
        deviceSimNumber:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the sim number of the device in the waste management vehicle.'    
          type: string    
        measurand:    
          description: 'Property. Model:''https://schema.org/Text''. Property/properties sensed/observed/measured by the device.'    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    feederID:    
      anyOf:    
        - description: 'Property. '    
          type: string    
        - description: 'Property. Model:''https://schema.org/Text'    
          format: uri    
          type: string    
      description: 'Unique ID of the streetlight feeder panel associated with the streetlight corresponding to this observation.'    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Relationship    
    feederPillarNum:    
      description: 'Streetlight feeder pillar information associated with the streetlight corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      x-ngsi:    
        type: Property    
    illuminanceLevel:    
      description: 'Relative illuminance level setting. A number between 0 and 1.'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    image:    
      description: 'A URL containing a photo of the streetlight'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/image    
        type: Relationship    
    lanternHeight:    
      description: 'Lantern''s height. In columns with many arms this can vary between streetlights. Another variation source of this property are wall-mounted streetlights.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    locationCategory:    
      description: 'Category of the location where the streetlight is placed. Enum:''bridge, centralIsland, facade, garden, park, parking, pedestrianPath, playground, road, sidewalk, tunnel'''    
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
      type: string    
      x-ngsi:    
        type: Property    
    municipalityInfo:    
      description: 'Municipality information corresponding to this observation.'    
      properties:    
        cityId:    
          description: 'Property. Model:''https://schema.org/Text''. City ID corresponding to this observation'    
          type: string    
        cityName:    
          description: 'Property. Model:''https://schema.org/Text''. City name corresponding to this observation'    
          type: string    
        district:    
          description: 'Property. Model:''https://schema.org/Text''. District name corresponding to this observation.'    
          type: string    
        stateName:    
          description: 'Property. Model:''https://schema.org/Text''. Name of the state corresponding to this observation.'    
          type: string    
        ulbName:    
          description: 'Property. Model:''https://schema.org/Text''.Name of the Urban Local Body corresponding to this observation.'    
          type: string    
        wardNum:    
          description: 'Property. Model:''https://schema.org/Number''. Ward number corresponding to this observation.'    
          type: number    
        zoneId:    
          description: 'Property. Model:''https://schema.org/Text''. Zone ID corresponding to this observation.'    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *streetlight_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    powerConsumption:    
      description: 'Power consumed by the LED or the streetlight bulb corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    powerFactor:    
      description: 'Power factor or the ratio of working power of the streetlight corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    powerRating:    
      description: 'Power rating of the LED or the streetlight bulb corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    powerState:    
      description: 'Streetlight''s power state. Enum:''bootingUp, low, off, on'''    
      enum:    
        - bootingUp    
        - low    
        - off    
        - on    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Relationship    
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
      x-ngsi:    
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
      x-ngsi:    
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
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'The overall status of this street light. Enum:''brokenLantern, columnIssue, defectiveLamp, ok'''    
      enum:    
        - brokenLantern    
        - columnIssue    
        - defectiveLamp    
        - ok    
      type: string    
      x-ngsi:    
        type: Property    
    streetPoleNum:    
      description: 'Street pole information associated with the streetlight corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Streetlight'    
      enum:    
        - Streetlight    
      type: string    
      x-ngsi:    
        type: Property    
    voltage:    
      description: 'Voltage value of the streetlight corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - status    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/Streetlight/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Streetlighting/Streetlight/schema.json    
  x-model-tags: IUDX    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Exemple de valeurs-clés NGSI-v2 pour les lampadaires.  
Voici un exemple de lampadaire au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "streetlight:guadalajara:4567",  
  "type": "Streetlight",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ]  
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
  "dateLastLampChange": "2016-07-08T08:02:21.753Z",  
  "powerConsumption": 10,  
  "current": 250,  
  "powerRating": 5,  
  "powerFactor": 0.7,  
  "voltage": 50,  
  "feederPillarNum": "70",  
  "streetPoleNum": "2",  
  "feederID": "F1",  
  "observationDateTime": "2021-01-11T15:51:02+05:30",  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityID": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneID": "2",  
    "wardNum": 4  
  },  
  "deviceInfo": {  
    "rfID": "5634684",  
    "deviceBatteryStatus": "Connected",  
    "deviceName": "SL1",  
    "deviceID": "43",  
    "measurand": "6",  
    "deviceSimNumber": "6755375727",  
    "deviceModel": {  
      "brandName": "abc",  
      "manufacturerName": "xyz",  
      "modelName": "SL1",  
      "modelURL": "www.abcstreetlight.com"  
    }  
  }  
}  
```  
</details>  
#### Eclairage public NGSI-v2 normalisé Exemple  
Voici un exemple d'un lampadaire au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "streetlight:guadalajara:4567",  
  "type": "Streetlight",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -3.164485591715449,  
        40.62785133667262  
      ]  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Roundabouts city entrance"  
  },  
  "status": {  
    "type": "Text",  
    "value": "ok"  
  },  
  "refStreetlightGroup": {  
    "type": "Relationship",  
    "value": "streetlightgroup:G345"  
  },  
  "refStreetlightModel": {  
    "type": "Relationship",  
    "value": "streetlightmodel:STEEL_Tubular_10m"  
  },  
  "circuit": {  
    "type": "Text",  
    "value": "C-456-A467"  
  },  
  "lanternHeight": {  
    "type": "Number",  
    "value": 10  
  },  
  "locationCategory": {  
    "type": "Text",  
    "value": "centralIsland"  
  },  
  "powerState": {  
    "type": "Text",  
    "value": "off"  
  },  
  "controllingMethod": {  
    "type": "Text",  
    "value": "individual"  
  },  
  "dateLastLampChange": {  
    "type": "DateTime",  
    "value": "2016-07-08T08:02:21.753Z"  
  },  
  "powerConsumption": {  
    "type": "Number",  
    "value": 10  
  },  
  "current": {  
    "type": "Number",  
    "value": 250  
  },  
  "powerRating": {  
    "type": "Number",  
    "value": 5  
  },  
  "powerFactor": {  
    "type": "Number",  
    "value": 0.7  
  },  
  "voltage": {  
    "type": "Number",  
    "value": 50  
  },  
  "feederPillarNum": {  
    "type": "Text",  
    "value": "70"  
  },  
  "streetPoleNum": {  
    "type": "Text",  
    "value": "2"  
  },  
  "feederID": {  
    "type": "Text",  
    "value": "F1"  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2021-01-11T15:51:02+05:30"  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityId": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneId": "2",  
      "wardNum": 4  
    },  
    "deviceInfo": {  
      "type": "StructuredValue",  
      "value": {  
        "rfId": "5634684",  
        "deviceBatteryStatus": "Connected",  
        "deviceName": "SL1",  
        "deviceID": "43",  
        "measurand": "6",  
        "deviceSimNumber": "6755375727",  
        "deviceModel": {  
          "brandName": "abc",  
          "manufacturerName": "xyz",  
          "modelName": "SL1",  
          "modelURL": "www.abcstreetlight.com"  
        }  
      }  
    }  
  }  
}  
```  
</details>  
#### Exemple de valeurs-clés NGSI-LD pour les lampadaires.  
Voici un exemple de lampadaire au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Streetlight:streetlight:guadalajara:4567",  
    "type": "Streetlight",  
    "areaServed": "Roundabouts city entrance",  
    "circuit": "C-456-A467",  
    "controllingMethod": "individual",  
    "current": 250,  
    "dateLastLampChange": {  
        "@type": "DateTime",  
        "@value": "2016-07-08T08:02:21.753Z"  
    },  
    "deviceInfo": {  
        "rfID": "5634684",  
        "deviceBatteryStatus": "Connected",  
        "deviceName": "SL1",  
        "deviceID": "43",  
        "measurand": "6",  
        "deviceSimNumber": "6755375727",  
        "deviceModel": {  
            "brandName": "abc",  
            "manufacturerName": "xyz",  
            "modelName": "SL1",  
            "modelURL": "www.abcstreetlight.com"  
        }  
    },  
    "feederID": "F1",  
    "feederPillarNum": "70",  
    "lanternHeight": 10,  
    "location": {  
        "coordinates": [  
            -3.164485591715449,  
            40.62785133667262  
        ],  
        "type": "Point"  
    },  
    "locationCategory": "centralIsland",  
    "municipalityInfo": {  
        "district": "Bangalore Urban",  
        "ulbName": "BMC",  
        "cityID": "23",  
        "stateName": "Karnataka",  
        "cityName": "Bangalore",  
        "zoneID": "2",  
        "wardNum": 4  
    },  
    "observationDateTime": "2021-01-11T15:51:02+05:30",  
    "powerConsumption": 10,  
    "powerFactor": 0.7,  
    "powerRating": 5,  
    "powerState": "off",  
    "refStreetlightGroup": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:G345",  
    "refStreetlightModel": "urn:ngsi-ld:StreetlightModel:streetlightmodel:STEEL_Tubular_10m",  
    "status": "ok",  
    "streetPoleNum": "2",  
    "voltage": 50,  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Eclairage public NGSI-LD normalisé Exemple  
Voici un exemple de lampadaire au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Streetlight:streetlight:guadalajara:4567",  
    "type": "Streetlight",  
    "areaServed": {  
        "type": "Property",  
        "value": "Roundabouts city entrance"  
    },  
    "circuit": {  
        "type": "Property",  
        "value": "C-456-A467"  
    },  
    "controllingMethod": {  
        "type": "Property",  
        "value": "individual"  
    },  
    "current": {  
        "type": "Property",  
        "value": 250  
    },  
    "dateLastLampChange": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-07-08T08:02:21.753Z"  
        }  
    },  
    "feederID": {  
        "type": "Property",  
        "value": "F1"  
    },  
    "feederPillarNum": {  
        "type": "Property",  
        "value": "70"  
    },  
    "lanternHeight": {  
        "type": "Property",  
        "value": 10  
    },  
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
    "locationCategory": {  
        "type": "Property",  
        "value": "centralIsland"  
    },  
    "municipalityInfo": {  
        "type": "Property",  
        "value": {  
            "district": "Bangalore Urban",  
            "ulbName": "BMC",  
            "cityID": "23",  
            "stateName": "Karnataka",  
            "cityName": "Bangalore",  
            "zoneID": "2",  
            "wardNum": 4  
        },  
        "deviceInfo": {  
            "type": "Property",  
            "value": {  
                "rfID": "5634684",  
                "deviceBatteryStatus": "Connected",  
                "deviceName": "SL1",  
                "deviceID": "43",  
                "measurand": "6",  
                "deviceSimNumber": "6755375727",  
                "deviceModel": {  
                    "brandName": "abc",  
                    "manufacturerName": "xyz",  
                    "modelName": "SL1",  
                    "modelURL": "www.abcstreetlight.com"  
                }  
            }  
        }  
    },  
    "observationDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-01-11T15:51:02+05:30"  
        }  
    },  
    "powerConsumption": {  
        "type": "Property",  
        "value": 10  
    },  
    "powerFactor": {  
        "type": "Property",  
        "value": 0.7  
    },  
    "powerRating": {  
        "type": "Property",  
        "value": 5  
    },  
    "powerState": {  
        "type": "Property",  
        "value": "off"  
    },  
    "refStreetlightGroup": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:G345"  
    },  
    "refStreetlightModel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:StreetlightModel:streetlightmodel:STEEL_Tubular_10m"  
    },  
    "status": {  
        "type": "Property",  
        "value": "ok"  
    },  
    "streetPoleNum": {  
        "type": "Property",  
        "value": "2"  
    },  
    "voltage": {  
        "type": "Property",  
        "value": 50  
    },  
    "@context": [  
        "iudx:Streetlight",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
