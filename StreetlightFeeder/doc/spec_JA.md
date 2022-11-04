<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティストリートライトフィーダー  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightFeeder/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**街路灯の制御盤 Data Model.**.  
バージョン: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `activePower[array]`: 各相の有効電力消費量。3 相の有効電力を以下の順序で組み合わせた順序付きトリプル。[R Y B］  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `deviceInfo[object]`: 観測に関連するデバイスの情報。  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: エンティティの一意な識別子  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `numStreetlight[number]`: この観測に対応するフィーダパネルに接続されている街路灯の総数を記述する。  . Model: [https://schema.org/Number](https://schema.org/Number)- `observationDateTime[string]`: 最後に報告された観測時刻。  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `phaseCurrent[array]`: 各相の電流。三相の有効電力を次の順序で並べたもの。[R Y B］  . Model: [https://schema.org/Text](https://schema.org/Text)- `phaseVoltage[array]`: 各相の電圧。三相の有効電力を次の順序で並べたもの。[R Y B］  . Model: [https://schema.org/Text](https://schema.org/Text)- `powerState[string]`: 街路灯フィーダパネルの現在の状態を示す。  . Model: [https://schema.org/Text](https://schema.org/Text)- `reactivePower[array]`: 相ごとに消費される無効電力。3 相の有効電力を以下の順序で組み合わせた順序付きトリプル。[R Y B］  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `totalActivePower[number]`: 全相で消費される総活動電力。  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalReactivePower[number]`: 全相の総無効電力。  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSIエンティティタイプ。StreetlightFeeder である必要があります。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StreetlightFeeder:    
  description: 'A streetlight control panel Data Model.'    
  properties:    
    activePower:    
      description: 'Active power consumed per phase. Ordered triple comprising of active power from three phases in the following order: [R Y B]'    
      items:    
        minItems: 3    
        type: number    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    deviceInfo:    
      description: 'Information about the device associated with the observations.'    
      properties:    
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
        rfId:    
          description: 'Property. Model:''https://schema.org/Text''. Gives the ID of the RFID reader.'    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &streetlightfeeder_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numStreetlight:    
      description: 'Describes the total number of streetlights connected to the feeder panel corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
        anyOf: *streetlightfeeder_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    phaseCurrent:    
      description: 'Current per phase. Ordered triple comprising of active power from three phases in the following order: [R Y B]'    
      items:    
        minItems: 3    
        type: number    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    phaseVoltage:    
      description: 'Voltage per phase. Ordered triple comprising of active power from three phases in the following order: [R Y B]'    
      items:    
        minItems: 3    
        type: number    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    powerState:    
      description: 'Indicates the current status of the streetlight feeder panel.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    reactivePower:    
      description: 'Reactive power consumed per phase. Ordered triple comprising of active power from three phases in the following order: [R Y B]'    
      items:    
        minItems: 3    
        type: number    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    totalActivePower:    
      description: 'Total active power consumed by all phases.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    totalReactivePower:    
      description: 'Total reactive power for all phases.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be StreetlightFeeder'    
      enum:    
        - StreetlightFeeder    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/StreetlightFeeder/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Streetlighting/StreetLightFeeder/schema.json    
  x-model-tags: IUDX    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### StreetlightFeeder NGSI-v2 key-value の例  
以下はStreetlightFeederをJSON-LD形式でkey-valuesにした例です。これは `options=keyValues` を使用した場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "https://smart-data-models.github.io/dataModel.Streetlighting/StreetLightFeeder/schema.json",  
  "type": "StreetlightFeeder",  
  "totalActivePower": 30,  
  "phaseCurrent": [  
    25,  
    28,  
    30  
  ],  
  "reactivePower": [  
    25,  
    28,  
    30  
  ],  
  "numStreetlight": 45,  
  "phaseVoltage": [  
    240,  
    120,  
    50  
  ],  
  "totalReactivePower": 200,  
  "activePower": [  
    120,  
    200,  
    150  
  ],  
  "powerState": "ON",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
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
#### StreetlightFeeder NGSI-v2 正規化例  
以下は、StreetlightFeederを正規化したJSON-LD形式の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "https://smart-data-models.github.io/dataModel.Streetlighting/StreetLightFeeder/schema.json",  
  "type": "StreetlightFeeder",  
  "totalActivePower": {  
    "type": "Number",  
    "value": 30  
  },  
  "phaseCurrent": {  
    "type": "array",  
    "value": [  
      25,  
      28,  
      30  
    ]  
  },  
  "reactivePower": {  
    "type": "array",  
    "value": [  
      25,  
      28,  
      30  
    ]  
  },  
  "numStreetlight": {  
    "type": "Number",  
    "value": 45  
  },  
  "phaseVoltage": {  
    "type": "array",  
    "value": [  
      240,  
      120,  
      50  
    ]  
  },  
  "totalReactivePower": {  
    "type": "Number",  
    "value": 200  
  },  
  "activePower": {  
    "type": "array",  
    "value": [  
      120,  
      200,  
      150  
    ]  
  },  
  "powerState": {  
    "type": "Text",  
    "value": "ON"  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "deviceInfo": {  
    "type": "StructuredValue",  
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
  },  
  "@context": [  
    "iudx:StreetLightFeeder",  
    "https://smart-data-models.github.io/dataModel.StreetLight/context.jsonld"  
  ]  
}  
```  
</details>  
#### StreetlightFeeder NGSI-LD key-value の例  
ここでは、StreetlightFeederをJSON-LD形式でkey-valuesにした例を示します。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "https://smart-data-models.github.io/dataModel.Streetlighting/StreetLightFeeder/schema.json",  
    "type": "StreetlightFeeder",  
    "activePower": [  
        120,  
        200,  
        150  
    ],  
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
    },  
    "numStreetlight": 45,  
    "observationDateTime": "2021-03-11T15:51:02+05:30",  
    "phaseCurrent": [  
        25,  
        28,  
        30  
    ],  
    "phaseVoltage": [  
        240,  
        120,  
        50  
    ],  
    "powerState": "ON",  
    "reactivePower": [  
        25,  
        28,  
        30  
    ],  
    "totalActivePower": 30,  
    "totalReactivePower": 200,  
    "@context": [  
        "iudx:StreetLightFeeder",  
        "https://smart-data-models.github.io/dataModel.StreetLight/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### StreetlightFeeder NGSI-LD 正規化例  
以下は、StreetlightFeederを正規化したJSON-LD形式の例である。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "https://smart-data-models.github.io/dataModel.Streetlighting/StreetLightFeeder/schema.json",  
    "type": "StreetlightFeeder",  
    "activePower": {  
        "type": "Property",  
        "value": [  
            120,  
            200,  
            150  
        ]  
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
    },  
    "numStreetlight": {  
        "type": "Property",  
        "value": 45  
    },  
    "observationDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-03-11T15:51:02+05:30"  
        }  
    },  
    "phaseCurrent": {  
        "type": "Property",  
        "value": [  
            25,  
            28,  
            30  
        ]  
    },  
    "phaseVoltage": {  
        "type": "Property",  
        "value": [  
            240,  
            120,  
            50  
        ]  
    },  
    "powerState": {  
        "type": "Property",  
        "value": "ON"  
    },  
    "reactivePower": {  
        "type": "Property",  
        "value": [  
            25,  
            28,  
            30  
        ]  
    },  
    "totalActivePower": {  
        "type": "Property",  
        "value": 30  
    },  
    "totalReactivePower": {  
        "type": "Property",  
        "value": 200  
    },  
    "@context": [  
        "iudx:StreetLightFeeder",  
        "https://smart-data-models.github.io/dataModel.StreetLight/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
