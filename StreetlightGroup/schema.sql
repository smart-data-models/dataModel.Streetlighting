/* (Beta) Export of data model StreetlightGroup of the subject dataModel.Streetlighting for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE powerState_type AS ENUM ('bootingUp','low','off','on');CREATE TYPE StreetlightGroup_type AS ENUM ('StreetlightGroup');
CREATE TABLE StreetlightGroup (activeProgramId TEXT, address JSON, alternateName TEXT, annotations JSON, areaServed TEXT, color TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateLastSwitchingOff TIMESTAMP, dateLastSwitchingOn TIMESTAMP, dateModified TIMESTAMP, description TEXT, illuminanceLevel NUMERIC, image TEXT, name TEXT, owner JSON, powerState powerState_type, refStreetlight JSON, source TEXT, switchingMode JSON, switchingOnHours JSON, type StreetlightGroup_type);