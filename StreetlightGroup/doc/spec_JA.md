<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティストリートライトグループ    
==================<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightGroup/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**街路灯グループ    
バージョン: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `activeProgramId[string]`: この街灯グループのアクティブなプログラムの識別子  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。      
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 公道上の特定の物件を特定する番号      
- `alternateName[string]`: この項目の別名  - `annotations[array]`: 注釈（インシデンス、備考など）用のフィールド。  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: 製品の色  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateLastSwitchingOff[date-time]`: 最後のスイッチオフのタイムスタンプ  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateLastSwitchingOn[date-time]`: 最後のスイッチオンのタイムスタンプ  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `illuminanceLevel[number]`: グループの相対照度レベル設定。許可される値：0から1の間の数値  . Model: [http://schema.org/Number](http://schema.org/Number)- `image[uri]`: 商品の画像  . Model: [https://schema.org/URL](https://schema.org/URL)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `powerState[string]`: 街灯グループの電源状態。Enum:'on, off, low, bootingUp'.Enum:'bootingUp, low, off, on'.  . Model: [htts://schema.org/Text](htts://schema.org/Text)- `refStreetlight[array]`: このグループに属する街灯エンティティのリスト。Streetlight タイプのエンティティへの参照のリスト。許容される値：グループの位置と個々の街灯の位置の間に地形的な整合性がなければならない。  - `refStreetlightControlCabinet[*]`: 街灯グループの制御盤  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `switchingMode[array]`: 最後にランプを交換したタイムスタンプ。Enum:' night-ON、night-OFF、night-LOW、always-ON、day-ON、day-OFF、day-LOW'.  - `switchingOnHours[array]`: 時間の切り替え。通常、特定の日付の特別なスケジュールを設定するために使用されます。  - `type[string]`: NGSI Entity タイプ。StreetlightGroupでなければならない。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
StreetlightGroup`型のエンティティは街灯のグループを表す。それらは同じ自動化システム（キャビネットコントローラ）によって一緒に制御されるかもしれない。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
StreetlightGroup:      
  description: A Street light group      
  properties:      
    activeProgramId:      
      description: Identifier of the active program for this streetlight group      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
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
    color:      
      description: The color of the product      
      type: string      
      x-ngsi:      
        model: https://schema.org/color      
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
    dateLastSwitchingOff:      
      description: Timestamp of the last switching off      
      format: date-time      
      type: string      
      x-ngsi:      
        model: http://schema.org/DateTime      
        type: Property      
    dateLastSwitchingOn:      
      description: Timestamp of the last switching on      
      format: date-time      
      type: string      
      x-ngsi:      
        model: http://schema.org/DateTime      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
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
      description: 'Relative illuminance level setting for the group. Allowed values: A number between 0 and 1'      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    image:      
      description: An image of the item      
      format: uri      
      type: string      
      x-ngsi:      
        model: https://schema.org/URL      
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
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
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
    powerState:      
      description: 'Streetlight group''s power state. Enum:''on, off, low, bootingUp''. Enum:''bootingUp, low, off, on'''      
      enum:      
        - bootingUp      
        - low      
        - off      
        - on      
      type: string      
      x-ngsi:      
        model: htts://schema.org/Text      
        type: Property      
    refStreetlight:      
      description: 'List of streetlight entities belonging to this group. List of references to entities fo type Streetlight. Allowed values: There must topographical integrity between the location of the group and of the individual streetlights'      
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
      description: Streetlight group's control cabinet      
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
    switchingMode:      
      description: 'Timestamp of the last change of lamp made. Enum:'' night-ON, night-OFF, night-LOW, always-ON, day-ON, day-OFF, day-LOW'''      
      items:      
        enum:      
          - night-ON      
          - night-OFF      
          - night-LOW      
          - always-ON      
          - day-ON      
          - day-OFF      
          - day-LOW      
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    switchingOnHours:      
      description: Switching on hours. It is used normally to set special schedules for certain dates      
      items:      
        properties:      
          description:      
            description: Timestamp of the last change of lamp made      
            type: string      
            x-ngsi:      
              type: Property      
          from:      
            anyOf:      
              - format: date      
              - pattern: ^--((0[13578]|1[02])-31|(0[1,3-9]|1[0-2])-30|(0\d|1[0-2])-([0-2]\d))$      
                type: string      
            type: string      
          hours:      
            description: Timestamp of the last change of lamp made      
            type: string      
            x-ngsi:      
              type: Property      
          to:      
            anyOf:      
              - format: date      
              - pattern: ^--((0[13578]|1[02])-31|(0[1,3-9]|1[0-2])-30|(0\d|1[0-2])-([0-2]\d))$      
                type: string      
            description: Ending date (it can be yearless)      
            type: string      
            x-ngsi:      
              type: Property      
        required:      
          - from      
          - to      
          - hours      
        type: object      
      type: array      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be StreetlightGroup      
      enum:      
        - StreetlightGroup      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - location      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/StreetlightGroup/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Streetlighting/Streetlight/schema.json      
  x-model-tags: ""      
  x-version: 0.1.0      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### StreetlightGroup NGSI-v2 キー値の例    
以下はStreetlightGroupをJSON-LD形式でkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "streetlightgroup:mycity:A12",  
  "type": "StreetlightGroup",  
  "location": {  
    "type": "MultiLineString",  
    "coordinates": [  
      [  
        [  
          100.0,  
          0.0  
        ],  
        [  
          101.0,  
          1.0  
        ]  
      ],  
      [  
        [  
          102.0,  
          2.0  
        ],  
        [  
          103.0,  
          3.0  
        ]  
      ]  
    ]  
  },  
  "powerState": "on",  
  "areaServed": "Calle Comercial Centro",  
  "circuitId": "C-456-A467",  
  "dateLastSwitchingOn": "2016-07-07T19:59:06.618Z",  
  "dateLastSwitchingOff": "2016-07-07T07:59:06.618Z",  
  "refStreetlightCabinetController": "cabinetcontroller:CC45A34",  
  "switchingOnHours": [  
    {  
      "from": "--11-30",  
      "to": "--01-07",  
      "hours": "Mo,Su 16:00-02:00",  
      "description": "Christmas"  
    }  
  ]  
}  
```  
</details>    
#### StreetlightGroup NGSI-v2 正規化例    
以下は、正規化された JSON-LD 形式の StreetlightGroup の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "streetlightgroup:mycity:A12",  
  "type": "StreetlightGroup",  
  "circuitId": {  
    "type": "Text",  
    "value": "C-456-A467"  
  },  
  "powerState": {  
    "type": "Text",  
    "value": "on"  
  },  
  "dateLastSwitchingOn": {  
    "type": "DateTime",  
    "value": "2016-07-07T19:59:06.618Z"  
  },  
  "refStreetlightCabinetController": {  
    "type": "Text",  
    "value": "cabinetcontroller:CC45A34"  
  },  
  "dateLastSwitchingOff": {  
    "type": "DateTime",  
    "value": "2016-07-07T07:59:06.618Z"  
  },  
  "switchingOnHours": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "hours": "Mo,Su 16:00-02:00",  
        "to": "--01-07",  
        "from": "--11-30",  
        "description": "Christmas"  
      }  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "MultiLineString",  
      "coordinates": [  
        [  
          [  
            100.0,  
            0.0  
          ],  
          [  
            101.0,  
            1.0  
          ]  
        ],  
        [  
          [  
            102.0,  
            2.0  
          ],  
          [  
            103.0,  
            3.0  
          ]  
        ]  
      ]  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Calle Comercial Centro"  
  }  
}  
```  
</details>    
#### StreetlightGroup NGSI-LD キー値の例    
以下は、StreetlightGroupをJSON-LD形式でkey-valuesとした例である。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:mycity:A12",  
  "type": "StreetlightGroup",  
  "areaServed": "Calle Comercial Centro",  
  "circuitId": "C-456-A467",  
  "dateLastSwitchingOff": "2016-07-07T07:59:06.618Z",  
  "dateLastSwitchingOn": "2016-07-07T19:59:06.618Z",  
  "location": {  
    "coordinates": [  
      [  
        [  
          100.0,  
          0.0  
        ],  
        [  
          101.0,  
          1.0  
        ]  
      ],  
      [  
        [  
          102.0,  
          2.0  
        ],  
        [  
          103.0,  
          3.0  
        ]  
      ]  
    ],  
    "type": "MultiLineString"  
  },  
  "powerState": "on",  
  "refStreetlightCabinetController": "urn:ngsi-ld:StreetlightCabinetController:cabinetcontroller:CC45A34",  
  "switchingOnHours": [  
    {  
      "description": "Christmas",  
      "from": "--11-30",  
      "hours": "Mo,Su 16:00-02:00",  
      "to": "--01-07"  
    }  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 街灯グループ NGSI-LD 正規化例    
以下は、正規化された JSON-LD 形式の StreetlightGroup の例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:mycity:A12",  
  "type": "StreetlightGroup",  
  "areaServed": {  
    "type": "Property",  
    "value": "Calle Comercial Centro"  
  },  
  "circuitId": {  
    "type": "Property",  
    "value": "C-456-A467"  
  },  
  "dateLastSwitchingOff": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-07-07T07:59:06.618Z"  
    }  
  },  
  "dateLastSwitchingOn": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-07-07T19:59:06.618Z"  
    }  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "MultiLineString",  
      "coordinates": [  
        [  
          [  
            100.0,  
            0.0  
          ],  
          [  
            101.0,  
            1.0  
          ]  
        ],  
        [  
          [  
            102.0,  
            2.0  
          ],  
          [  
            103.0,  
            3.0  
          ]  
        ]  
      ]  
    }  
  },  
  "powerState": {  
    "type": "Property",  
    "value": "on"  
  },  
  "refStreetlightCabinetController": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:StreetlightCabinetController:cabinetcontroller:CC45A34"  
  },  
  "switchingOnHours": {  
    "type": "Property",  
    "value": [  
      {  
        "hours": "Mo,Su 16:00-02:00",  
        "to": "--01-07",  
        "from": "--11-30",  
        "description": "Christmas"  
      }  
    ]  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
