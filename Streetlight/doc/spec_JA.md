エンティティストリートライト  
==============  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/Streetlight/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな説明。**街路灯**。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `annotations`: アイテムに関するアノテーション  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `circuit`: この街灯が接続され、電力を得るための回路。通常、この回路に関する詳細情報を得るための識別子が含まれている。  - `color`: 商品の色について  - `controllingMethod`: この街灯を制御するために使用される方法です。Enum:'group, individual'.  - `current`: この観測に対応する街灯の現在の値。  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateLastLampChange`: 最後に行われたランプの交換のタイムスタンプ  - `dateLastSwitchingOff`: 最後に電源を切った時のタイムスタンプ  - `dateLastSwitchingOn`: 前回の電源投入時のタイムスタンプ  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateServiceStarted`: 街路灯がサービスを開始した日  - `description`: このアイテムの説明  - `deviceInfo`: オブザベーションに関連するデバイスに関する情報です。  - `feederID`: この観測に対応する街灯に関連する街灯フィーダーパネルのユニークID。  - `feederPillarNum`: この観測に対応する街灯に関連する街灯フィーダーピラー情報。  - `id`: エンティティのユニークな識別子  - `illuminanceLevel`: 相対照度レベルの設定。0から1の間の数値。  - `image`: 街路灯の写真を含むURL  - `lanternHeight`: ランタンの高さ。アームの多い柱では、街灯ごとに異なる。また、壁掛け式の街路灯もこの特性を持つバリエーションの一つである。  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `locationCategory`: 街灯が設置されている場所のカテゴリ。Enum:'bridge, centralIsland, facade, garden, park, parking, pedestrianPath, playground, road, sidewalk, tunnel'.  - `municipalityInfo`: この観測に対応する自治体の情報  - `name`: このアイテムの名前です。  - `observationDateTime`: 最後に報告された観測時刻。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `powerConsumption`: この観測に対応するLEDや街灯の電球の消費電力。  - `powerFactor`: この観測値に対応する街路灯の力率または動作電力の割合。  - `powerRating`: 今回の観測に対応したLEDまたは街路灯の電球の定格電力。  - `powerState`: ストリートライトの電源状態。Enum:'bootingUp, low, off, on'.  - `refDevice`: Streetligthをモニターするために使用されるデバイスへの参照。Deviceタイプのエンティティ（複数可）への参照のリスト。  - `refStreetlightControlCabinet`: この街灯が個別に制御されている場合は、担当の制御盤を参照する。  - `refStreetlightGroup`: 街路灯のグループ（この街路灯が何らかのグループに属している場合）。  - `refStreetlightModel`: ストリートライトのモデル。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `status`: この街路灯の全体的なステータス。Enum:'brokenLantern', 'columnIssue', 'defectiveLamp', 'ok'  - `streetPoleNum`: この観測に対応する街灯に関連する街灯情報。  - `type`: NGSI エンティティタイプ。Streetlightである必要があります。  - `voltage`: この観測に対応する街灯の電圧値。    
必須項目  
- `id`  - `location`  - `status`  - `type`    
Streetlight`というタイプのエンティティは、都市部の街灯を表します。実際には、1つのランプにつき1つの `Streetlight` 型のエンティティが存在します。したがって、あるポールに複数のランタンが設置されている場合、設置されているランプの数だけ街灯のエンティティが存在することになります。その結果、1つの場所に1つ以上の街灯エンティティが存在することになります。Streetlight」エンティティには、構造的な特性に対応する属性はありません。このようなデータは `StreetlightModel` タイプのエンティティによって取得されます。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
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
      x-ngsi:    
        type: Geoproperty    
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
## ペイロードの例  
#### Streetlight NGSI-v2 key-valuesの例。  
JSON-LD形式でkey-valuesとしてStreetlightを表現した例です。これは`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### ストリートライト NGSI-v2 正規化例  
ここでは、JSON-LD形式のStreetlightを正規化した例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### 街灯 NGSI-LD のキーバリューの例  
JSON-LD形式でkey-valuesとしてStreetlightを表示した例です。これは`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "areaServed": "Roundabouts city entrance",  
  "circuit": "C-456-A467",  
  "controllingMethod": "individual",  
  "dateLastLampChange": {  
    "@type": "DateTime",  
    "@value": "2016-07-08T08:02:21.753Z"  
  },  
  "id": "urn:ngsi-ld:Streetlight:streetlight:guadalajara:4567",  
  "lanternHeight": 10,  
  "location": {  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ],  
    "type": "Point"  
  },  
  "locationCategory": "centralIsland",  
  "powerState": "off",  
  "refStreetlightGroup": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:G345",  
  "refStreetlightModel": "urn:ngsi-ld:StreetlightModel:streetlightmodel:STEEL_Tubular_10m",  
  "status": "ok",  
  "type": "Streetlight",  
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
#### 街灯 NGSI-LDの正規化例  
ここでは、JSON-LD形式のStreetlightを正規化した例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
  "powerConsumption": {  
    "type": "Property",  
    "value": 10  
  },  
  "current": {  
    "type": "Property",  
    "value": 250  
  },  
  "powerRating": {  
    "type": "Property",  
    "value": 5  
  },  
  "powerFactor": {  
    "type": "Property",  
    "value": 0.7  
  },  
  "voltage": {  
    "type": "Property",  
    "value": 50  
  },  
  "feederPillarNum": {  
    "type": "Property",  
    "value": "70"  
  },  
  "streetPoleNum": {  
    "type": "Property",  
    "value": "2"  
  },  
  "feederID": {  
    "type": "Property",  
    "value": "F1"  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-01-11T15:51:02+05:30"  
    }  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "iudx:Streetlight"  
  ]  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
