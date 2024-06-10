<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: Streetlight    
===================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/Streetlight/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **A Street light**    
version: 0.1.0    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government      
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Number identifying a specific property on a public street      
- `alternateName[string]`: An alternative name for this item  - `annotations[array]`: Annotations about the item  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `circuit[string]`: The circuit to which this streetlight connects to and gets power from. Typically it will contain an identifier that will allow to obtain more information about such circuit  - `color[string]`: The color of the product  . Model: [https://schema.org/color](https://schema.org/color)- `controllingMethod[string]`: The method used to control this streetlight. Enum:'group, individual'.   - `current[number]`: Current value of the streetlight corresponding to this observation  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateLastLampChange[date-time]`: Timestamp of the last change of lamp made  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastSwitchingOff[date-time]`: Timestamp of the last switching off  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastSwitchingOn[date-time]`: Timestamp of the last switching on  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `dateServiceStarted[date-time]`: Date at which the streetlight started giving service  . Model: [https://schema.org/Date](https://schema.org/Date)- `description[string]`: A description of this item  - `deviceInfo[object]`: Information about the device associated with the observations  . Model: [https://schema.org/Text](https://schema.org/Text)	- `RFId[string]`: Gives the ID of the RFID reader  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceBatteryStatus[string]`: Gives the Battery charging status of the reporting device(Connected, Disconnected)  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceId[string]`: Device ID of the physical sensor/ measurement station corresponding to this observation  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceModel[object]`: Describes the information of the device, sensor or system in consideration  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceName[string]`: Device Name or Station name of the sensor device/station corresponding to this observation  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `deviceSimNumber[string]`: Gives the sim number of the device in the waste management vehicle  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `measurand[string]`: Property/properties sensed/observed/measured by the device  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `feederID[*]`: Unique ID of the streetlight feeder panel associated with the streetlight corresponding to this observation  . Model: [https://schema.org/Text](https://schema.org/Text)- `feederPillarNum[string]`: Streetlight feeder pillar information associated with the streetlight corresponding to this observation  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Unique identifier of the entity  - `illuminanceLevel[number]`: Relative illuminance level setting. A number between 0 and 1  - `image[uri]`: A URL containing a photo of the streetlight  . Model: [https://schema.org/image](https://schema.org/image)- `lanternHeight[number]`: Lantern's height. In columns with many arms this can vary between streetlights. Another variation source of this property are wall-mounted streetlights  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `locationCategory[string]`: Category of the location where the streetlight is placed. Enum:'bridge, centralIsland, facade, garden, park, parking, pedestrianPath, playground, road, sidewalk, tunnel'  - `municipalityInfo[object]`: Municipality information corresponding to this observation  . Model: [https://schema.org/Text](https://schema.org/Text)	- `cityId[string]`: City ID corresponding to this observation  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `cityName[string]`: City name corresponding to this observation  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `district[string]`: District name corresponding to this observation  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `stateName[string]`: Name of the state corresponding to this observation  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `ulbName[string]`:   . Model: [https://schema.org/Text.Name of the Urban Local Body corresponding to this observation](https://schema.org/Text.Name of the Urban Local Body corresponding to this observation)    
	- `wardNum[number]`: Ward number corresponding to this observation  . Model: [https://schema.org/Number](https://schema.org/Number)    
	- `zoneId[string]`: Zone ID corresponding to this observation  . Model: [https://schema.org/Text](https://schema.org/Text)    
- `name[string]`: The name of this item  - `observationDateTime[date-time]`: Last reported time of observation  . Model: [https://schema.org/Text](https://schema.org/Text)- `lifetimeMotionDetected`: Accumulated count of motion detections.- `lifetimePowerConsumption`: Total power consumed by the device over its entire operational lifespan.- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `powerConsumption[number]`: Power consumed by the LED or the streetlight bulb corresponding to this observation  . Model: [https://schema.org/Number](https://schema.org/Number)- `powerFactor[number]`: Power factor or the ratio of working power of the streetlight corresponding to this observation  . Model: [https://schema.org/Number](https://schema.org/Number)- `powerRating[number]`: Power rating of the LED or the streetlight bulb corresponding to this observation  . Model: [https://schema.org/Number](https://schema.org/Number)- `powerState[string]`: Streetlight's power state. Enum:'bootingUp, low, off, on'  . Model: [https://schema.org/Text](https://schema.org/Text)- `refDevice[array]`: Reference to the device(s) used to monitor this streetligth. List of Reference to entity(ies) of type Device  - `refStreetlightControlCabinet[*]`: If this streetlight is individually controlled, reference to the control cabinet in charge of  - `refStreetlightGroup[*]`: Streetlight's group, if this streetlight belongs to any group  - `refStreetlightModel[*]`: Streetlight's model  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `status[string]`: The overall status of this street light. Enum:'brokenLantern, columnIssue, defectiveLamp, ok'  - `streetPoleNum[string]`: Street pole information associated with the streetlight corresponding to this observation  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI Entity type. It has to be Streetlight  - `voltage[number]`: Voltage value of the streetlight corresponding to this observation  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Required properties    
- `id`  - `location`  - `status`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
An entity of type `Streetlight` represents a urban streetlight. Actually, there  will be an entity of type `Streetlight` per lamp. Thus, if a particular pole   holds more than one lantern there will be as many streetlight entites as   installed lamps. As a result there might be more than one streetlight entity per   location. A `Streetlight` entity does not contain any attribute corresponding to structural characteristics. Such data is captured by entities of type `StreetlightModel`.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Data Model description of properties    
Sorted alphabetically (click for details)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Streetlight:      
  description: A Street light      
  properties:      
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
    circuit:      
      description: The circuit to which this streetlight connects to and gets power from. Typically it will contain an identifier that will allow to obtain more information about such circuit      
      type: string      
      x-ngsi:      
        type: Property      
    color:      
      description: The color of the product      
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
      description: Current value of the streetlight corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
    dateLastLampChange:      
      description: Timestamp of the last change of lamp made      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateLastSwitchingOff:      
      description: Timestamp of the last switching off      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateLastSwitchingOn:      
      description: Timestamp of the last switching on      
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
      description: Date at which the streetlight started giving service      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Date      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    deviceInfo:      
      description: Information about the device associated with the observations      
      properties:      
        RFId:      
          description: Gives the ID of the RFID reader      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        deviceBatteryStatus:      
          description: 'Gives the Battery charging status of the reporting device(Connected, Disconnected)'      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        deviceId:      
          description: Device ID of the physical sensor/ measurement station corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        deviceModel:      
          description: 'Describes the information of the device, sensor or system in consideration'      
          properties:      
            brandName:      
              description: 'Name of the brand associated with an entity, e.g., sensor, device etc'      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            manufacturerName:      
              description: 'Name of the manufacturer associated with an entity, e.g., sensor, device etc'      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            modelName:      
              description: 'Name of a specific model associated with an entity, e.g., sensor, device etc'      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
            modelURL:      
              description: 'URL providing further information of a specific model associated with an entity, e.g., sensor, device etc'      
              type: string      
              x-ngsi:      
                model: https://schema.org/Text      
                type: Property      
          type: object      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        deviceName:      
          description: Device Name or Station name of the sensor device/station corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        deviceSimNumber:      
          description: Gives the sim number of the device in the waste management vehicle      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        measurand:      
          description: Property/properties sensed/observed/measured by the device      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    feederID:      
      anyOf:      
        - description: ""      
          type: string      
          x-ngsi:      
            type: Property      
        - description: ""      
          format: uri      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
      description: Unique ID of the streetlight feeder panel associated with the streetlight corresponding to this observation      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Relationship      
    feederPillarNum:      
      description: Streetlight feeder pillar information associated with the streetlight corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
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
    illuminanceLevel:      
      description: Relative illuminance level setting. A number between 0 and 1      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    image:      
      description: An image of the item      
      format: uri      
      type: string      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Property      
    lanternHeight:      
      description: Lantern's height. In columns with many arms this can vary between streetlights. Another variation source of this property are wall-mounted streetlights      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
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
      description: Municipality information corresponding to this observation      
      properties:      
        cityId:      
          description: City ID corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        cityName:      
          description: City name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        district:      
          description: District name corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        stateName:      
          description: Name of the state corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        ulbName:      
          description: ""      
          type: string      
          x-ngsi:      
            model: 'https://schema.org/Text.Name of the Urban Local Body corresponding to this observation'      
            type: Property      
        wardNum:      
          description: Ward number corresponding to this observation      
          type: number      
          x-ngsi:      
            model: https://schema.org/Number      
            type: Property      
        zoneId:      
          description: Zone ID corresponding to this observation      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    observationDateTime:      
      description: Last reported time of observation      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
    powerConsumption:      
      description: Power consumed by the LED or the streetlight bulb corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    powerFactor:      
      description: Power factor or the ratio of working power of the streetlight corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    powerRating:      
      description: Power rating of the LED or the streetlight bulb corresponding to this observation      
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
      description: Reference to the device(s) used to monitor this streetligth. List of Reference to entity(ies) of type Device      
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
    refStreetlightControlCabinet:      
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
      description: 'If this streetlight is individually controlled, reference to the control cabinet in charge of'      
      x-ngsi:      
        type: Relationship      
    refStreetlightGroup:      
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
      description: 'Streetlight''s group, if this streetlight belongs to any group'      
      x-ngsi:      
        type: Relationship      
    refStreetlightModel:      
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
      description: Streetlight's model      
      x-ngsi:      
        type: Relationship      
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
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
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
      description: Street pole information associated with the streetlight corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be Streetlight      
      enum:      
        - Streetlight      
      type: string      
      x-ngsi:      
        type: Property      
    voltage:      
      description: Voltage value of the streetlight corresponding to this observation      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/Streetlight/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Streetlighting/Streetlight/schema.json      
  x-model-tags: IUDX      
  x-version: 0.2.0      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Example payloads      
#### Streetlight NGSI-v2 key-values Example      
Here is an example of a Streetlight in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
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
    "cityId": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneId": "2",  
    "wardNum": 4  
  },  
  "deviceInfo": {  
    "rfId": "5634684",  
    "deviceBatteryStatus": "Connected",  
    "deviceName": "SL1",  
    "deviceId": "43",  
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
#### Streetlight NGSI-v2 normalized Example      
Here is an example of a Streetlight in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
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
    "type": "Text",  
    "value": "streetlightgroup:G345"  
  },  
  "refStreetlightModel": {  
    "type": "Text",  
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
    }  
  }  
}  
```  
</details>    
#### Streetlight NGSI-LD key-values Example      
Here is an example of a Streetlight in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Streetlight:streetlight:guadalajara:4567",  
  "type": "Streetlight",  
  "areaServed": "Roundabouts city entrance",  
  "circuit": "C-456-A467",  
  "controllingMethod": "individual",  
  "current": 250,  
  "dateLastLampChange": "2016-07-08T08:02:21.753Z",  
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
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Streetlight NGSI-LD normalized Example      
Here is an example of a Streetlight in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
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
      "cityId": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneId": "2",  
      "wardNum": 4  
    },  
    "deviceInfo": {  
      "type": "Property",  
      "value": {  
        "rfId": "5634684",  
        "deviceBatteryStatus": "Connected",  
        "deviceName": "SL1",  
        "deviceId": "43",  
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
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
