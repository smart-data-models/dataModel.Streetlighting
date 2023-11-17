<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: StreetlightControlCabinet    
=================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightControlCabinet/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Un armadio di controllo per lampioni**    
versione: 0.1.0    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `activePowerR[number]`: Potenza attiva consumata nella fase R  . Model: [http://schema.org/Number](http://schema.org/Number)- `activePowerS[number]`: Potenza attiva consumata nella fase S  . Model: [http://schema.org/Number](http://schema.org/Number)- `activePowerT[number]`: Potenza attiva consumata nella fase T  . Model: [http://schema.org/Number](http://schema.org/Number)- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni Paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica      
- `alternateName[string]`: Un nome alternativo per questa voce  - `annotations[array]`: Annotazioni sull'elemento  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: Nome del marchio del mobile  . Model: [https://schema.org/brand](https://schema.org/brand)- `color[string]`: Il colore del prodotto  . Model: [https://schema.org/color](https://schema.org/color)- `compliantWith[array]`: Elenco degli standard a cui è conforme il controllore dell'armadio (es. IP54)  - `cosPhi[number]`: Coseno del parametro phi  . Model: [https://schema.org/Number](https://schema.org/Number)- `cupboardMadeOf[string]`: Materiale di cui è fatto l'armadio del mobile. Enum:'cemento, metallo, altro, plastica'.  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateLastProgramming[date-time]`: Data in cui è stata effettuata un'operazione di programmazione sul cabinet  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateMeteringStarted[date-time]`: La data di inizio della misurazione dell'energia consumata  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateServiceStarted[date-time]`: Data in cui il controllore dell'armadio ha iniziato a prestare servizio  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Descrizione dell'articolo  - `energyConsumed[number]`: Energia consumata dai circuiti controllati dall'inizio della misurazione (da dataAvvioMetering)  . Model: [https://schema.org/Number](https://schema.org/Number)- `energyCost[number]`: Costo dell'energia consumata dai circuiti controllati a partire dalla data di inizio della misurazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `features[array]`: Un elenco delle caratteristiche del controllore dell'armadio.  I valori tecnici considerati significativi dalle applicazioni. Orologio astronomico". L'armadio di comando include un orologio astronomico per gestire le ore di commutazione. `Controllo individuale`. L'armadio di comando permette di controllare i lampioni individualmente.  - `frequency[number]`: La frequenza di lavoro del circuito  - `id[*]`: Identificatore univoco dell'entità  - `image[uri]`: Un'immagine dell'articolo  . Model: [https://schema.org/URL](https://schema.org/URL)- `intensityR[number]`: Intensità elettrica nella fase R  . Model: [http://schema.org/Number](http://schema.org/Number)- `intensityS[number]`: Intensità elettrica in fase S  . Model: [http://schema.org/Number](http://schema.org/Number)- `intensityT[number]`:  Intensità elettrica in fase T  . Model: [http://schema.org/Number](http://schema.org/Number)- `lastMeterReading[number]`: Valore dell'ultima lettura ottenuta dal sistema di misurazione dell'energia consumata  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `manufacturerName[string]`: Nome del produttore del mobile  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `maximumPowerAvailable[number]`: La potenza massima disponibile (per contratto) per i circuiti controllati da questo armadio  - `meterReadingPeriod[number]`: La periodicità delle letture del contatore dell'energia consumata, espressa in giorni.  . Model: [http://schema.org/Number](http://schema.org/Number)- `modelName[string]`: Nome del modello del mobile  . Model: [https://schema.org/model](https://schema.org/model)- `name[string]`: Il nome di questo elemento  - `nextActuationDeadline[date-time]`: Termine ultimo per l'esecuzione della prossima operazione (programmazione, test, ecc.).  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `powerFactorR[number]`: Fattore di potenza per la fase R. Valori ammessi: Un numero compreso tra -1 e 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `powerFactorS[number]`: Fattore di potenza per la fase S. Valori ammessi: Un numero compreso tra -1 e 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `powerFactorT[number]`: Fattore di potenza per la fase T. Valori ammessi: Un numero compreso tra -1 e 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactiveEnergyConsumed[number]`: Energia consumata (con riferimento alla potenza reattiva) dai circuiti dalla data di inizio della misurazione  . Model: [https://schema.org/Number](https://schema.org/Number)- `reactivePowerR[number]`: Potenza reattiva nella fase R  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactivePowerS[number]`: Potenza reattiva nella fase S  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactivePowerT[number]`: Potenza reattiva nella fase T  . Model: [http://schema.org/Number](http://schema.org/Number)- `refDevice[array]`: Riferimento al/ai dispositivo/i utilizzato/i per il monitoraggio di questo quadro elettrico  - `refStreetlightGroup[array]`: Gruppo/i di lampioni controllato/i. Elenco dei riferimenti alle entità di tipo StreetlightGroup  - `responsible[string]`: Responsabile del controllore dell'armadio, ovvero soggetto incaricato dell'attuazione (programmazione, ecc.)  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `serialNumber[string]`: Numero di serie del contenitore  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `thdrIntensityR[number]`: Distorsione armonica totale (R) dell'intensità nella fase R. Valori ammessi: Un numero compreso tra 0 e 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrIntensityS[number]`: Distorsione armonica totale (S) dell'intensità nella fase S. Valori ammessi: Un numero compreso tra 0 e 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrIntensityT[number]`: Distorsione armonica totale (T) dell'intensità nella fase T. Valori ammessi: Un numero compreso tra 0 e 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageR[number]`: Distorsione armonica totale (R) della tensione nella fase R. Valori ammessi: Un numero compreso tra 0 e 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageS[number]`: Distorsione armonica totale (S) della tensione nella fase S. Valori ammessi: Un numero compreso tra 0 e 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageT[number]`: Distorsione armonica totale (T) della tensione nella fase T. Valori ammessi: Un numero compreso tra 0 e 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `totalActivePower[number]`: Potenza attiva attualmente consumata (contando tutte le fasi)  - `totalReactivePower[number]`: Potenza reattiva attualmente consumata (contando tutte le fasi)  - `type[string]`: Tipo di entità NGSI. Deve essere StreetlightControlCabinet (armadietto di controllo).  - `voltageR[number]`: Tensione elettrica nella fase R  . Model: [http://schema.org/Number](http://schema.org/Number)- `voltageS[number]`: Tensione elettrica nella fase S  . Model: [http://schema.org/Number](http://schema.org/Number)- `voltageT[number]`: Tensione elettrica in fase T  . Model: [http://schema.org/Number](http://schema.org/Number)- `workingMode[string]`: Modalità di funzionamento di questo controllore di quadri elettrici.  `automatico` : il controllore dell'armadio decide automaticamente l'accensione e lo spegnimento dei gruppi di luci. Il funzionamento manuale non è consentito. `manuale` : Per l'accensione e lo spegnimento è necessario l'intervento umano. `semiautomatico` : Come `automatico`, ma in questo caso è consentito l'intervento manuale.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `location`  - `refStreetlightGroup`  - `type`  - `workingMode`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Rappresenta un'apparecchiatura, solitamente su strada, utilizzata per il controllo automatizzato di un gruppo di lampioni, cioè di uno o più circuiti.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
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
      description: Annotations about the item      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
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
      description: A description of this item      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/StreetlightControlCabinet/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Streetlighting/StreetlightControlCabinet/schema.json      
  x-model-tags: ""      
  x-version: 0.1.0      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### StreetlightControlCabinet Valori chiave NGSI-v2 Esempio    
Ecco un esempio di StreetlightControlCabinet in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "streetlightcontrolcabinet:A45HGJK",  
  "type": "StreetlightControlCabinet",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ]  
  },  
  "cupboardMadeOf": "plastic",  
  "brandName": "Siemens",  
  "modelName": "Simatic S7 1200",  
  "refStreetlightGroup": [  
    "streetlightgroup:BG678",  
    "streetlightgroup:789"  
  ],  
  "compliantWith": [  
    "IP54"  
  ],  
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
#### StreetlightControlCabinet NGSI-v2 normalizzato Esempio    
Ecco un esempio di StreetlightControlCabinet in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "streetlightcontrolcabinet:A45HGJK",  
  "type": "StreetlightControlCabinet",  
  "modelName": {  
    "type": "Text",  
    "value": "Simatic S7 1200"  
  },  
  "lastMeterReading": {  
    "type": "Number",  
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
    "type": "StructuredValue",  
    "value": [  
      "streetlightgroup:BG678",  
      "streetlightgroup:789"  
    ]  
  },  
  "compliantWith": {  
    "type": "StructuredValue",  
    "value": [  
      "IP54"  
    ]  
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
    "type": "Text",  
    "value": "automatic"  
  },  
  "energyConsumed": {  
    "type": "Number",  
    "value": 162456  
  },  
  "meterReadingPeriod": {  
    "type": "Number",  
    "value": 60  
  },  
  "cupboardMadeOf": {  
    "type": "Text",  
    "value": "plastic"  
  },  
  "brandName": {  
    "type": "Text",  
    "value": "Siemens"  
  },  
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
    "type": "Number",  
    "value": 10  
  }  
}  
```  
</details>    
#### StreetlightControlCabinet Valori-chiave NGSI-LD Esempio    
Ecco un esempio di StreetlightControlCabinet in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
  "dateLastProgramming": "2016-07-08T16:04:30.201Z",  
  "dateMeteringStarted": "2013-07-07T15:05:59.408Z",  
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
#### StreetlightControlCabinet NGSI-LD normalizzato Esempio    
Ecco un esempio di StreetlightControlCabinet in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
