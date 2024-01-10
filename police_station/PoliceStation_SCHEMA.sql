CREATE TABLE `PoliceOfficer` (
  `OfficerID` INTEGER PRIMARY KEY,
  `Name` VARCHAR,
  `BadgeNumber` VARCHAR,
  `Rank` VARCHAR,
  `Shift` VARCHAR,
  `DateOfJoining` DATE,
  `ContactNumber` VARCHAR,
  `Address` VARCHAR
);

CREATE TABLE `Suspect` (
  `SuspectID` INTEGER PRIMARY KEY,
  `Name` VARCHAR,
  `DateOfBirth` DATE,
  `Address` VARCHAR,
  `CriminalRecord` VARCHAR,
  `Height` INT,
  `Weight` INT,
  `EyeColor` VARCHAR
);

CREATE TABLE `Case` (
  `CaseID` INTEGER PRIMARY KEY,
  `Description` VARCHAR,
  `DateOpened` DATE,
  `Status` VARCHAR,
  `Type` VARCHAR,
  `InvestigatingOfficerID` INT,
  `PriorityLevel` INT,
  `Location` VARCHAR,
  FOREIGN KEY (`InvestigatingOfficerID`) REFERENCES `PoliceOfficer` (`OfficerID`)
);

CREATE TABLE `Victim` (
  `VictimID` INTEGER PRIMARY KEY,
  `Name` VARCHAR,
  `ContactInformation` VARCHAR,
  `Statement` VARCHAR,
  `DateOfIncident` DATE,
  `Injuries` VARCHAR,
  `EmergencyContact` VARCHAR,
  `Gender` VARCHAR,
  `CaseID` INT,
  FOREIGN KEY (`CaseID`) REFERENCES `Case` (`CaseID`)
);

CREATE TABLE `Witness` (
  `WitnessID` INTEGER PRIMARY KEY,
  `Name` VARCHAR,
  `ContactInformation` VARCHAR,
  `Statement` VARCHAR,
  `RelationshipToCase` VARCHAR,
  `Occupation` VARCHAR,
  `DateOfInterview` DATE,
  `Address` VARCHAR
);

CREATE TABLE `Evidence` (
  `EvidenceID` INTEGER PRIMARY KEY,
  `Description` VARCHAR,
  `DateCollected` DATE,
  `Type` VARCHAR,
  `ChainOfCustody` VARCHAR,
  `StorageLocation` VARCHAR,
  `LabAnalysisResults` VARCHAR,
  `SeizedByOfficerID` INT,
  FOREIGN KEY (`SeizedByOfficerID`) REFERENCES `PoliceOfficer` (`OfficerID`)
);

CREATE TABLE `CrimeScene` (
  `SceneID` INTEGER PRIMARY KEY,
  `Location` VARCHAR,
  `Date` DATE,
  `Description` VARCHAR,
  `InvestigatingOfficerID` INT,
  `WeatherConditions` VARCHAR,
  `PhotosTaken` VARCHAR,
  `PreliminaryFindings` VARCHAR,
  `CaseID` INT,
  FOREIGN KEY (`InvestigatingOfficerID`) REFERENCES `PoliceOfficer` (`OfficerID`),
  FOREIGN KEY (`CaseID`) REFERENCES `Case` (`CaseID`)
);

CREATE TABLE `Vehicle` (
  `VehicleID` INTEGER PRIMARY KEY,
  `LicensePlate` VARCHAR,
  `Owner` VARCHAR,
  `Make` VARCHAR,
  `Model` VARCHAR,
  `Color` VARCHAR,
  `RegisteredAddress` VARCHAR,
  `VehicleType` VARCHAR,
  `SuspectID` INT,
  FOREIGN KEY (`SuspectID`) REFERENCES `Suspect` (`SuspectID`)
);

CREATE TABLE `ArrestRecord` (
  `ArrestRecordID` INTEGER PRIMARY KEY,
  `SuspectID` INT,
  `ArrestingOfficerID` INT,
  `DateTimeOfArrest` DATETIME,
  `ArrestLocation` VARCHAR,
  `Charges` VARCHAR,
  FOREIGN KEY (`SuspectID`) REFERENCES `Suspect` (`SuspectID`),
  FOREIGN KEY (`ArrestingOfficerID`) REFERENCES `PoliceOfficer` (`OfficerID`)
);

CREATE TABLE `PoliceDepartment` (
  `DepartmentID` INTEGER PRIMARY KEY,
  `Name` VARCHAR,
  `Location` VARCHAR,
  `ContactInformation` VARCHAR,
  `ChiefOfficerID` INT,
  `NumberOfOfficers` INT,
  `Budget` VARCHAR,
  `SpecialUnits` VARCHAR,
  FOREIGN KEY (`ChiefOfficerID`) REFERENCES `PoliceOfficer` (`OfficerID`)
);

CREATE TABLE `CaseWitness` (
  `CaseWitnessID` INTEGER PRIMARY KEY,
  `CaseID` INT,
  `WitnessID` INT,
  `DateOfInterview` DATE,
  `Statement` VARCHAR,
  FOREIGN KEY (`CaseID`) REFERENCES `Case` (`CaseID`),
  FOREIGN KEY (`WitnessID`) REFERENCES `Witness` (`WitnessID`)
);

CREATE TABLE `SuspectCase` (
  `SuspectCaseID` INTEGER PRIMARY KEY,
  `SuspectID` INT,
  `CaseID` INT,
  `RoleInCase` VARCHAR,
  FOREIGN KEY (`SuspectID`) REFERENCES `Suspect` (`SuspectID`),
  FOREIGN KEY (`CaseID`) REFERENCES `Case` (`CaseID`)
);

CREATE TABLE `OfficerArrestRecord` (
  `OfficerArrestRecordID` INTEGER PRIMARY KEY,
  `OfficerID` INT,
  `ArrestRecordID` INT,
  FOREIGN KEY (`OfficerID`) REFERENCES `PoliceOfficer` (`OfficerID`),
  FOREIGN KEY (`ArrestRecordID`) REFERENCES `ArrestRecord` (`ArrestRecordID`)
);
