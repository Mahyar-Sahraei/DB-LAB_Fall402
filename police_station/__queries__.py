
__SQL_QUERIES = {
    'query_1': "SELECT `Case`.CaseID, `Case`.Description, PoliceOfficer.Name AS InvestigatingOfficer \
                FROM `Case` \
                LEFT JOIN PoliceOfficer ON `Case`.InvestigatingOfficerID = PoliceOfficer.OfficerID;",
    'query_2': "SELECT AVG(Suspect.Height) AS AverageHeight \
                FROM Suspect \
                JOIN SuspectCase ON Suspect.SuspectID = SuspectCase.SuspectID \
                GROUP BY Suspect.SuspectID \
                HAVING COUNT(DISTINCT SuspectCase.CaseID) > 1;",
    'query_3': "SELECT PoliceOfficer.Name, COUNT(ArrestRecord.ArrestRecordID) AS TotalArrests \
                FROM PoliceOfficer \
                LEFT JOIN ArrestRecord ON PoliceOfficer.OfficerID = ArrestRecord.ArrestingOfficerID \
                GROUP BY PoliceOfficer.OfficerID \
                ORDER BY TotalArrests DESC;",
    'query_4': "SELECT `Case`.CaseID, `Case`.Description, `Case`.PriorityLevel, PoliceOfficer.Name AS InvestigatingOfficer \
                FROM `Case` \
                LEFT JOIN PoliceOfficer ON `Case`.InvestigatingOfficerID = PoliceOfficer.OfficerID \
                ORDER BY `Case`.PriorityLevel DESC \
                LIMIT 5;",
    'query_5': "SELECT `Case`.CaseID, Victim.Name AS VictimName, Witness.Name AS WitnessName \
                FROM `Case` \
                JOIN Victim ON `Case`.CaseID = Victim.CaseID \
                JOIN Witness ON `Case`.CaseID = Witness.CaseID \
                WHERE Victim.EmergencyContact = Witness.ContactInformation;",
    'query_6': "SELECT Suspect.Name AS SuspectName, ArrestRecord.DateTimeOfArrest, PoliceOfficer.Rank \
                FROM Suspect \
                JOIN ArrestRecord ON Suspect.SuspectID = ArrestRecord.SuspectID \
                JOIN PoliceOfficer ON ArrestRecord.ArrestingOfficerID = PoliceOfficer.OfficerID \
                WHERE Suspect.SuspectID IS NOT NULL \
                AND PoliceOfficer.Rank = (SELECT Rank FROM PoliceOfficer WHERE OfficerID = ArrestRecord.ArrestingOfficerID);",
    'query_7': "SELECT AVG(WitnessCount) AS AverageWitnessCount \
                FROM ( \
                    SELECT `Case`.CaseID, COUNT(Witness.WitnessID) AS WitnessCount \
                    FROM `Case` \
                    LEFT JOIN CaseWitness ON `Case`.CaseID = CaseWitness.CaseID \
                    LEFT JOIN Witness ON CaseWitness.WitnessID = Witness.WitnessID \
                    GROUP BY `Case`.CaseID \
                ) AS WitnessCounts;",
    'query_8': "SELECT `Case`.CaseID, Evidence.Description, Vehicle.RegisteredAddress \
                FROM `Case` \
                JOIN Evidence ON `Case`.CaseID = Evidence.CaseID \
                JOIN Vehicle ON `Case`.CaseID = Vehicle.CaseID \
                WHERE Evidence.StorageLocation = Vehicle.RegisteredAddress;",
    'query_9': "SELECT DISTINCT `Case`.CaseID, Witness.Occupation \
                FROM `Case` \
                JOIN CaseWitness ON `Case`.CaseID = CaseWitness.CaseID \
                JOIN Witness ON CaseWitness.WitnessID = Witness.WitnessID \
                WHERE Witness.Occupation IN ( \
                    SELECT Occupation \
                    FROM Witness \
                    GROUP BY Occupation \
                    HAVING COUNT(DISTINCT Witness.WitnessID) > 1 \
                );",
    'query_10': "SELECT * \
                 FROM PoliceOfficer \
                 LEFT JOIN ArrestRecord ON PoliceOfficer.OfficerID = ArrestRecord.ArrestingOfficerID \
                 WHERE ArrestRecord.ArrestRecordID IS NULL;"
}