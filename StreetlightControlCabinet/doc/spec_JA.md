<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティStreetlightControlCabinet  
===============================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightControlCabinet/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**街路灯の制御盤**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `activePowerR[number]`: R相で消費される有効電力  . Model: [http://schema.org/Number](http://schema.org/Number)- `activePowerS[number]`: S相で消費される有効電力  . Model: [http://schema.org/Number](http://schema.org/Number)- `activePowerT[number]`: T相で消費される有効電力  . Model: [http://schema.org/Number](http://schema.org/Number)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `annotations[array]`: 注釈(発生状況、備考など)用のフィールド。  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: キャビネットのブランド名  . Model: [https://schema.org/brand](https://schema.org/brand)- `color[string]`: 製品の色  . Model: [https://schema.org/color](https://schema.org/color)- `compliantWith[array]`: キャビネットコントローラーが準拠している規格の一覧（例：IP54）。  - `cosPhi[number]`: ファイパラメータのコサイン  . Model: [https://schema.org/Number](https://schema.org/Number)- `cupboardMadeOf[string]`: キャビネットの戸棚の材質。Enum:'コンクリート, 金属, その他, プラスチック'  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateLastProgramming[string]`: キャビネットに対するプログラム操作が行われた日。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateMeteringStarted[string]`: 消費電力量の計測開始日  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateServiceStarted[string]`: キャビネットコントローラのサービス開始日  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 最後にランプを交換した時のタイムスタンプ  - `energyConsumed[number]`: 計測開始以降に制御された回路で消費された電力量（dateMeteringStarted以降）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `energyCost[number]`: 計測開始日以降に制御された回路で消費されたエネルギーコスト  . Model: [https://schema.org/Number](https://schema.org/Number)- `features[array]`: キャビネットコントローラの機能一覧です。  アプリケーションによって意味のあるものとみなされる技術的な値。`astronomicalClock`.コントロールキャビネットは、スイッチング時間に対処するための天文時計を含んでいます。`individualControl`.コントロールキャビネットは、街灯を個別に制御することができます。  - `frequency[number]`: 回路の動作周波数  - `id[*]`: エンティティの一意な識別子  - `image[string]`: アイテムの画像  . Model: [https://schema.org/URL](https://schema.org/URL)- `intensityR[number]`: R相の電気強度  . Model: [http://schema.org/Number](http://schema.org/Number)- `intensityS[number]`: S相の電気強度  . Model: [http://schema.org/Number](http://schema.org/Number)- `intensityT[number]`: T相の電気強度  . Model: [http://schema.org/Number](http://schema.org/Number)- `lastMeterReading[number]`: 消費電力量計測システムから取得した最後の読み取り値  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `manufacturerName[string]`: キャビネットのメーカー名  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `maximumPowerAvailable[number]`: このキャビネットが制御する回路で使用可能な最大電力（契約による  - `meterReadingPeriod[number]`: 消費電力量メーターの周期（日数  . Model: [http://schema.org/Number](http://schema.org/Number)- `modelName[string]`: キャビネットのモデル名  . Model: [https://schema.org/model](https://schema.org/model)- `name[string]`: このアイテムの名称です。  - `nextActuationDeadline[string]`: 次に実行される作動の期限（プログラミング、テストなど）  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `powerFactorR[number]`: R相の力率 許容値。1～1 の数値  . Model: [http://schema.org/Number](http://schema.org/Number)- `powerFactorS[number]`: S相の力率 許容値。1～1 の数値  . Model: [http://schema.org/Number](http://schema.org/Number)- `powerFactorT[number]`: T相の力率 許容値。1～1 の数値  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactiveEnergyConsumed[number]`: 計測開始日以降の回路別消費電力量（無効電力に関するもの  . Model: [https://schema.org/Number](https://schema.org/Number)- `reactivePowerR[number]`: R相の無効電力  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactivePowerS[number]`: S相の無効電力  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactivePowerT[number]`: T相の無効電力  . Model: [http://schema.org/Number](http://schema.org/Number)- `refDevice[array]`: この制御盤を監視するために使用される装置（複数可）を参照する。  - `refStreetlightGroup[array]`: 制御される街灯グループ（複数可）。StreetlightGroup 型のエンティティへの参照のリスト  - `responsible[string]`: キャビネットコントローラ、すなわち作動（プログラミングなど）を担当するエンティティを担当する。  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `serialNumber[string]`: 容器のシリアル番号。  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `thdrIntensityR[number]`: R相の強度の全高調波歪み(R) 許容値。0から1の間の数値  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrIntensityS[number]`: S相の強度の全高調波歪み(S) 許容値。0から1の間の数値  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrIntensityT[number]`: T相の強度の全高調波歪み(T) 許容値。0から1までの数値  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageR[number]`: R 相の電圧の全高調波歪み（R） 許容値。0以上1以下の数値  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageS[number]`: S 相の電圧の全高調波歪み（S） 許容値。0以上1以下の数値  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageT[number]`: T相の電圧の全高調波歪み（T） 許容値。0～1 の数値  . Model: [http://schema.org/Number](http://schema.org/Number)- `totalActivePower[number]`: 現在消費している有効電力（全相数カウント）  - `totalReactivePower[number]`: 現在消費している無効電力（全相数カウント）  - `type[string]`: NGSI エンティティタイプ。これは StreetlightControlCabinet でなければなりません。  - `voltageR[number]`: R相の電気張力  . Model: [http://schema.org/Number](http://schema.org/Number)- `voltageS[number]`: S相の電気張力  . Model: [http://schema.org/Number](http://schema.org/Number)- `voltageT[number]`: T相の電気張力  . Model: [http://schema.org/Number](http://schema.org/Number)- `workingMode[string]`: 本キャビネットコントローラーの動作モード  automatic` : 照明グループのオン・オフをキャビネット・コントローラーが自動的に決定します。手動操作はできません。manual` : オン/オフの切り替えに人の操作が必要です。semiautomatic` : `automatic` と同じですが、この場合、手動での操作が可能です。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `location`  - `refStreetlightGroup`  - `type`  - `workingMode`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
街路灯のグループ、すなわち1つまたは複数の回路の自動制御に使用される、通常は路上にある装置を表します。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
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
## ペイロードの例  
#### StreetlightControlCabinet NGSI-v2 key-value の例。  
以下は、StreetlightControlCabinetをJSON-LD形式でkey-valuesにした例です。これは、`options=keyValues` を使用した場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### StreetlightControlCabinet NGSI-v2 正規化例  
以下は、StreetlightControlCabinet を正規化した JSON-LD 形式の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### StreetlightControlCabinet NGSI-LD key-value 例  
以下はStreetlightControlCabinetをJSON-LD形式でkey-valuesにした例です。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータが返されます。  
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
#### StreetlightControlCabinet NGSI-LD 正規化例  
以下は、StreetlightControlCabinetをJSON-LD形式で正規化した例である。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
