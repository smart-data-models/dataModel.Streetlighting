<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：路灯控制柜    
========<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightControlCabinet/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：**路灯控制柜**    
版本： 0.1.0    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `activePowerR[number]`: R 相消耗的有功功率  . Model: [http://schema.org/Number](http://schema.org/Number)- `activePowerS[number]`: S 相消耗的有功功率  . Model: [http://schema.org/Number](http://schema.org/Number)- `activePowerT[number]`: T 阶段消耗的有功功率  . Model: [http://schema.org/Number](http://schema.org/Number)- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 在公共街道上标识特定房产的编号      
- `alternateName[string]`: 该项目的替代名称  - `annotations[array]`: 项目说明  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: 橱柜品牌名称  . Model: [https://schema.org/brand](https://schema.org/brand)- `color[string]`: 产品的颜色  . Model: [https://schema.org/color](https://schema.org/color)- `compliantWith[array]`: 机柜控制器符合的标准列表（例如 IP54）  - `cosPhi[number]`: phi 参数的余弦  . Model: [https://schema.org/Number](https://schema.org/Number)- `cupboardMadeOf[string]`: 橱柜的材质。枚举："混凝土、金属、其他、塑料  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateLastProgramming[date-time]`: 对机柜进行编程操作的日期  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateMeteringStarted[date-time]`: 计量能源消耗的起始日期  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `dateServiceStarted[date-time]`: 机柜控制器开始提供服务的日期  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 项目描述  - `energyConsumed[number]`: 自计量开始（自 dateMeteringStarted）以来受控电路消耗的能量  . Model: [https://schema.org/Number](https://schema.org/Number)- `energyCost[number]`: 自计量开始之日起，受控电路所消耗能源的成本  . Model: [https://schema.org/Number](https://schema.org/Number)- `features[array]`: 机柜控制器功能列表。  应用中认为有意义的技术值。天文钟"。控制柜包括一个天文钟，用于处理切换时间。`individualControl`.控制柜允许单独控制路灯。  - `frequency[number]`: 电路的工作频率  - `id[*]`: 实体的唯一标识符  - `image[uri]`: 物品的图片  . Model: [https://schema.org/URL](https://schema.org/URL)- `intensityR[number]`: R 相的电强度  . Model: [http://schema.org/Number](http://schema.org/Number)- `intensityS[number]`: S 相的电强度  . Model: [http://schema.org/Number](http://schema.org/Number)- `intensityT[number]`: T 阶段的电强度  . Model: [http://schema.org/Number](http://schema.org/Number)- `lastMeterReading[number]`: 从能源消耗计量系统获得的最后读数值  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `location[*]`: 项目的 Geojson 引用。可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `manufacturerName[string]`: 橱柜制造商名称  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `maximumPowerAvailable[number]`: 本机柜所控制电路的最大可用功率（按合同规定  - `meterReadingPeriod[number]`: 以天为单位的能源消耗表读数周期  . Model: [http://schema.org/Number](http://schema.org/Number)- `modelName[string]`: 机柜型号名称  . Model: [https://schema.org/model](https://schema.org/model)- `name[string]`: 该项目的名称  - `nextActuationDeadline[date-time]`: 下一次执行（编程、测试等）的截止日期  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `powerFactorR[number]`: R 相的功率因数允许值：介于 -1 和 1 之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `powerFactorS[number]`: S 相的功率因数允许值：介于 -1 和 1 之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `powerFactorT[number]`: T 相的功率因数允许值：介于 -1 和 1 之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactiveEnergyConsumed[number]`: 自计量开始之日起电路消耗的能量（与无功功率有关  . Model: [https://schema.org/Number](https://schema.org/Number)- `reactivePowerR[number]`: R 相无功功率  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactivePowerS[number]`: S 相无功功率  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactivePowerT[number]`: T 相无功功率  . Model: [http://schema.org/Number](http://schema.org/Number)- `refDevice[array]`: 用于监控该控制柜的设备参考信息  - `refStreetlightGroup[array]`: 受控路灯组。路灯组类型实体引用列表  - `responsible[string]`: 负责机柜控制器，即负责执行（编程等）的实体  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `serialNumber[string]`: 集装箱序列号  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `thdrIntensityR[number]`: R 相中强度的总谐波失真 (R)：介于 0 和 1 之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrIntensityS[number]`: 相位 S 中强度的总谐波失真 (S)：介于 0 和 1 之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrIntensityT[number]`: T 相强度的总谐波失真 (T)：介于 0 和 1 之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageR[number]`: R 相电压的总谐波失真 (R)：介于 0 和 1 之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageS[number]`: S 相电压的总谐波失真 (S)：介于 0 和 1 之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageT[number]`: T 相电压的总谐波失真 (T)：介于 0 和 1 之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `totalActivePower[number]`: 当前消耗的有功功率（计算所有相位）  - `totalReactivePower[number]`: 当前消耗的无功功率（计算所有相位）  - `type[string]`: NGSI 实体类型。必须是 StreetlightControlCabinet  - `voltageR[number]`: R 相电张力  . Model: [http://schema.org/Number](http://schema.org/Number)- `voltageS[number]`: S 相电张力  . Model: [http://schema.org/Number](http://schema.org/Number)- `voltageT[number]`: T 相电张力  . Model: [http://schema.org/Number](http://schema.org/Number)- `workingMode[string]`: 机柜控制器的工作模式。  自动"： 机柜控制器自动决定灯组的开关。不允许手动操作。手动"： 需要人工干预开关。semiautomatic"（半自动）： 与 "automatic"（自动）相同，但在这种情况下允许手动操作。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `id`  - `location`  - `refStreetlightGroup`  - `type`  - `workingMode`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
它代表的设备通常位于街道上，用于自动控制一组或多组路灯，即一个或多个电路。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
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
## 有效载荷示例    
#### StreetlightControlCabinet NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 StreetlightControlCabinet 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### StreetlightControlCabinet NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 StreetlightControlCabinet 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### StreetlightControlCabinet NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 StreetlightControlCabinet 示例。当使用 `options=keyValues` 时，这与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
#### 路灯控制柜 NGSI-LD 标准化示例    
下面是一个规范化 JSON-LD 格式的 StreetlightControlCabinet 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
