Entidad: Gabinete de control del alumbrado público  
==================================================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightControlCabinet/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Un armario de control del alumbrado público.  

## Lista de propiedades  

- `activePowerR`: Potencia activa consumida en la fase R  - `activePowerS`: Potencia activa consumida en la fase S  - `activePowerT`: Potencia activa consumida en la fase T  - `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `annotations`: Un campo reservado para anotaciones (incidencias, observaciones, etc.)  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `brandName`: Nombre de la marca del armario  - `color`: El color del producto  - `compliantWith`: Una lista de las normas que cumple el controlador del armario (por ejemplo, IP54)  - `cosPhi`: Coseno del parámetro phi  - `cupboardMadeOf`: Material del que está hecho el armario. Enum:'hormigón, metal, otro, plástico'  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateLastProgramming`: Fecha en la que hubo una operación de programación sobre el armario  - `dateMeteringStarted`: La fecha de inicio de la medición de la energía consumida  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateServiceStarted`: Fecha en la que el controlador del armario comenzó a dar servicio  - `description`: Marca de tiempo del último cambio de lámpara realizado  - `energyConsumed`: Energía consumida por los circuitos controlados desde el inicio de la medición (desde dateMeteringStarted)  - `energyCost`: Coste de la energía consumida por los circuitos controlados desde la fecha de inicio de la medición  - `features`: Una lista de las características del controlador del armario.  Aquellos valores técnicos considerados significativos por las aplicaciones. `Reloj astronómico`. El armario de control incluye un reloj astronómico para tratar las horas de conmutación. `ControlIndividual`. El armario de control permite controlar las farolas de forma individual.  - `frequency`: La frecuencia de trabajo del circuito  - `id`: Identificador único de la entidad  - `image`: Una imagen del artículo  - `intensityR`: Intensidad eléctrica en la fase R  - `intensityS`: Intensidad eléctrica en la fase S  - `intensityT`:  Intensidad eléctrica en la fase T  - `lastMeterReading`: Valor de la última lectura obtenida del sistema de medición de energía consumida  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `manufacturerName`: Nombre del fabricante del armario  - `maximumPowerAvailable`: La potencia máxima disponible (por contrato) para los circuitos controlados por este armario  - `meterReadingPeriod`: La periodicidad de las lecturas del contador de energía consumida en días  - `modelName`: Nombre del modelo de armario  - `name`: El nombre de este artículo.  - `nextActuationDeadline`: Fecha límite para la siguiente actuación que debe realizarse (programación, pruebas, etc.)  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `powerFactorR`: Factor de potencia para la fase R. Valores permitidos: Un número entre -1 y 1  - `powerFactorS`: Factor de potencia para la fase S. Valores permitidos: Un número entre -1 y 1  - `powerFactorT`: Factor de potencia para la fase T. Valores permitidos: Un número entre -1 y 1  - `reactiveEnergyConsumed`: Energía consumida (con respecto a la potencia reactiva) por los circuitos desde la fecha de inicio de la medición  - `reactivePowerR`: Potencia reactiva en la fase R  - `reactivePowerS`: Potencia reactiva en fase S  - `reactivePowerT`: Potencia reactiva en fase T  - `refDevice`: Referencia al dispositivo o dispositivos utilizados para supervisar este armario de control.  - `refStreetlightGroup`: Grupo(s) de farolas controlado(s). Lista de referencias a entidades de tipo StreetlightGroup  - `responsible`: Responsable del controlador del armario, es decir, entidad encargada de la actuación (programación, etc.).  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `serialNumber`: Número de serie del contenedor.  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `thdrIntensityR`: Distorsión armónica total (R) de la intensidad en la fase R. Valores permitidos: Un número entre 0 y 1  - `thdrIntensityS`: Distorsión armónica total (S) de la intensidad en la fase S. Valores permitidos: Un número entre 0 y 1  - `thdrIntensityT`: Distorsión armónica total (T) de la intensidad en la fase T. Valores permitidos: Un número entre 0 y 1  - `thdrVoltageR`: Distorsión armónica total (R) de la tensión en la fase R. Valores permitidos: Un número entre 0 y 1  - `thdrVoltageS`: Distorsión armónica total (S) de la tensión en la fase S. Valores permitidos: Un número entre 0 y 1  - `thdrVoltageT`: Distorsión armónica total (T) de la tensión en la fase T. Valores permitidos: Un número entre 0 y 1  - `totalActivePower`: Potencia activa consumida actualmente (contando todas las fases)  - `totalReactivePower`: Potencia reactiva consumida actualmente (contando todas las fases)  - `type`: Tipo de entidad NGSI. Tiene que ser StreetlightControlCabinet  - `voltageR`: Tensión eléctrica en la fase R  - `voltageS`: Tensión eléctrica en la fase S  - `voltageT`: Tensión eléctrica en la fase T  - `workingMode`: Modo de trabajo de este controlador de armario.  Automático": El controlador del armario decide automáticamente cuándo se encienden y apagan los grupos de luces. No se permite la operación manual. Manual": Se requiere la intervención humana para el encendido y el apagado. `semiautomatic` : Lo mismo que `automatic` pero en este caso se permite la intervención manual.    
Propiedades requeridas  
- `id`  - `location`  - `refStreetlightGroup`  - `type`  - `workingMode`    
Representa un equipo, generalmente en la calle, utilizado para el control automatizado de un grupo o grupos de farolas, es decir, uno o varios circuitos.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
## Ejemplo de carga útil  
#### StreetlightControlCabinet NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un StreetlightControlCabinet en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### StreetlightControlCabinet NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un StreetlightControlCabinet en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### StreetlightControlCabinet NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un StreetlightControlCabinet en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### StreetlightControlCabinet NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un StreetlightControlCabinet en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
