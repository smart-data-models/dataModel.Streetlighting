Entité : StreetlightControlCabinet  
==================================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightControlCabinet/LICENSE.md)  
Description globale : **A Cabinet de contrôle de l'éclairage public**  

## Liste des biens  

- `activePowerR`: Puissance active consommée en phase R  - `activePowerS`: Puissance active consommée en phase S  - `activePowerT`: Puissance active consommée en phase T  - `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `annotations`: Un champ réservé aux annotations (incidences, remarques, etc.)  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `brandName`: Nom de la marque du cabinet  - `color`: La couleur du produit  - `compliantWith`: Une liste des normes auxquelles le contrôleur de cabinet est conforme (ex. IP54)  - `cosPhi`: Cosinus du paramètre phi  - `cupboardMadeOf`: Matériau dont est faite l'armoire du cabinet. Enum : "béton, métal, autre, plastique  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateLastProgramming`: Date à laquelle il y a eu une opération de programmation au-dessus du cabinet  - `dateMeteringStarted`: La date de début du comptage de l'énergie consommée  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateServiceStarted`: Date à laquelle le contrôleur de cabinet a commencé à rendre service  - `description`: Horodatage du dernier changement de lampe effectué  - `energyConsumed`: Énergie consommée par les circuits contrôlés depuis le début du comptage (depuis la date de début du comptage)  - `energyCost`: Coût de l'énergie consommée par les circuits contrôlés depuis la date de début du comptage  - `features`: Une liste des caractéristiques du contrôleur de cabinet.  Les valeurs techniques considérées comme significatives par les applications. Horloge astronomique". L'armoire de commande comprend une horloge astronomique pour traiter les heures de commutation. Contrôle individuel". L'armoire de commande permet de contrôler les lampadaires individuellement.  - `frequency`: La fréquence de fonctionnement du circuit  - `id`: Identifiant unique de l'entité  - `image`: Une image de l'objet  - `intensityR`: Intensité électrique en phase R  - `intensityS`: Intensité électrique en phase S  - `intensityT`:  Intensité électrique en phase T  - `lastMeterReading`: Valeur du dernier relevé obtenu à partir du système de comptage de l'énergie consommée  - `location`:   - `manufacturerName`: Nom du fabricant du cabinet  - `maximumPowerAvailable`: La puissance maximale disponible (par contrat) pour les circuits contrôlés par cette armoire  - `meterReadingPeriod`: La périodicité des relevés des compteurs d'énergie consommée en jours  - `modelName`: Nom du modèle de cabinet  - `name`: Le nom de cet article.  - `nextActuationDeadline`: Date limite pour la prochaine action à effectuer (programmation, test, etc.)  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `powerFactorR`: Facteur de puissance pour la phase R. Valeurs autorisées : Un nombre compris entre -1 et 1  - `powerFactorS`: Facteur de puissance pour la phase S. Valeurs autorisées : Un nombre compris entre -1 et 1  - `powerFactorT`: Facteur de puissance pour la phase T. Valeurs autorisées : Un nombre compris entre -1 et 1  - `reactiveEnergyConsumed`: Énergie consommée (en ce qui concerne la puissance réactive) par les circuits depuis la date de début du comptage  - `reactivePowerR`: Puissance réactive en phase R  - `reactivePowerS`: Puissance réactive en phase S  - `reactivePowerT`: Puissance réactive en phase T  - `refDevice`: Référence au(x) dispositif(s) utilisé(s) pour surveiller cette armoire de commande.  - `refStreetlightGroup`: Groupe(s) d'éclairage public contrôlé(s). Liste des références aux entités du type StreetlightGroup  - `responsible`: Responsable du contrôleur de cabinet, c'est-à-dire de l'entité chargée de l'actionnement (programmation, etc.).  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `serialNumber`: Numéro de série du conteneur.  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `thdrIntensityR`: Distorsion harmonique totale (R) d'intensité dans la phase R. Valeurs autorisées : Un nombre compris entre 0 et 1  - `thdrIntensityS`: Distorsion harmonique totale (S) d'intensité dans la phase S. Valeurs autorisées : Un nombre compris entre 0 et 1  - `thdrIntensityT`: Distorsion harmonique totale (T) d'intensité dans la phase T. Valeurs autorisées : Un nombre compris entre 0 et 1  - `thdrVoltageR`: Distorsion harmonique totale (R) de la tension dans la phase R. Valeurs autorisées : Un nombre compris entre 0 et 1  - `thdrVoltageS`: Distorsion harmonique totale (S) de la tension dans la phase S. Valeurs autorisées : Un nombre compris entre 0 et 1  - `thdrVoltageT`: Distorsion harmonique totale (T) de la tension dans la phase T. Valeurs autorisées : Un nombre compris entre 0 et 1  - `totalActivePower`: Puissance active actuellement consommée (en comptant toutes les phases)  - `totalReactivePower`: Puissance réactive actuellement consommée (en comptant toutes les phases)  - `type`: Type d'entité NGSI. Il doit s'agir de StreetlightControlCabinet  - `voltageR`: Tension électrique en phase R  - `voltageS`: Tension électrique en phase S  - `voltageT`: Tension électrique en phase T  - `workingMode`: Mode de fonctionnement de ce contrôleur de cabinet.  Automatique : le contrôleur d'armoire décide automatiquement de l'allumage et de l'extinction des groupes de lumières. Le fonctionnement manuel n'est pas autorisé. Manuelle : l'intervention humaine est nécessaire pour l'allumage et l'extinction. Semi-automatique : même chose qu'en automatique, mais dans ce cas, l'intervention manuelle est autorisée.    
Propriétés requises  
- `id`  - `location`  - `refStreetlightGroup`  - `type`  - `workingMode`    
Il s'agit d'un équipement, généralement situé dans la rue, utilisé pour le contrôle automatisé d'un ou de plusieurs groupes de lampadaires, c'est-à-dire d'un ou de plusieurs circuits.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StreetlightControlCabinet:    
  description: 'A Streetlight control cabinet'    
  properties:    
    activePowerR:    
      description: 'Active power consumed in R phase'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'Kilowatts (kW)'    
    activePowerS:    
      description: 'Active power consumed in S phase'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'Kilowatts (kW)'    
    activePowerT:    
      description: 'Active power consumed in T phase'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'Kilowatts (kW)'    
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
      description: 'A field reserved for annotations (incidences, remarks, etc.)'    
      items:    
        type: string    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    brandName:    
      description: 'Name of the cabinet''s brand'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/brand    
    color:    
      description: 'The color of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
    compliantWith:    
      description: 'A list of standards to which the cabinet controller is compliant with (ex. IP54)'    
      items:    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
    cosPhi:    
      description: 'Cosine of phi parameter'    
      maximum: 1    
      minimum: -1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    cupboardMadeOf:    
      description: 'Material the cabinet''s cupboard is made of. Enum:''concrete, metal, other, plastic'''    
      enum:    
        - concrete    
        - metal    
        - other    
        - plastic    
      type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateLastProgramming:    
      description: 'Date at which there was a programming operation over the cabinet'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateMeteringStarted:    
      description: 'The starting date for metering energy consumed'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateServiceStarted:    
      description: 'Date at which the cabinet controller started giving service'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    description:    
      description: 'Timestamp of the last change of lamp made'    
      type: Property    
    energyConsumed:    
      description: 'Energy consumed by the circuits controlled since metering started (since dateMeteringStarted)'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Kilowatts per hour (kWh)'    
    energyCost:    
      description: 'Cost of the energy consumed by the circuits controlled since the metering start date'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    features:    
      description: 'A list of cabinet controller features.  Those technical values considered meaningful by applications. `astronomicalClock`. The control cabinet includes an astronomical clock to deal with switching hours. `individualControl`. The control cabinet allows to control street lights individually.'    
      items:    
        enum:    
          - astronomicalClock    
          - individualControl    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
    frequency:    
      description: 'The working frequency of the circuit'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        units: 'Hertz (Hz)'    
    id:    
      anyOf: &streetlightcontrolcabinet_-_properties_-_owner_-_items_-_anyof    
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
    intensityR:    
      description: 'Electric intensity in R phase'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'Ampers (A)'    
    intensityS:    
      description: 'Electric intensity in S phase'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'Ampers (A)'    
    intensityT:    
      description: ' Electric intensity in T phase'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'Ampers (A)'    
    lastMeterReading:    
      description: 'Value of the last reading obtained from the energy consumed metering system'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
        units: 'Kilowatts per hour (kWh)'    
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
    manufacturerName:    
      description: 'Name of the cabinet''s manufacturer'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/manufacturer    
    maximumPowerAvailable:    
      description: 'The maximum power available (by contract) for the circuits controlled by this cabinet'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        units: 'Kilowatts (kW)'    
    meterReadingPeriod:    
      description: 'The periodicity of energy consumed meter readings in days'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    modelName:    
      description: 'Name of the cabinet''s model'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/model    
    name:    
      description: 'The name of this item.'    
      type: Property    
    nextActuationDeadline:    
      description: 'Deadline for next actuation to be performed (programming, testing, etc.)'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *streetlightcontrolcabinet_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    powerFactorR:    
      description: 'Power factor for phase R. Allowed values: A number between -1 and 1'    
      maximum: 1    
      minimum: -1    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    powerFactorS:    
      description: 'Power factor for phase S. Allowed values: A number between -1 and 1'    
      maximum: 1    
      minimum: -1    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    powerFactorT:    
      description: 'Power factor for phase T. Allowed values: A number between -1 and 1'    
      maximum: 1    
      minimum: -1    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    reactiveEnergyConsumed:    
      description: 'Energy consumed (with regards to reactive power) by circuits since the metering start date'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'KiloVolts-Ampere-Reactive per hour (kVArh)'    
    reactivePowerR:    
      description: 'Reactive power in R phase'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'KiloVolts-Ampere-Reactive (kVArh)'    
    reactivePowerS:    
      description: 'Reactive power in S phase'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'KiloVolts-Ampere-Reactive (kVArh)'    
    reactivePowerT:    
      description: 'Reactive power in T phase'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'KiloVolts-Ampere-Reactive (kVArh)'    
    refDevice:    
      description: 'Reference to the device(s) used to monitor this control cabinet.'    
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
    refStreetlightGroup:    
      description: 'Streetlight group(s) controlled. List of references to entities of type StreetlightGroup'    
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
    responsible:    
      description: 'Responsible for the cabinet controller, i.e. entity in charge of actuating (programming, etc.).'    
      type: Property    
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
    serialNumber:    
      description: 'Serial number of the container.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/serialNumber    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    thdrIntensityR:    
      description: 'Total harmonic distortion (R) of intensity in phase R. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    thdrIntensityS:    
      description: 'Total harmonic distortion (S) of intensity in phase S. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    thdrIntensityT:    
      description: 'Total harmonic distortion (T) of intensity in phase T. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    thdrVoltageR:    
      description: 'Total harmonic distortion (R) of voltage in phase R. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    thdrVoltageS:    
      description: 'Total harmonic distortion (S) of voltage in phase S. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    thdrVoltageT:    
      description: 'Total harmonic distortion (T) of voltage in phase T. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    totalActivePower:    
      description: 'Active power currently consumed (counting all phases)'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        units: 'KiloWatts (kW)'    
    totalReactivePower:    
      description: 'Reactive power currently consumed (counting all phases)'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        units: 'KiloVolts-Ampere-Reactive (kVArh)'    
    type:    
      description: 'NGSI Entity type. It has to be StreetlightControlCabinet'    
      enum:    
        - StreetlightControlCabinet    
      type: Property    
    voltageR:    
      description: 'Electric tension in phase R'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'Volts (V)'    
    voltageS:    
      description: 'Electric tension in phase S'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'Volts (V)'    
    voltageT:    
      description: 'Electric tension in phase T'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'Volts (V)'    
    workingMode:    
      description: 'Working mode for this cabinet controller.  `automatic` : The cabinet controller decides automatically when light groups are switched on and off. Manual operation is not allowed. `manual` : Human intervention is required for switching on and off. `semiautomatic` : The same as `automatic` but in this case manual intervention is allowed.'    
      enum:    
        - automatic    
        - manual    
        - semiautomatic    
      type: Property    
  required:    
    - id    
    - type    
    - location    
    - refStreetlightGroup    
    - workingMode    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### StreetlightControlCabinet NGSI V2 valeurs clés Exemple  
Voici un exemple d'un StreetlightControlCabinet au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "streetlightcontrolcabinet:A45HGJK",  
  "type": "StreetlightControlCabinet",  
  "location": {  
    "type": "Point",  
    "coordinates": [-3.164485591715449, 40.62785133667262]  
  },  
  "cupboardMadeOf": "plastic",  
  "brandName": "Siemens",  
  "modelName": "Simatic S7 1200",  
  "refStreetlightGroup": ["streetlightgroup:BG678", "streetlightgroup:789"],  
  "compliantWith": ["IP54"],  
  "dateLastProgramming": "2016-07-08T16:04:30.201Z",  
  "maximumPowerAvailable": 10,  
  "energyConsumed": 162456,  
  "dateMeteringStarted": "2013-07-07T15:05:59.408Z",  
  "lastMeterReading": 161237,  
  "meterReadingPeriod": 60,  
  "intensityR": 20.1,  
  "intensityS": 14.4,  
  "intensityT": 22,  
  "reactivePowerR": 45,  
  "reactivePowerS": 43.5,  
  "reactivePowerT": 42,  
  "workingMode": "automatic"  
}  
```  
#### StreetlightControlCabinet NGSI V2 normalisé Exemple  
Voici un exemple d'un StreetlightControlCabinet au format JSON tel que normalisé. Il est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "streetlightcontrolcabinet:A45HGJK",  
  "type": "StreetlightControlCabinet",  
  "modelName": {  
    "value": "Simatic S7 1200"  
  },  
  "lastMeterReading": {  
    "value": 161237  
  },  
  "dateMeteringStarted": {  
    "type": "DateTime",  
    "value": "2013-07-07T15:05:59.408Z"  
  },  
  "dateLastProgramming": {  
    "type": "DateTime",  
    "value": "2016-07-08T16:04:30.201Z"  
  },  
  "refStreetlightGroup": {  
    "type": "Relationship",  
    "value": ["streetlightgroup:BG678", "streetlightgroup:789"]  
  },  
  "compliantWith": {  
    "value": ["IP54"]  
  },  
  "intensityR": {  
    "type": "Number",  
    "value": 20.1  
  },  
  "intensityS": {  
    "type": "Number",  
    "value": 14.4  
  },  
  "intensityT": {  
    "type": "Number",  
    "value": 22  
  },  
  "workingMode": {  
    "value": "automatic"  
  },  
  "energyConsumed": {  
    "value": 162456  
  },  
  "meterReadingPeriod": {  
    "value": 60  
  },  
  "cupboardMadeOf": {  
    "value": "plastic"  
  },  
  "brandName": {  
    "value": "Siemens"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-3.164485591715449, 40.62785133667262]  
    }  
  },  
  "reactivePowerR": {  
    "type": "Number",  
    "value": 45  
  },  
  "reactivePowerS": {  
    "type": "Number",  
    "value": 43.5  
  },  
  "reactivePowerT": {  
    "type": "Number",  
    "value": 42  
  },  
  "maximumPowerAvailable": {  
    "value": 10  
  }  
}  
```  
#### StreetlightControlCabinet NGSI-LD valeurs clés Exemple  
Voici un exemple d'un StreetlightControlCabinet au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "brandName": "Siemens",  
 "compliantWith": ["IP54"],  
 "cupboardMadeOf": "plastic",  
 "dateLastProgramming": {"@type": "DateTime",  
                         "@value": "2016-07-08T16:04:30.201Z"},  
 "dateMeteringStarted": {"@type": "DateTime",  
                         "@value": "2013-07-07T15:05:59.408Z"},  
 "energyConsumed": 162456,  
 "id": "urn:ngsi-ld:StreetlightControlCabinet:streetlightcontrolcabinet:A45HGJK",  
 "intensityR": 20.1,  
 "intensityS": 14.4,  
 "intensityT": 22,  
 "lastMeterReading": 161237,  
 "location": {"coordinates": [-3.164485591715449, 40.62785133667262],  
              "type": "Point"},  
 "maximumPowerAvailable": 10,  
 "meterReadingPeriod": 60,  
 "modelName": "Simatic S7 1200",  
 "reactivePowerR": 45,  
 "reactivePowerS": 43.5,  
 "reactivePowerT": 42,  
 "refStreetlightGroup": ["urn:ngsi-ld:StreetlightGroup:streetlightgroup:BG678",  
                         "urn:ngsi-ld:StreetlightGroup:streetlightgroup:789"],  
 "type": "StreetlightControlCabinet",  
 "workingMode": "automatic"}  
```  
#### StreetlightControlCabinet NGSI-LD normalisé Exemple  
Voici un exemple d'un StreetlightControlCabinet au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:StreetlightControlCabinet:streetlightcontrolcabinet:A45HGJK",  
    "type": "StreetlightControlCabinet",  
    "modelName": {  
        "type": "Property",  
        "value": "Simatic S7 1200"  
    },  
    "lastMeterReading": {  
        "type": "Property",  
        "value": 161237  
    },  
    "dateMeteringStarted": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2013-07-07T15:05:59.408Z"  
        }  
    },  
    "dateLastProgramming": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-07-08T16:04:30.201Z"  
        }  
    },  
    "refStreetlightGroup": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:StreetlightGroup:streetlightgroup:BG678",  
            "urn:ngsi-ld:StreetlightGroup:streetlightgroup:789"  
        ]  
    },  
    "compliantWith": {  
        "type": "Property",  
        "value": [  
            "IP54"  
        ]  
    },  
    "intensityR": {  
        "type": "Property",  
        "value": 20.1  
    },  
    "intensityS": {  
        "type": "Property",  
        "value": 14.4  
    },  
    "intensityT": {  
        "type": "Property",  
        "value": 22  
    },  
    "workingMode": {  
        "type": "Property",  
        "value": "automatic"  
    },  
    "energyConsumed": {  
        "type": "Property",  
        "value": 162456  
    },  
    "meterReadingPeriod": {  
        "type": "Property",  
        "value": 60  
    },  
    "cupboardMadeOf": {  
        "type": "Property",  
        "value": "plastic"  
    },  
    "brandName": {  
        "type": "Property",  
        "value": "Siemens"  
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
    "reactivePowerR": {  
        "type": "Property",  
        "value": 45  
    },  
    "reactivePowerS": {  
        "type": "Property",  
        "value": 43.5  
    },  
    "reactivePowerT": {  
        "type": "Property",  
        "value": 42  
    },  
    "maximumPowerAvailable": {  
        "type": "Property",  
        "value": 10  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
