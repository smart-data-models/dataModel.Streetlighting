Entität: StreetlightControlCabinet  
==================================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightControlCabinet/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Ein Schaltschrank für Straßenbeleuchtung**  

## Liste der Eigenschaften  

- `activePowerR`: In der R-Phase aufgenommene Wirkleistung  - `activePowerS`: In der S-Phase aufgenommene Wirkleistung  - `activePowerT`: Aufgenommene Wirkleistung in Phase T  - `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `annotations`: Ein Feld, das für Anmerkungen (Vorkommnisse, Bemerkungen usw.) reserviert ist  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `brandName`: Name der Marke des Schranks  - `color`: Die Farbe des Produkts  - `compliantWith`: Eine Liste der Normen, denen der Schaltschrank-Controller entspricht (z. B. IP54)  - `cosPhi`: Kosinus des phi-Parameters  - `cupboardMadeOf`: Material, aus dem der Schrank gefertigt ist. Enum:'Beton, Metall, Sonstiges, Kunststoff'  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateLastProgramming`: Datum, an dem ein Programmiervorgang über den Schrank stattgefunden hat  - `dateMeteringStarted`: Das Startdatum für die Zählung der verbrauchten Energie  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `dateServiceStarted`: Datum, an dem die Schranksteuerung ihren Dienst aufgenommen hat  - `description`: Zeitstempel des zuletzt durchgeführten Lampenwechsels  - `energyConsumed`: Von den kontrollierten Stromkreisen verbrauchte Energie seit Beginn der Messung (seit dateMeteringStarted)  - `energyCost`: Kosten der Energie, die von den kontrollierten Stromkreisen seit dem Startdatum der Messung verbraucht wurde  - `features`: Eine Liste der Eigenschaften der Schranksteuerung.  Die technischen Werte, die von den Anwendungen als sinnvoll erachtet werden. astronomischeUhr`. Der Schaltschrank enthält eine astronomische Uhr zur Behandlung von Schaltzeiten. Einzelsteuerung". Der Schaltschrank ermöglicht die individuelle Steuerung von Straßenleuchten.  - `frequency`: Die Arbeitsfrequenz der Schaltung  - `id`: Eindeutiger Bezeichner der Entität  - `image`: Ein Bild des Artikels  - `intensityR`: Elektrische Intensität in der R-Phase  - `intensityS`: Elektrische Intensität in der S-Phase  - `intensityT`:  Elektrische Intensität in der T-Phase  - `lastMeterReading`: Wert der letzten Ablesung, die vom Messsystem für verbrauchte Energie erhalten wurde  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `manufacturerName`: Name des Herstellers des Schaltschranks  - `maximumPowerAvailable`: Die maximal verfügbare Leistung (nach Vertrag) für die von diesem Schrank gesteuerten Stromkreise  - `meterReadingPeriod`: Die Periodizität der Zählerstände der verbrauchten Energie in Tagen  - `modelName`: Name des Modells des Schranks  - `name`: Der Name dieses Elements.  - `nextActuationDeadline`: Termin für die nächste auszuführende Betätigung (Programmieren, Testen, etc.)  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `powerFactorR`: Leistungsfaktor für Phase R. Erlaubte Werte: Eine Zahl zwischen -1 und 1  - `powerFactorS`: Leistungsfaktor für Phase S. Erlaubte Werte: Eine Zahl zwischen -1 und 1  - `powerFactorT`: Leistungsfaktor für Phase T. Erlaubte Werte: Eine Zahl zwischen -1 und 1  - `reactiveEnergyConsumed`: Von den Stromkreisen verbrauchte Energie (in Bezug auf die Blindleistung) seit dem Startdatum der Messung  - `reactivePowerR`: Blindleistung in der R-Phase  - `reactivePowerS`: Blindleistung in der S-Phase  - `reactivePowerT`: Blindleistung in der T-Phase  - `refDevice`: Verweis auf das/die Gerät(e), das/die zur Überwachung dieses Schaltschranks verwendet wird/werden.  - `refStreetlightGroup`: Gesteuerte Straßenlampengruppe(n). Liste der Referenzen auf Entitäten des Typs StreetlightGroup  - `responsible`: Verantwortlich für die Schaltschranksteuerung, d.h. Instanz, die für die Ansteuerung (Programmierung, etc.) zuständig ist.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `serialNumber`: Seriennummer des Containers.  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `thdrIntensityR`: Gesamte harmonische Verzerrung (R) der Intensität in der Phase R. Erlaubte Werte: Eine Zahl zwischen 0 und 1  - `thdrIntensityS`: Gesamte harmonische Verzerrung (S) der Intensität in Phase S. Erlaubte Werte: Eine Zahl zwischen 0 und 1  - `thdrIntensityT`: Gesamte harmonische Verzerrung (T) der Intensität in der Phase T. Erlaubte Werte: Eine Zahl zwischen 0 und 1  - `thdrVoltageR`: Gesamte harmonische Verzerrung (R) der Spannung in Phase R. Erlaubte Werte: Eine Zahl zwischen 0 und 1  - `thdrVoltageS`: Gesamte harmonische Verzerrung (S) der Spannung in Phase S. Erlaubte Werte: Eine Zahl zwischen 0 und 1  - `thdrVoltageT`: Gesamte harmonische Verzerrung (T) der Spannung in Phase T. Erlaubte Werte: Eine Zahl zwischen 0 und 1  - `totalActivePower`: Aktuell aufgenommene Wirkleistung (alle Phasen zählend)  - `totalReactivePower`: Aktuell aufgenommene Blindleistung (alle Phasen zählend)  - `type`: NGSI Entity-Typ. Es muss StreetlightControlCabinet sein  - `voltageR`: Elektrische Spannung in Phase R  - `voltageS`: Elektrische Spannung in der Phase S  - `voltageT`: Elektrische Spannung in der Phase T  - `workingMode`: Arbeitsmodus für diesen Schaltschrank-Controller.  Automatik": Der Schaltschrank-Controller entscheidet automatisch, wann Lichtgruppen ein- und ausgeschaltet werden. Eine manuelle Bedienung ist nicht zulässig. `manuell` : Zum Ein- und Ausschalten ist ein menschlicher Eingriff erforderlich. `semiautomatisch` : Wie `automatisch`, aber in diesem Fall ist ein manueller Eingriff erlaubt.    
Erforderliche Eigenschaften  
- `id`  - `location`  - `refStreetlightGroup`  - `type`  - `workingMode`    
Es handelt sich um ein Gerät, in der Regel auf der Straße, das zur automatischen Steuerung einer oder mehrerer Gruppen von Straßenleuchten, d. h. eines oder mehrerer Stromkreise, verwendet wird.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
            format: uri    
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
## Beispiel-Nutzlasten  
#### StreetlightControlCabinet NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen StreetlightControlCabinet im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### StreetlightControlCabinet NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen StreetlightControlCabinet im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
#### StreetlightControlCabinet NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen StreetlightControlCabinet im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### StreetlightControlCabinet NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen StreetlightControlCabinet im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "brandName": "Siemens",  
  "compliantWith": [  
    "IP54"  
  ],  
  "cupboardMadeOf": "plastic",  
  "dateLastProgramming": {  
    "@type": "DateTime",  
    "@value": "2016-07-08T16:04:30.201Z"  
  },  
  "dateMeteringStarted": {  
    "@type": "DateTime",  
    "@value": "2013-07-07T15:05:59.408Z"  
  },  
  "energyConsumed": 162456,  
  "id": "urn:ngsi-ld:StreetlightControlCabinet:streetlightcontrolcabinet:A45HGJK",  
  "intensityR": 20.1,  
  "intensityS": 14.4,  
  "intensityT": 22,  
  "lastMeterReading": 161237,  
  "location": {  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ],  
    "type": "Point"  
  },  
  "maximumPowerAvailable": 10,  
  "meterReadingPeriod": 60,  
  "modelName": "Simatic S7 1200",  
  "reactivePowerR": 45,  
  "reactivePowerS": 43.5,  
  "reactivePowerT": 42,  
  "refStreetlightGroup": [  
    "urn:ngsi-ld:StreetlightGroup:streetlightgroup:BG678",  
    "urn:ngsi-ld:StreetlightGroup:streetlightgroup:789"  
  ],  
  "type": "StreetlightControlCabinet",  
  "workingMode": "automatic"  
}  
```  
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht