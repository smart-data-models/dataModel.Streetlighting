<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティ街灯モデル    
===========<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightModel/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**街灯モデル    
バージョン: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。      
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: この項目の別名  - `annotations[array]`: アイテムに関する注釈  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: 街灯を実装するアセットのタイプ。Enum:'`postTop、bollard、lamppost、lightTower、flashingBeacon、sideEntry、signLight、ornamententalLantern'.または、上記で定義されておらず、アプリケーションにとって意味のあるその他の値。  - `color[string]`: 製品の色  . Model: [https://schema.org/color](https://schema.org/color)- `colorRenderingIndex[number]`: ランプの演色評価数  . Model: [https://schema.org/Number](https://schema.org/Number)- `colorTemperature[number]`: ランプの相関色温度  . Model: [https://schema.org/Number](https://schema.org/Number)- `columnBrandName[string]`: コラムのブランド名  . Model: [https://schema.org/brand](https://schema.org/brand)- `columnColor[string]`: カラムの描画色。許容値：W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords)で指定されているカラーキーワード。W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)で指定される色値。  . Model: [https://schema.org/color](https://schema.org/color)- `columnMadeOf[string]`: カラムの材質。列挙:'スチール, アルミニウム, 木材, その他'  . Model: [https://schema.org/Text](https://schema.org/Text)- `columnManufacturerName[string]`: カラムのメーカー名  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `columnModelName[string]`: カラムのモデル名  . Model: [https://schema.org/model](https://schema.org/model)- `compliantWith[array]`: この街灯モデルが準拠している規格のリスト  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `image[uri]`: 商品の画像  . Model: [https://schema.org/URL](https://schema.org/URL)- `lampBrandName[string]`: ランプのブランド名  . Model: [https://schema.org/brand](https://schema.org/brand)- `lampManufacturerName[string]`: ランプメーカー名  - `lampModelName[string]`: ランプのモデル名  . Model: [https://schema.org/model](https://schema.org/model)- `lampTechnology[string]`: ランプが使用する技術。Enum:'LED, LPS, HPS'。または、上記のリストに含まれない、アプリケーションにとって意味のあるその他の値。  - `lampWeight[string]`: ランプの重量  . Model: [Kilograms (kg)](Kilograms (kg))- `lanternBrandName[string]`: ランタンのブランド名  . Model: [https://schema.org/brand](https://schema.org/brand)- `lanternManufacturerName[string]`: ランタンのメーカー名  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `lanternModelName[string]`: ランタンのモデル名  . Model: [https://schema.org/Text](https://schema.org/Text)- `lanternWeight[number]`: ランタンの重さ  . Model: [https://schema.org/weight](https://schema.org/weight)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `luminousFlux[number]`: ランプが提供できる最大光出力  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxPowerConsumption[number]`: ランタンがサポートする最大消費電力  . Model: [https://schema.org/Number](https://schema.org/Number)- `minPowerConsumption[number]`: ランタンがサポートする最低消費電力  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `powerConsumption[number]`: (ランプによる（公称）消費電力  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: NGSI エンティティタイプ。これは StreetlightModel でなければなりません。  - `workingLife[number]`: ランプが故障せずに動作する推定時間数  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
これは、特定の支持構造モデル、ランタンモデル、ランプモデルから構成される街灯のモデルを表している。街灯インスタンスは、特定の街灯モデルに基づいています。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
StreetlightModel:      
  description: A Street light model      
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
    category:      
      description: 'Type of asset which implements the street light. Enum:''`postTop, bollard, lamppost, lightTower, flashingBeacon, sideEntry, signLight, ornamentalLantern''. Or any other value not defined above and meaningful for the application'      
      items:      
        enum:      
          - bollard      
          - flashingBeacon      
          - lamppost      
          - lightTower      
          - ornamentalLantern      
          - postTop      
          - sideEntry      
          - signLight      
        type: string      
      minItems: 1      
      type: array      
      uniqueItems: true      
      x-ngsi:      
        type: Property      
    color:      
      description: The color of the product      
      type: string      
      x-ngsi:      
        model: https://schema.org/color      
        type: Property      
    colorRenderingIndex:      
      description: Color rendering index of the lamp      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    colorTemperature:      
      description: Correlated color temperature of the lamp      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Kelvin degrees (K)      
    columnBrandName:      
      description: Name of the column's brand      
      type: string      
      x-ngsi:      
        model: https://schema.org/brand      
        type: Property      
    columnColor:      
      description: "Column's painting color. Allowed Values: A color keyword as specified by [W3C Color Keywords](https://www.w3.org/TR/SVG/types.html#ColorKeywords). A color value as specified by [W3C Color Data Type](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)"      
      type: string      
      x-ngsi:      
        model: https://schema.org/color      
        type: Property      
    columnMadeOf:      
      description: 'Material column is made of. Enum:''steel, aluminium, wood, other'''      
      enum:      
        - steel      
        - aluminium      
        - wood      
        - other      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    columnManufacturerName:      
      description: Name of the column's manufacturer      
      type: string      
      x-ngsi:      
        model: https://schema.org/manufacturer      
        type: Property      
    columnModelName:      
      description: Name of the column's model      
      type: string      
      x-ngsi:      
        model: https://schema.org/model      
        type: Property      
    compliantWith:      
      description: A list of standards to which this streetlight model is compliant with      
      items:      
        type: string      
      minItems: 1      
      type: array      
      uniqueItems: true      
      x-ngsi:      
        model: https://schema.org/Text      
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
    image:      
      description: An image of the item      
      format: uri      
      type: string      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Property      
    lampBrandName:      
      description: Name of the lamp's brand      
      type: string      
      x-ngsi:      
        model: https://schema.org/brand      
        type: Property      
    lampManufacturerName:      
      description: Name of the lamp's manufacturer      
      type: string      
      x-ngsi:      
        type: Property      
    lampModelName:      
      description: Name of the lamp's model      
      type: string      
      x-ngsi:      
        model: https://schema.org/model      
        type: Property      
    lampTechnology:      
      description: 'Technology used by the lamp. Enum:''LED, LPS, HPS''. Or any other value not covered by the above list and meaningful to the application'      
      enum:      
        - LED      
        - LPS      
        - HPS      
      type: string      
      x-ngsi:      
        type: Property      
    lampWeight:      
      description: Lamp's weight      
      type: string      
      x-ngsi:      
        model: Kilograms (kg)      
        type: Property      
        units: Kilograms (kg)      
    lanternBrandName:      
      description: Name of the lantern's brand      
      type: string      
      x-ngsi:      
        model: https://schema.org/brand      
        type: Property      
    lanternManufacturerName:      
      description: Name of the lantern's manufacturer      
      type: string      
      x-ngsi:      
        model: https://schema.org/manufacturer      
        type: Property      
    lanternModelName:      
      description: Name of the lantern's model      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    lanternWeight:      
      description: Lantern's weight      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/weight      
        type: Property      
        units: Kilograms (kg)      
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
    luminousFlux:      
      description: Maximum light output which can be provided by the lamp      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Lumens (lm)      
    maxPowerConsumption:      
      description: Maximum power consumption supported by the lantern      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Watts (W)      
    minPowerConsumption:      
      description: Minimum power consumption supported by the lantern      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Watts (W)      
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
    powerConsumption:      
      description: (Nominal) power consumption made by the lamp      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Watts (W)      
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
    type:      
      description: NGSI Entity type. It has to be StreetlightModel      
      enum:      
        - StreetlightModel      
      type: string      
      x-ngsi:      
        type: Property      
    workingLife:      
      description: The estimated number of hours working (the lamp) without failure      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Hours      
  required:      
    - id      
    - type      
    - name      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/StreetlightModel/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Streetlighting/Streetlight/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### StreetlightModel NGSI-v2 キー値の例    
以下は、StreetlightModel を JSON-LD フォーマットの key-values で表した例である。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "streetlightmodel:TubularNumana:ASR42CG:HPS:100",  
  "type": "StreetlightModel",  
  "name": "Tubular Numana 6M - ASR42CG - Son-T 100",  
  "columnModelName": "01 TUBULAR P/T 6M NUMANA",  
  "columnColor": "green",  
  "lanternModelName": "ASR42CG",  
  "lanternManufacturerName": "Indal WRTL",  
  "lampModelName": "SON-T",  
  "lampBrandName": "Philips",  
  "lampTechnology": "HPS",  
  "powerConsumption": 100,  
  "colorTemperature": 3000,  
  "colorRenderingIndex": 25,  
  "luminousFlux": 2300,  
  "category": [  
    "postTop"  
  ]  
}  
```  
</details>    
#### StreetlightModel NGSI-v2 正規化例    
以下は正規化された JSON-LD フォーマットの StreetlightModel の例です。これは、オプションを使用しない場合は NGSI-v2 と互換性があり、個々のエンティティのコンテキスト データを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "streetlightmodel:TubularNumana:ASR42CG:HPS:100",  
  "type": "StreetlightModel",  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "postTop"  
    ]  
  },  
  "colorRenderingIndex": {  
    "type": "Number",  
    "value": 25  
  },  
  "columnColor": {  
    "type": "Text",  
    "value": "green"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Tubular Numana 6M - ASR42CG - Son-T 100"  
  },  
  "powerConsumption": {  
    "type": "Number",  
    "value": 100  
  },  
  "lanternManufacturerName": {  
    "type": "Text",  
    "value": "Indal WRTL"  
  },  
  "luminousFlux": {  
    "type": "Number",  
    "value": 2300  
  },  
  "lampTechnology": {  
    "type": "Text",  
    "value": "HPS"  
  },  
  "colorTemperature": {  
    "type": "Number",  
    "value": 3000  
  },  
  "lanternModelName": {  
    "type": "Text",  
    "value": "ASR42CG"  
  },  
  "columnModelName": {  
    "type": "Text",  
    "value": "01 TUBULAR P/T 6M NUMANA"  
  },  
  "lampModelName": {  
    "type": "Text",  
    "value": "SON-T"  
  },  
  "lampBrandName": {  
    "type": "Text",  
    "value": "Philips"  
  }  
}  
```  
</details>    
#### StreetlightModel NGSI-LD キー値の例    
以下は StreetlightModel を JSON-LD フォーマットの key-values で表した例である。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:StreetlightModel:streetlightmodel:TubularNumana:ASR42CG:HPS:100",  
  "type": "StreetlightModel",  
  "category": [  
    "postTop"  
  ],  
  "colorRenderingIndex": 25,  
  "colorTemperature": 3000,  
  "columnColor": "green",  
  "columnModelName": "01 TUBULAR P/T 6M NUMANA",  
  "lampBrandName": "Philips",  
  "lampModelName": "SON-T",  
  "lampTechnology": "HPS",  
  "lanternManufacturerName": "Indal WRTL",  
  "lanternModelName": "ASR42CG",  
  "luminousFlux": 2300,  
  "name": "Tubular Numana 6M - ASR42CG - Son-T 100",  
  "powerConsumption": 100,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 街灯モデル NGSI-LD 正規化例    
以下は正規化された JSON-LD フォーマットの StreetlightModel の例です。これは、オプションを使用しない場合の NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:StreetlightModel:streetlightmodel:TubularNumana:ASR42CG:HPS:100",  
  "type": "StreetlightModel",  
  "category": {  
    "type": "Property",  
    "value": [  
      "postTop"  
    ]  
  },  
  "colorRenderingIndex": {  
    "type": "Property",  
    "value": 25  
  },  
  "colorTemperature": {  
    "type": "Property",  
    "value": 3000  
  },  
  "columnColor": {  
    "type": "Property",  
    "value": "green"  
  },  
  "columnModelName": {  
    "type": "Property",  
    "value": "01 TUBULAR P/T 6M NUMANA"  
  },  
  "lampBrandName": {  
    "type": "Property",  
    "value": "Philips"  
  },  
  "lampModelName": {  
    "type": "Property",  
    "value": "SON-T"  
  },  
  "lampTechnology": {  
    "type": "Property",  
    "value": "HPS"  
  },  
  "lanternManufacturerName": {  
    "type": "Property",  
    "value": "Indal WRTL"  
  },  
  "lanternModelName": {  
    "type": "Property",  
    "value": "ASR42CG"  
  },  
  "luminousFlux": {  
    "type": "Property",  
    "value": 2300  
  },  
  "name": {  
    "type": "Property",  
    "value": "Tubular Numana 6M - ASR42CG - Son-T 100"  
  },  
  "powerConsumption": {  
    "type": "Property",  
    "value": 100  
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
