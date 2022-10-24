<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティストリートライトグループ  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightGroup/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**街路灯グループ**。  
バージョン: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `activeProgramId[string]`: この街路灯グループのアクティブプログラムの識別子  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `annotations[array]`: 注釈（発生状況、備考など）のために予約されたフィールドです。  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: 製品の色  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateLastSwitchingOff[string]`: 最後のスイッチオフのタイムスタンプ  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateLastSwitchingOn[string]`: 最後のスイッチオンのタイムスタンプ  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `illuminanceLevel[number]`: グループの相対的な照度レベルの設定。許可された値。0〜1までの数値  . Model: [http://schema.org/Number](http://schema.org/Number)- `image[string]`: アイテムの画像  . Model: [https://schema.org/URL](https://schema.org/URL)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `powerState[string]`: 街灯グループの電源状態。Enum:'on, off, low, bootingUp'.Enum:'bootingUp, low, off, on'.  . Model: [htts://schema.org/Text](htts://schema.org/Text)- `refStreetlight[array]`: このグループに属する街灯の実体のリスト。エンティティfoタイプStreetlightへの参照のリスト。許容される値。グループと個々の街灯の位置の間に地形的な整合性がなければならない。  - `refStreetlightControlCabinet[*]`: 街路灯グループの制御盤  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `switchingMode[array]`: 最後にランプを交換したときのタイムスタンプ。Enum:' night-ON, night-OFF, night-LOW, always-ON, day-ON, day-OFF, day-LOW'.  - `switchingOnHours[array]`: 時間を切り換えること。通常は、特定の日付に特別なスケジュールを設定するために使用します。  - `type[string]`: NGSI Entity タイプ。StreetlightGroupでなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
StreetlightGroup` 型のエンティティは、街灯のグループを表します。それらは同じ自動化システム（キャビネットコントローラ）によって一緒に制御されるかもしれません。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StreetlightGroup:    
  description: 'A Street light group'    
  properties:    
    activeProgramId:    
      description: 'Identifier of the active program for this streetlight group'    
      type: string    
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
    annotations:    
      description: 'A field reserved for annotations (incidences, remarks, etc.).'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
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
    dateLastSwitchingOff:    
      description: 'Timestamp of the last switching off'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateLastSwitchingOn:    
      description: 'Timestamp of the last switching on'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
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
    id:    
      anyOf: &streetlightgroup_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Relative illuminance level setting for the group. Allowed values: A number between 0 and 1'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *streetlightgroup_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      description: 'List of streetlight entities belonging to this group. List of references to entities fo type Streetlight. Allowed values: There must topographical integrity between the location of the group and of the individual streetlights.'    
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
      description: 'Streetlight group''s control cabinet'    
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
      description: 'Switching on hours. It is used normally to set special schedules for certain dates.'    
      items:    
        properties:    
          description:    
            description: 'Property. Timestamp of the last change of lamp made'    
            type: string    
          from:    
            oneOf:    
              - format: date    
              - pattern: ^--((0[13578]|1[02])-31|(0[1,3-9]|1[0-2])-30|(0\d|1[0-2])-([0-2]\d))$    
                type: string    
            type: string    
          hours:    
            description: 'Property. Timestamp of the last change of lamp made'    
            type: string    
          to:    
            description: 'Property. Ending date (it can be yearless)'    
            oneOf:    
              - format: date    
              - pattern: ^--((0[13578]|1[02])-31|(0[1,3-9]|1[0-2])-30|(0\d|1[0-2])-([0-2]\d))$    
                type: string    
            type: string    
        required:    
          - from    
          - to    
          - hours    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be StreetlightGroup'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/StreetlightGroup/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Streetlighting/Streetlight/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### StreetlightGroup NGSI-v2 key-value の例。  
以下はStreetlightGroupをJSON-LD形式でkey-valuesにした例です。これは、`options=keyValues`を使用したときにNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
以下は、StreetlightGroup を JSON-LD 形式で正規化した例である。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "streetlightgroup:mycity:A12",  
  "type": "StreetlightGroup",  
  "circuitId": {  
    "value": "C-456-A467"  
  },  
  "powerState": {  
    "value": "on"  
  },  
  "dateLastSwitchingOn": {  
    "type": "DateTime",  
    "value": "2016-07-07T19:59:06.618Z"  
  },  
  "refStreetlightCabinetController": {  
    "type": "Relationship",  
    "value": "cabinetcontroller:CC45A34"  
  },  
  "dateLastSwitchingOff": {  
    "type": "DateTime",  
    "value": "2016-07-07T07:59:06.618Z"  
  },  
  "switchingOnHours": {  
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
        [[100.0, 0.0], [101.0, 1.0]],  
        [[102.0, 2.0], [103.0, 3.0]]  
      ]  
    }  
  },  
  "areaServed": {  
    "value": "Calle Comercial Centro"  
  }  
}  
```  
</details>  
#### StreetlightGroup NGSI-LD key-value 例  
以下はStreetlightGroupをJSON-LD形式でkey-valuesにした例です。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータが返されます。  
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### StreetlightGroup NGSI-LD 正規化例  
以下は、StreetlightGroup を JSON-LD 形式で正規化した例である。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:StreetlightGroup:streetlightgroup:mycity:A12",  
    "type": "StreetlightGroup",  
    "areaServed": "Calle Comercial Centro",  
    "circuitId": "C-456-A467",  
    "dateLastSwitchingOff": {  
        "@type": "DateTime",  
        "@value": "2016-07-07T07:59:06.618Z"  
    },  
    "dateLastSwitchingOn": {  
        "@type": "DateTime",  
        "@value": "2016-07-07T19:59:06.618Z"  
    },  
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
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
