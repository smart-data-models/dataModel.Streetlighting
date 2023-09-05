<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: ArmarioControlAlumbradoPúblico  
=======================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightControlCabinet/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Armario de control de alumbrado público  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `activePowerR[number]`: Potencia activa consumida en la fase R  . Model: [http://schema.org/Number](http://schema.org/Number)- `activePowerS[number]`: Potencia activa consumida en fase S  . Model: [http://schema.org/Number](http://schema.org/Number)- `activePowerT[number]`: Potencia activa consumida en la fase T  . Model: [http://schema.org/Number](http://schema.org/Number)- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local    
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nombre alternativo para este artículo  - `annotations[array]`: Campo reservado a las anotaciones (incidencias, observaciones, etc.)  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: Nombre de la marca del armario  . Model: [https://schema.org/brand](https://schema.org/brand)- `color[string]`: El color del producto  . Model: [https://schema.org/color](https://schema.org/color)- `compliantWith[array]`: Lista de normas que cumple el controlador del armario (por ejemplo, IP54)  - `cosPhi[number]`: Coseno del parámetro phi  . Model: [https://schema.org/Number](https://schema.org/Number)- `cupboardMadeOf[string]`: Material del que está hecho el armario. Enum:'hormigón, metal, otro, plástico'  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateLastProgramming[date-time]`: Fecha en la que se realizó una operación de programación sobre el armario  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateMeteringStarted[date-time]`: Fecha de inicio de la medición de la energía consumida  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `dateServiceStarted[date-time]`: Fecha en la que el controlador del armario empezó a dar servicio  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Marca de tiempo del último cambio de lámpara realizado  - `energyConsumed[number]`: Energía consumida por los circuitos controlados desde el inicio de la medición (desde dateMeteringStarted)  . Model: [https://schema.org/Number](https://schema.org/Number)- `energyCost[number]`: Coste de la energía consumida por los circuitos controlados desde la fecha de inicio de la medición  . Model: [https://schema.org/Number](https://schema.org/Number)- `features[array]`: Una lista de las características del controlador del armario.  Aquellos valores técnicos considerados significativos por las aplicaciones. `relojastronómico`. El armario regulador incluye un reloj astronómico para tratar las horas de conmutación. `ControlIndividual`. El armario de control permite controlar las farolas individualmente  - `frequency[number]`: La frecuencia de trabajo del circuito  - `id[*]`: Identificador único de la entidad  - `image[uri]`: Una imagen del artículo  . Model: [https://schema.org/URL](https://schema.org/URL)- `intensityR[number]`: Intensidad eléctrica en fase R  . Model: [http://schema.org/Number](http://schema.org/Number)- `intensityS[number]`: Intensidad eléctrica en fase S  . Model: [http://schema.org/Number](http://schema.org/Number)- `intensityT[number]`:  Intensidad eléctrica en fase T  . Model: [http://schema.org/Number](http://schema.org/Number)- `lastMeterReading[number]`: Valor de la última lectura obtenida del sistema de medición de la energía consumida  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `manufacturerName[string]`: Nombre del fabricante del armario  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `maximumPowerAvailable[number]`: La potencia máxima disponible (por contrato) para los circuitos controlados por este armario.  - `meterReadingPeriod[number]`: La periodicidad de las lecturas del contador de energía consumida en días  . Model: [http://schema.org/Number](http://schema.org/Number)- `modelName[string]`: Nombre del modelo de armario  . Model: [https://schema.org/model](https://schema.org/model)- `name[string]`: El nombre de este artículo  - `nextActuationDeadline[date-time]`: Fecha límite para realizar la siguiente actuación (programación, pruebas, etc.)  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `powerFactorR[number]`: Factor de potencia para la fase R. Valores permitidos: Un número entre -1 y 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `powerFactorS[number]`: Factor de potencia para la fase S. Valores permitidos: Un número entre -1 y 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `powerFactorT[number]`: Factor de potencia para la fase T. Valores permitidos: Un número entre -1 y 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactiveEnergyConsumed[number]`: Energía consumida (con respecto a la potencia reactiva) por los circuitos desde la fecha de inicio de la medición  . Model: [https://schema.org/Number](https://schema.org/Number)- `reactivePowerR[number]`: Potencia reactiva en fase R  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactivePowerS[number]`: Potencia reactiva en fase S  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactivePowerT[number]`: Potencia reactiva en fase T  . Model: [http://schema.org/Number](http://schema.org/Number)- `refDevice[array]`: Referencia al dispositivo o dispositivos utilizados para supervisar este armario eléctrico  - `refStreetlightGroup[array]`: Grupo(s) de farolas controlado(s). Lista de referencias a entidades de tipo StreetlightGroup  - `responsible[string]`: Responsable del controlador del armario, es decir, entidad encargada de accionar (programar, etc.)  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `serialNumber[string]`: Número de serie del contenedor  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `thdrIntensityR[number]`: Distorsión armónica total (R) de la intensidad en fase R. Valores permitidos: Un número entre 0 y 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrIntensityS[number]`: Distorsión armónica total (S) de la intensidad en fase S. Valores permitidos: Un número entre 0 y 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrIntensityT[number]`: Distorsión armónica total (T) de la intensidad en fase T. Valores permitidos: Un número entre 0 y 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageR[number]`: Distorsión armónica total (R) de la tensión en la fase R. Valores permitidos: Un número entre 0 y 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageS[number]`: Distorsión armónica total (S) de la tensión en la fase S. Valores permitidos: Un número entre 0 y 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageT[number]`: Distorsión armónica total (T) de la tensión en la fase T. Valores permitidos: Un número entre 0 y 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `totalActivePower[number]`: Potencia activa consumida actualmente (contando todas las fases)  - `totalReactivePower[number]`: Potencia reactiva consumida actualmente (contando todas las fases)  - `type[string]`: Tipo de entidad NGSI. Tiene que ser StreetlightControlCabinet  - `voltageR[number]`: Tensión eléctrica en fase R  . Model: [http://schema.org/Number](http://schema.org/Number)- `voltageS[number]`: Tensión eléctrica en fase S  . Model: [http://schema.org/Number](http://schema.org/Number)- `voltageT[number]`: Tensión eléctrica en fase T  . Model: [http://schema.org/Number](http://schema.org/Number)- `workingMode[string]`: Modo de funcionamiento de este controlador de armario.  Automático": El controlador del armario decide automáticamente cuándo se encienden y apagan los grupos de luces. No se permite el funcionamiento manual. manual` : Es necesaria la intervención humana para encender y apagar. `semiautomatic` : Igual que `automatic` pero en este caso se permite la intervención manual.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `location`  - `refStreetlightGroup`  - `type`  - `workingMode`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Representa un equipo, generalmente en la calle, utilizado para el control automatizado de un grupo o grupos de farolas, es decir, uno o varios circuitos.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StreetlightControlCabinet:    
  description: A Streetlight control cabinet    
  properties:    
    activePowerR:    
      description: Active power consumed in R phase    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Kilowatts (kW)    
    activePowerS:    
      description: Active power consumed in S phase    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Kilowatts (kW)    
    activePowerT:    
      description: Active power consumed in T phase    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Kilowatts (kW)    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: 'A field reserved for annotations (incidences, remarks, etc.)'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    brandName:    
      description: Name of the cabinet's brand    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
    color:    
      description: The color of the product    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    compliantWith:    
      description: A list of standards to which the cabinet controller is compliant with (ex. IP54)    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    cosPhi:    
      description: Cosine of phi parameter    
      maximum: 1    
      minimum: -1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cupboardMadeOf:    
      description: 'Material the cabinet''s cupboard is made of. Enum:''concrete, metal, other, plastic'''    
      enum:    
        - concrete    
        - metal    
        - other    
        - plastic    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateLastProgramming:    
      description: Date at which there was a programming operation over the cabinet    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateMeteringStarted:    
      description: The starting date for metering energy consumed    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateServiceStarted:    
      description: Date at which the cabinet controller started giving service    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: Timestamp of the last change of lamp made    
      type: string    
      x-ngsi:    
        type: Property    
    energyConsumed:    
      description: Energy consumed by the circuits controlled since metering started (since dateMeteringStarted)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilowatts per hour (kWh)    
    energyCost:    
      description: Cost of the energy consumed by the circuits controlled since the metering start date    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    features:    
      description: A list of cabinet controller features.  Those technical values considered meaningful by applications. `astronomicalClock`. The control cabinet includes an astronomical clock to deal with switching hours. `individualControl`. The control cabinet allows to control street lights individually    
      items:    
        enum:    
          - astronomicalClock    
          - individualControl    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    frequency:    
      description: The working frequency of the circuit    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: Hertz (Hz)    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    image:    
      description: An image of the item    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    intensityR:    
      description: Electric intensity in R phase    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Ampers (A)    
    intensityS:    
      description: Electric intensity in S phase    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Ampers (A)    
    intensityT:    
      description: ' Electric intensity in T phase'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Ampers (A)    
    lastMeterReading:    
      description: Value of the last reading obtained from the energy consumed metering system    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
        units: Kilowatts per hour (kWh)    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    manufacturerName:    
      description: Name of the cabinet's manufacturer    
      type: string    
      x-ngsi:    
        model: https://schema.org/manufacturer    
        type: Property    
    maximumPowerAvailable:    
      description: The maximum power available (by contract) for the circuits controlled by this cabinet    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: Kilowatts (kW)    
    meterReadingPeriod:    
      description: The periodicity of energy consumed meter readings in days    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    modelName:    
      description: Name of the cabinet's model    
      type: string    
      x-ngsi:    
        model: https://schema.org/model    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    nextActuationDeadline:    
      description: 'Deadline for next actuation to be performed (programming, testing, etc.)'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    powerFactorR:    
      description: 'Power factor for phase R. Allowed values: A number between -1 and 1'    
      maximum: 1    
      minimum: -1    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    powerFactorS:    
      description: 'Power factor for phase S. Allowed values: A number between -1 and 1'    
      maximum: 1    
      minimum: -1    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    powerFactorT:    
      description: 'Power factor for phase T. Allowed values: A number between -1 and 1'    
      maximum: 1    
      minimum: -1    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    reactiveEnergyConsumed:    
      description: Energy consumed (with regards to reactive power) by circuits since the metering start date    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: KiloVolts-Ampere-Reactive per hour (kVArh)    
    reactivePowerR:    
      description: Reactive power in R phase    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: KiloVolts-Ampere-Reactive (kVArh)    
    reactivePowerS:    
      description: Reactive power in S phase    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: KiloVolts-Ampere-Reactive (kVArh)    
    reactivePowerT:    
      description: Reactive power in T phase    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: KiloVolts-Ampere-Reactive (kVArh)    
    refDevice:    
      description: Reference to the device(s) used to monitor this control cabinet    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Relationship    
    refStreetlightGroup:    
      description: Streetlight group(s) controlled. List of references to entities of type StreetlightGroup    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Relationship    
    responsible:    
      description: 'Responsible for the cabinet controller, i.e. entity in charge of actuating (programming, etc.)'    
      type: string    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
    serialNumber:    
      description: Serial number of the container    
      type: string    
      x-ngsi:    
        model: https://schema.org/serialNumber    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    thdrIntensityR:    
      description: 'Total harmonic distortion (R) of intensity in phase R. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    thdrIntensityS:    
      description: 'Total harmonic distortion (S) of intensity in phase S. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    thdrIntensityT:    
      description: 'Total harmonic distortion (T) of intensity in phase T. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    thdrVoltageR:    
      description: 'Total harmonic distortion (R) of voltage in phase R. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    thdrVoltageS:    
      description: 'Total harmonic distortion (S) of voltage in phase S. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    thdrVoltageT:    
      description: 'Total harmonic distortion (T) of voltage in phase T. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    totalActivePower:    
      description: Active power currently consumed (counting all phases)    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: KiloWatts (kW)    
    totalReactivePower:    
      description: Reactive power currently consumed (counting all phases)    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: KiloVolts-Ampere-Reactive (kVArh)    
    type:    
      description: NGSI Entity type. It has to be StreetlightControlCabinet    
      enum:    
        - StreetlightControlCabinet    
      type: string    
      x-ngsi:    
        type: Property    
    voltageR:    
      description: Electric tension in phase R    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Volts (V)    
    voltageS:    
      description: Electric tension in phase S    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Volts (V)    
    voltageT:    
      description: Electric tension in phase T    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Volts (V)    
    workingMode:    
      description: 'Working mode for this cabinet controller.  `automatic` : The cabinet controller decides automatically when light groups are switched on and off. Manual operation is not allowed. `manual` : Human intervention is required for switching on and off. `semiautomatic` : The same as `automatic` but in this case manual intervention is allowed'    
      enum:    
        - automatic    
        - manual    
        - semiautomatic    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - refStreetlightGroup    
    - workingMode    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/StreetlightControlCabinet/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Streetlighting/StreetlightControlCabinet/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### StreetlightControlCabinet NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un StreetlightControlCabinet en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### StreetlightControlCabinet NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de StreetlightControlCabinet en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### StreetlightControlCabinet NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un StreetlightControlCabinet en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:StreetlightControlCabinet:streetlightcontrolcabinet:A45HGJK",  
  "type": "StreetlightControlCabinet",  
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
  "workingMode": "automatic",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### StreetlightControlCabinet NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de StreetlightControlCabinet en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:StreetlightControlCabinet:streetlightcontrolcabinet:A45HGJK",  
  "type": "StreetlightControlCabinet",  
  "brandName": {  
    "type": "Property",  
    "value": "Siemens"  
  },  
  "compliantWith": {  
    "type": "Property",  
    "value": [  
      "IP54"  
    ]  
  },  
  "cupboardMadeOf": {  
    "type": "Property",  
    "value": "plastic"  
  },  
  "dateLastProgramming": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-07-08T16:04:30.201Z"  
    }  
  },  
  "dateMeteringStarted": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2013-07-07T15:05:59.408Z"  
    }  
  },  
  "energyConsumed": {  
    "type": "Property",  
    "value": 162456  
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
  "lastMeterReading": {  
    "type": "Property",  
    "value": 161237  
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
  "maximumPowerAvailable": {  
    "type": "Property",  
    "value": 10  
  },  
  "meterReadingPeriod": {  
    "type": "Property",  
    "value": 60  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "Simatic S7 1200"  
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
  "refStreetlightGroup": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:StreetlightGroup:streetlightgroup:BG678",  
      "urn:ngsi-ld:StreetlightGroup:streetlightgroup:789"  
    ]  
  },  
  "workingMode": {  
    "type": "Property",  
    "value": "automatic"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
