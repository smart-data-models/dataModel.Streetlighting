<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 가로등 제어 캐비닛  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightControlCabinet/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **가로등 제어 캐비닛**  
버전: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `activePowerR[number]`: R상에서 소비되는 유효 전력  . Model: [http://schema.org/Number](http://schema.org/Number)- `activePowerS[number]`: S상에서 소비되는 유효 전력  . Model: [http://schema.org/Number](http://schema.org/Number)- `activePowerT[number]`: T상에서 소비되는 유효 전력  . Model: [http://schema.org/Number](http://schema.org/Number)- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `annotations[array]`: 항목에 대한 주석  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: 캐비닛 브랜드 이름  . Model: [https://schema.org/brand](https://schema.org/brand)- `color[string]`: 제품의 색상  . Model: [https://schema.org/color](https://schema.org/color)- `compliantWith[array]`: 캐비닛 컨트롤러가 준수하는 표준 목록(예: IP54)  - `cosPhi[number]`: 파이 파라미터의 코사인  . Model: [https://schema.org/Number](https://schema.org/Number)- `cupboardMadeOf[string]`: 캐비닛의 찬장이 만들어진 재질. Enum:'콘크리트, 금속, 기타, 플라스틱'  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateLastProgramming[date-time]`: 캐비닛에 대한 프로그래밍 작업이 있었던 날짜  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateMeteringStarted[date-time]`: 에너지 소비량 측정 시작 날짜  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateServiceStarted[date-time]`: 캐비닛 컨트롤러가 서비스를 제공하기 시작한 날짜  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 이 항목에 대한 설명  - `energyConsumed[number]`: 계량 시작 이후 제어된 회로에서 소비한 에너지(dateMeteringStarted 이후)  . Model: [https://schema.org/Number](https://schema.org/Number)- `energyCost[number]`: 계량 시작일 이후 제어된 회로에서 소비한 에너지 비용  . Model: [https://schema.org/Number](https://schema.org/Number)- `features[array]`: 캐비닛 컨트롤러 기능 목록입니다.  애플리케이션에서 의미 있는 것으로 간주되는 기술 값입니다. 천문 시계`. 제어 캐비닛에는 전환 시간을 처리하는 천문 시계가 포함되어 있습니다. 개별제어`. 제어 캐비닛은 가로등을 개별적으로 제어할 수 있습니다.  - `frequency[number]`: 회로의 작동 주파수  - `id[*]`: 엔티티의 고유 식별자  - `image[uri]`: 항목 이미지  . Model: [https://schema.org/URL](https://schema.org/URL)- `intensityR[number]`: R 위상의 전기 강도  . Model: [http://schema.org/Number](http://schema.org/Number)- `intensityS[number]`: S상의 전기 강도  . Model: [http://schema.org/Number](http://schema.org/Number)- `intensityT[number]`:  T 위상의 전기 강도  . Model: [http://schema.org/Number](http://schema.org/Number)- `lastMeterReading[number]`: 에너지 소비량 측정 시스템에서 얻은 마지막 판독값입니다.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `manufacturerName[string]`: 캐비닛 제조업체 이름  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `maximumPowerAvailable[number]`: 이 캐비닛으로 제어되는 회로에 사용 가능한 최대 전력(계약에 따라)  - `meterReadingPeriod[number]`: 에너지 소비량 계량기 판독값의 주기(일 단위)  . Model: [http://schema.org/Number](http://schema.org/Number)- `modelName[string]`: 캐비닛 모델 이름  . Model: [https://schema.org/model](https://schema.org/model)- `name[string]`: 이 항목의 이름  - `nextActuationDeadline[date-time]`: 다음 작동(프로그래밍, 테스트 등)을 수행해야 하는 마감일  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `powerFactorR[number]`: 위상 R의 역률. 허용되는 값입니다: -1에서 1 사이의 숫자  . Model: [http://schema.org/Number](http://schema.org/Number)- `powerFactorS[number]`: 위상 S의 역률. 허용된 값입니다: -1에서 1 사이의 숫자  . Model: [http://schema.org/Number](http://schema.org/Number)- `powerFactorT[number]`: 위상 T의 역률 - 허용되는 값입니다: -1에서 1 사이의 숫자  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactiveEnergyConsumed[number]`: 계량 시작일 이후 회로별 에너지 소비량(무효 전력 관련)  . Model: [https://schema.org/Number](https://schema.org/Number)- `reactivePowerR[number]`: R 위상의 무효 전력  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactivePowerS[number]`: S상의 무효 전력  . Model: [http://schema.org/Number](http://schema.org/Number)- `reactivePowerT[number]`: T 위상의 무효 전력  . Model: [http://schema.org/Number](http://schema.org/Number)- `refDevice[array]`: 이 제어 캐비닛을 모니터링하는 데 사용되는 장치 참조  - `refStreetlightGroup[array]`: 제어되는 가로등 그룹입니다. StreetlightGroup 유형의 엔티티에 대한 참조 목록  - `responsible[string]`: 캐비닛 컨트롤러, 즉 작동(프로그래밍 등)을 담당하는 주체를 담당합니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `serialNumber[string]`: 컨테이너의 일련 번호  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `thdrIntensityR[number]`: 위상 R에서 강도의 총 고조파 왜곡(R). 허용되는 값입니다: 0에서 1 사이의 숫자  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrIntensityS[number]`: 위상 S에서 강도의 총 고조파 왜곡(S). 허용되는 값입니다: 0에서 1 사이의 숫자  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrIntensityT[number]`: 위상 T에서 강도의 총 고조파 왜곡(T). 허용되는 값입니다: 0에서 1 사이의 숫자  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageR[number]`: 위상 R에서 전압의 총 고조파 왜곡(R). 허용된 값입니다: 0에서 1 사이의 숫자  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageS[number]`: 위상 S에서 전압의 총 고조파 왜곡(S). 허용된 값입니다: 0에서 1 사이의 숫자  . Model: [http://schema.org/Number](http://schema.org/Number)- `thdrVoltageT[number]`: 위상 T에서 전압의 총 고조파 왜곡(T). 허용된 값입니다: 0에서 1 사이의 숫자  . Model: [http://schema.org/Number](http://schema.org/Number)- `totalActivePower[number]`: 현재 소비된 유효 전력(모든 단계 계산)  - `totalReactivePower[number]`: 현재 소비된 무효 전력(모든 단계 계산)  - `type[string]`: NGSI 엔티티 유형. StreetlightControlCabinet이어야 합니다.  - `voltageR[number]`: 위상 R의 전기 장력  . Model: [http://schema.org/Number](http://schema.org/Number)- `voltageS[number]`: 위상 S의 전기 장력  . Model: [http://schema.org/Number](http://schema.org/Number)- `voltageT[number]`: 위상 T의 전기 장력  . Model: [http://schema.org/Number](http://schema.org/Number)- `workingMode[string]`: 이 캐비닛 컨트롤러의 작동 모드입니다.  자동`: 캐비닛 컨트롤러가 조명 그룹을 켜고 끄는 시기를 자동으로 결정합니다. 수동 조작은 허용되지 않습니다. 수동` : 켜고 끄기 위해 사람의 개입이 필요합니다. 반자동` : `자동`과 동일하지만 이 경우 수동 개입이 허용됩니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `location`  - `refStreetlightGroup`  - `type`  - `workingMode`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
일반적으로 가로등 그룹(들), 즉 하나 이상의 회로를 자동으로 제어하는 데 사용되는 거리의 장비를 나타냅니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
## 페이로드 예시  
#### StreetlightControlCabinet NGSI-v2 키값 예제  
다음은 키값으로 JSON-LD 형식의 StreetlightControlCabinet의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### StreetlightControlCabinet NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 StreetlightControlCabinet의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### StreetlightControlCabinet NGSI-LD 키값 예시  
다음은 키값으로 JSON-LD 형식의 StreetlightControlCabinet의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### StreetlightControlCabinet NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 StreetlightControlCabinet의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
10](https://smartdatamodels.org/index.php/faqs/)를 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
