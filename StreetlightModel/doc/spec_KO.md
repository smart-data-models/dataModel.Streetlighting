<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 가로등 모델  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Streetlighting/blob/master/StreetlightModel/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **가로등 모델**  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `annotations[array]`: 항목에 대한 주석  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: 가로등을 구현하는 에셋 유형입니다. Enum:'`postTop, 볼라드, 가로등주, 라이트타워, 깜박이는 비콘, 사이드엔트리, 사인라이트, 장식용 랜턴'. 또는 위에 정의되지 않았으며 애플리케이션에 의미 있는 다른 값  - `color[string]`: 제품의 색상  . Model: [https://schema.org/color](https://schema.org/color)- `colorRenderingIndex[number]`: 램프의 연색성 지수  . Model: [https://schema.org/Number](https://schema.org/Number)- `colorTemperature[number]`: 램프의 색온도 상관관계  . Model: [https://schema.org/Number](https://schema.org/Number)- `columnBrandName[string]`: 열의 브랜드 이름  . Model: [https://schema.org/brand](https://schema.org/brand)- `columnColor[string]`: 열의 페인팅 색상입니다. 허용된 값: W3C 색상 키워드](https://www.w3.org/TR/SVG/types.html#ColorKeywords)에 지정된 색상 키워드입니다. W3C 색상 데이터 유형](https://www.w3.org/TR/SVG/types.html#BasicDataTypes)에 지정된 색상 값입니다.  . Model: [https://schema.org/color](https://schema.org/color)- `columnMadeOf[string]`: 재질 열은 무엇으로 구성됩니다. 열거형:'강철, 알루미늄, 목재, 기타'  . Model: [https://schema.org/Text](https://schema.org/Text)- `columnManufacturerName[string]`: 열의 제조업체 이름  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `columnModelName[string]`: 열의 모델 이름  . Model: [https://schema.org/model](https://schema.org/model)- `compliantWith[array]`: 이 가로등 모델이 준수하는 표준 목록입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `image[uri]`: 항목 이미지  . Model: [https://schema.org/URL](https://schema.org/URL)- `lampBrandName[string]`: 램프의 브랜드 이름  . Model: [https://schema.org/brand](https://schema.org/brand)- `lampManufacturerName[string]`: 램프 제조업체 이름  - `lampModelName[string]`: 램프의 모델 이름  . Model: [https://schema.org/model](https://schema.org/model)- `lampTechnology[string]`: 램프가 사용하는 기술. 열거형:'LED, LPS, HPS'. 또는 위 목록에 포함되지 않고 애플리케이션에 의미 있는 기타 값.  - `lampWeight[string]`: 램프 무게  . Model: [Kilograms (kg)](Kilograms (kg))- `lanternBrandName[string]`: 랜턴의 브랜드 이름  . Model: [https://schema.org/brand](https://schema.org/brand)- `lanternManufacturerName[string]`: 랜턴 제조업체 이름  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `lanternModelName[string]`: 랜턴의 모델 이름  . Model: [https://schema.org/Text](https://schema.org/Text)- `lanternWeight[number]`: 랜턴의 무게  . Model: [https://schema.org/weight](https://schema.org/weight)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `luminousFlux[number]`: 램프가 제공할 수 있는 최대 광 출력  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxPowerConsumption[number]`: 랜턴이 지원하는 최대 전력 소비량  . Model: [https://schema.org/Number](https://schema.org/Number)- `minPowerConsumption[number]`: 랜턴이 지원하는 최소 전력 소비  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `powerConsumption[number]`: 램프의 (공칭) 전력 소비량  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 엔티티 유형입니다. StreetlightModel이어야 합니다.  - `workingLife[number]`: 고장 없이 작동할 수 있는 예상 시간(램프)  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
특정 지지 구조물 모델, 랜턴 모델, 램프 모델로 구성된 가로등 모델을 나타냅니다. 가로등 인스턴스는 특정 가로등 모델을 기반으로 합니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
## 페이로드 예시  
#### StreetlightModel NGSI-v2 키값 예시  
다음은 키-값으로 JSON-LD 형식의 StreetlightModel의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### StreetlightModel NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 StreetlightModel의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "streetlightmodel:TubularNumana:ASR42CG:HPS:100",  
  "type": "StreetlightModel",  
  "category": {  
    "type": "array",  
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
#### 가로등 모델 NGSI-LD 키 값 예시  
다음은 키-값으로 JSON-LD 형식의 StreetlightModel의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### StreetlightModel NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 StreetlightModel의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
