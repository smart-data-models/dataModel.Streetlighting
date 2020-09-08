# dataModel.Streetlighting
Streetlights, commonly known as 'lamp-posts', are designed to make the streets safer for pedestrians and drivers. These data models are intended to model streetlights and all their controlling equipment towards energy-efficient and effective urban illuminance.

### List of data models

The following entity types are available:
- [Streetlight](https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/Streetlight/README.md). -> An entity of type Streetlight represents a urban streetlight. Actually, there will be an entity of type Streetlight per lamp. Thus, if a particular pole holds more than one lantern there will be as many streetlight entites as installed lamps. As a result there might be more than one streetlight entity per location. A Streetlight entity does not contain any attribute corresponding to structural characteristics. Such data is captured by entities of type StreetlightModel.

- [StreetlightControlCabinet](https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/StreetlightControlCabinet/README.md). It represents equipment, usually on street, used to the automated control of a group(s) of streetlights, i.e. one or more circuits.

- [StreetlightGroup](https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/StreetlightGroup/README.md). An entity of type StreetlightGroup represents a group of streetlights. They might be controlled together by the same automated system (cabinet controller).


- [StreetlightModel](https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/StreetlightModel/README.md). It represents a model of streetlight composed by a specific supporting structure model, a lantern model and a lamp model.
A streetlight instance will be based on a certain streetlight model.




### Contributors
[Link](https://github.com/smart-data-models/dataModel.Streetlighting/blob/master/CONTRIBUTORS.yaml) to the 9 current contributors of the data models of this Subject.


### Contribution
You can raise an [issue](https://github.com/smart-data-models/dataModel.Streetlighting/issues) or submit your [PR](https://github.com/smart-data-models/dataModel.Streetlighting/pulls) on existing data models


