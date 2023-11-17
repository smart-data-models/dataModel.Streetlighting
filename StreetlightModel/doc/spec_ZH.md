<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：路灯模型    
=======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightModel/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：**A 路灯型号**    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: 该项目的替代名称  - `annotations[array]`: 项目说明  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: 实现路灯的资产类型。枚举：'`postTop, bollard, lamppost, lightTower, flashingBeacon, sideEntry, signLight, ornamentalLantern'。或其他未定义且对应用有意义的值  - `color[string]`: 产品的颜色  . Model: [https://schema.org/color](https://schema.org/color)- `colorRenderingIndex[number]`: 灯的显色指数  . Model: [https://schema.org/Number](https://schema.org/Number)- `colorTemperature[number]`: 灯的相关色温  . Model: [https://schema.org/Number](https://schema.org/Number)- `columnBrandName[string]`: 栏目品牌名称  . Model: [https://schema.org/brand](https://schema.org/brand)- `columnColor[string]`: 列的绘画颜色。允许值：W3C 颜色关键字](https://www.w3.org/TR/SVG/types.html#ColorKeywords) 指定的颜色关键字。W3C 颜色数据类型](https://www.w3.org/TR/SVG/types.html#BasicDataTypes) 中指定的颜色值。  . Model: [https://schema.org/color](https://schema.org/color)- `columnMadeOf[string]`: 柱子由材料制成。枚举:'钢、铝、木、其他  . Model: [https://schema.org/Text](https://schema.org/Text)- `columnManufacturerName[string]`: 圆柱制造商名称  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `columnModelName[string]`: 列的模型名称  . Model: [https://schema.org/model](https://schema.org/model)- `compliantWith[array]`: 该路灯型号符合的标准列表  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `image[uri]`: 物品的图片  . Model: [https://schema.org/URL](https://schema.org/URL)- `lampBrandName[string]`: 灯具品牌名称  . Model: [https://schema.org/brand](https://schema.org/brand)- `lampManufacturerName[string]`: 灯泡制造商名称  - `lampModelName[string]`: 灯泡型号名称  . Model: [https://schema.org/model](https://schema.org/model)- `lampTechnology[string]`: 灯具使用的技术。枚举："LED、LPS、HPS"。或上述列表未涵盖的、对应用有意义的任何其他值  - `lampWeight[string]`: 灯的重量  . Model: [Kilograms (kg)](Kilograms (kg))- `lanternBrandName[string]`: 灯笼品牌名称  . Model: [https://schema.org/brand](https://schema.org/brand)- `lanternManufacturerName[string]`: 灯笼制造商名称  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `lanternModelName[string]`: 灯笼型号名称  . Model: [https://schema.org/Text](https://schema.org/Text)- `lanternWeight[number]`: 灯笼的重量  . Model: [https://schema.org/weight](https://schema.org/weight)- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `luminousFlux[number]`: 灯泡可提供的最大光输出  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxPowerConsumption[number]`: 灯笼支持的最大耗电量  . Model: [https://schema.org/Number](https://schema.org/Number)- `minPowerConsumption[number]`: 灯笼支持的最低耗电量  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `powerConsumption[number]`: (灯泡（标称）耗电量  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 实体类型。必须是 StreetlightModel  - `workingLife[number]`: 灯泡无故障工作的估计小时数  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
它代表一个路灯模型，由特定的支撑结构模型、灯笼模型和灯泡模型组成。路灯实例将基于特定的路灯模型。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
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
## 有效载荷示例    
#### StreetlightModel NGSI-v2 key-values 示例    
下面是一个以 JSON-LD 格式作为键值的 StreetlightModel 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### 路灯模型 NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 StreetlightModel 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### StreetlightModel NGSI-LD key-values 示例    
下面是一个以 JSON-LD 格式作为键值的 StreetlightModel 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
#### 路灯模型 NGSI-LD 归一化示例    
下面是一个规范化 JSON-LD 格式的 StreetlightModel 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
