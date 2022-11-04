<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。路灯控制柜  
========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightControlCabinet/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**一个路灯控制柜**  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `activePowerR[number]`: 在R相消耗的有功功率  . Model: [http://schema.org/Number](http://schema.org/Number)- `activePowerS[number]`: S相消耗的有功功率  . Model: [http://schema.org/Number](http://schema.org/Number)- `activePowerT[number]`: 在T阶段消耗的有功功率  . Model: [http://schema.org/Number](http://schema.org/Number)- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `annotations[array]`: 为注释（事件、备注等）保留的字段。  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: 橱柜的品牌名称  . Model: [https://schema.org/brand](https://schema.org/brand)- `color[string]`: 产品的颜色  . Model: [https://schema.org/color](https://schema.org/color)- `compliantWith[array]`: 机柜控制器符合的标准列表（例如：IP54）。  - `cosPhi[number]`: phi参数的余弦  . Model: [https://schema.org/Number](https://schema.org/Number)- `cupboardMadeOf[string]`: 柜子的柜子是由什么材料制成的。Enum:'混凝土、金属、其他、塑料'  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateLastProgramming[string]`: 对内阁进行编程操作的日期  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateMeteringStarted[string]`: 计量所消耗能源的起始日期  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `dateServiceStarted[string]`: 机柜控制器开始提供服务的日期  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 最后一次换灯的时间戳  - `energyConsumed[number]`: 自计量开始以来，被控制的电路所消耗的能量（自dateMeteringStarted）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `energyCost[number]`: 自计量开始之日起，被控制的电路所消耗的能源成本  . Model: [https://schema.org/Number](https://schema.org/Number)- `features[array]`: 机柜控制器的功能列表。  那些被应用认为有意义的技术值。`天文钟'。控制柜包括一个天文钟来处理开关时间。个人控制"。控制柜允许单独控制路灯。  - `frequency[number]`: 电路的工作频率  - `id[*]`: 实体的唯一标识符  - `image[string]`: 该物品的图像  . Model: [https://schema.org/URL](https://schema.org/URL)- `intensityR[number]`: R相中的电强度  . Model: [http://schema.org/Number](http://schema.org/Number)- `intensityS[number]`: S阶段的电强度  . Model: [http://schema.org/Number](http://schema.org/Number)- `intensityT[number]`: T阶段的电强度  . Model: [http://schema.org/Number](http://schema.org/Number)- `lastMeterReading[number]`: 从能源消耗计量系统获得的最后一次读数的值  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `manufacturerName[string]`: 柜子的制造商名称  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `maximumPowerAvailable[number]`: 该机柜控制的电路的最大可用功率（按合同规定）。  - `meterReadingPeriod[number]`: 能源消耗表读数的周期（天）。  . Model: [http://schema.org/Number](http://schema.org/Number)- `modelName[string]`: 橱柜的型号名称  . Model: [https://schema.org/model](https://schema.org/model)- `name[string]`: 这个项目的名称。  - `nextActuationDeadline[string]`: 下一次执行的最后期限（编程、测试等）。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `powerFactorR[number]`: R相的功率因素，允许的值。一个介于-1和1之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `powerFactorS[number]`: S相的功率因数，允许的值。一个介于-1和1之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `powerFactorT[number]`: T相的功率因素，允许的值。一个介于-1和1之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactiveEnergyConsumed[number]`: 自计量开始之日起，各电路消耗的能量（关于无功功率）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `reactivePowerR[number]`: R相中的无功功率  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactivePowerS[number]`: S相中的无功功率  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactivePowerT[number]`: T阶段的无功功率  . Model: [http://schema.org/Number](http://schema.org/Number)- `refDevice[array]`: 参考用于监测该控制柜的设备。  - `refStreetlightGroup[array]`: 控制的路灯组。对路灯组类型的实体的引用列表  - `responsible[string]`: 对机柜控制器负责，即负责执行（编程等）的实体。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `serialNumber[string]`: 容器的序列号。  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `thdrIntensityR[number]`: R相中强度的总谐波失真（R），允许的数值。一个介于0和1之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrIntensityS[number]`: S相强度的总谐波失真（S），允许的值。一个介于0和1之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrIntensityT[number]`: 强度在T相的总谐波失真（T），允许的值。一个介于0和1之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageR[number]`: R相电压的总谐波失真（R），允许的数值。0和1之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageS[number]`: S相电压的总谐波失真（S），允许的值。0和1之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageT[number]`: T相电压的总谐波失真（T），允许的值。0和1之间的数字  . Model: [http://schema.org/Number](http://schema.org/Number)- `totalActivePower[number]`: 当前消耗的有功功率（计算所有相位）。  - `totalReactivePower[number]`: 目前消耗的无功功率（计算所有相位）。  - `type[string]`: NGSI实体类型。它必须是路灯控制柜  - `voltageR[number]`: R相中的电张力  . Model: [http://schema.org/Number](http://schema.org/Number)- `voltageS[number]`: S相中的电张力  . Model: [http://schema.org/Number](http://schema.org/Number)- `voltageT[number]`: T相中的电张力  . Model: [http://schema.org/Number](http://schema.org/Number)- `workingMode[string]`: 该柜式控制器的工作模式。  自动"：机柜控制器自动决定灯组的开启和关闭。不允许手动操作。手动"：开启和关闭时需要人工干预。semiautomatic"：与 "automatic "相同，但在这种情况下允许人工干预。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `location`  - `refStreetlightGroup`  - `type`  - `workingMode`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
它代表设备，通常在街道上，用于自动控制一组（几组）路灯，即一个或多个电路。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StreetlightControlCabinet:    
  description: 'A Streetlight control cabinet'    
  properties:    
    activePowerR:    
      description: 'Active power consumed in R phase'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'Kilowatts (kW)'    
    activePowerS:    
      description: 'Active power consumed in S phase'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'Kilowatts (kW)'    
    activePowerT:    
      description: 'Active power consumed in T phase'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'Kilowatts (kW)'    
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
      description: 'A field reserved for annotations (incidences, remarks, etc.)'    
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
    brandName:    
      description: 'Name of the cabinet''s brand'    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    compliantWith:    
      description: 'A list of standards to which the cabinet controller is compliant with (ex. IP54)'    
      items:    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    cosPhi:    
      description: 'Cosine of phi parameter'    
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
    dateLastProgramming:    
      description: 'Date at which there was a programming operation over the cabinet'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateMeteringStarted:    
      description: 'The starting date for metering energy consumed'    
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
      description: 'Date at which the cabinet controller started giving service'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: 'Timestamp of the last change of lamp made'    
      type: string    
      x-ngsi:    
        type: Property    
    energyConsumed:    
      description: 'Energy consumed by the circuits controlled since metering started (since dateMeteringStarted)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilowatts per hour (kWh)'    
    energyCost:    
      description: 'Cost of the energy consumed by the circuits controlled since the metering start date'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    features:    
      description: 'A list of cabinet controller features.  Those technical values considered meaningful by applications. `astronomicalClock`. The control cabinet includes an astronomical clock to deal with switching hours. `individualControl`. The control cabinet allows to control street lights individually.'    
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
      description: 'The working frequency of the circuit'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: 'Hertz (Hz)'    
    id:    
      anyOf: &streetlightcontrolcabinet_-_properties_-_owner_-_items_-_anyof    
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
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    intensityR:    
      description: 'Electric intensity in R phase'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'Ampers (A)'    
    intensityS:    
      description: 'Electric intensity in S phase'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'Ampers (A)'    
    intensityT:    
      description: ' Electric intensity in T phase'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'Ampers (A)'    
    lastMeterReading:    
      description: 'Value of the last reading obtained from the energy consumed metering system'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
        units: 'Kilowatts per hour (kWh)'    
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
    manufacturerName:    
      description: 'Name of the cabinet''s manufacturer'    
      type: string    
      x-ngsi:    
        model: https://schema.org/manufacturer    
        type: Property    
    maximumPowerAvailable:    
      description: 'The maximum power available (by contract) for the circuits controlled by this cabinet'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: 'Kilowatts (kW)'    
    meterReadingPeriod:    
      description: 'The periodicity of energy consumed meter readings in days'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    modelName:    
      description: 'Name of the cabinet''s model'    
      type: string    
      x-ngsi:    
        model: https://schema.org/model    
        type: Property    
    name:    
      description: 'The name of this item.'    
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
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *streetlightcontrolcabinet_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      description: 'Energy consumed (with regards to reactive power) by circuits since the metering start date'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'KiloVolts-Ampere-Reactive per hour (kVArh)'    
    reactivePowerR:    
      description: 'Reactive power in R phase'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'KiloVolts-Ampere-Reactive (kVArh)'    
    reactivePowerS:    
      description: 'Reactive power in S phase'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'KiloVolts-Ampere-Reactive (kVArh)'    
    reactivePowerT:    
      description: 'Reactive power in T phase'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'KiloVolts-Ampere-Reactive (kVArh)'    
    refDevice:    
      description: 'Reference to the device(s) used to monitor this control cabinet.'    
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
    refStreetlightGroup:    
      description: 'Streetlight group(s) controlled. List of references to entities of type StreetlightGroup'    
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
    responsible:    
      description: 'Responsible for the cabinet controller, i.e. entity in charge of actuating (programming, etc.).'    
      type: string    
      x-ngsi:    
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
    serialNumber:    
      description: 'Serial number of the container.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/serialNumber    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
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
      description: 'Active power currently consumed (counting all phases)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: 'KiloWatts (kW)'    
    totalReactivePower:    
      description: 'Reactive power currently consumed (counting all phases)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: 'KiloVolts-Ampere-Reactive (kVArh)'    
    type:    
      description: 'NGSI Entity type. It has to be StreetlightControlCabinet'    
      enum:    
        - StreetlightControlCabinet    
      type: string    
      x-ngsi:    
        type: Property    
    voltageR:    
      description: 'Electric tension in phase R'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'Volts (V)'    
    voltageS:    
      description: 'Electric tension in phase S'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'Volts (V)'    
    voltageT:    
      description: 'Electric tension in phase T'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'Volts (V)'    
    workingMode:    
      description: 'Working mode for this cabinet controller.  `automatic` : The cabinet controller decides automatically when light groups are switched on and off. Manual operation is not allowed. `manual` : Human intervention is required for switching on and off. `semiautomatic` : The same as `automatic` but in this case manual intervention is allowed.'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
## ＃＃＃＃有效载荷的例子  
#### StreetlightControlCabinet NGSI-v2关键值示例  
下面是一个以JSON-LD格式作为key-values的路灯控制柜的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### 路灯控制柜NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的路灯控制柜的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### StreetlightControlCabinet NGSI-LD关键值示例  
这里有一个JSON-LD格式的路灯控制柜的例子，作为关键值。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### 路灯控制柜NGSI-LD规范化实例  
下面是一个JSON-LD格式的路灯控制柜的例子，是规范化的。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Streetlighting/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
