from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from police_station.auth import login_required
from police_station.db import get_db
from police_station.__queries__ import __SQL_QUERIES

blue_print = Blueprint('main', __name__)

@blue_print.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        db = get_db()
        query_section = request.form['query_section']
        sql_query = __SQL_QUERIES[query_section]

        results = db.execute(sql_query).fetchall()
        return render_template('main/index.html', query_results=results)

    return render_template('main/index.html', query_results=None)


@blue_print.route('/add_record', methods=['GET', 'POST'])
@login_required
def add_record():
    if request.method == "POST":
        table_section = request.form["table_section"]
        db = get_db()

        if table_section == "table_1":
            witness_name = request.form["witness_name"]
            witness_contact = request.form["witness_contact"]
            witness_statement = request.form["witness_statement"]
            relationship_to_case = request.form['relationship_to_case']
            witness_occupation = request.form['witness_occupation']
            interview_date = request.form['interview_date']
            witness_address = request.form['witness_address']

            db.execute('''
                    INSERT INTO Witness
                    (WitnessId, Name, ContactInformation, Statement, RelationshipToCase, Occupation, DateOfInterview, Address)
                    VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)
                ''', (witness_name, witness_contact, witness_statement, relationship_to_case, witness_occupation, interview_date, witness_address))
            db.commit()

        elif table_section == "table_2":
            case_description = request.form['case_description']
            date_opened = request.form['date_opened']
            case_status = request.form['case_status']
            case_type = request.form['case_type']
            investigating_officer_id = request.form['investigating_officer']
            priority_level = request.form['priority_level']
            case_location = request.form['case_location']

            db.execute('''
                    INSERT INTO `Case`
                    (CaseId, Description, DateOpened, Status, Type, InvestigatingOfficerId, PriorityLevel, Location)
                    VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)
                ''', (case_description, date_opened, case_status, case_type, investigating_officer_id, priority_level, case_location))
            db.commit()

        elif table_section == "table_3":
            suspect_name = request.form["suspect_name"]
            date_of_birth = request.form["date_of_birth"]
            suspect_address = request.form["suspect_address"]
            criminal_record = request.form["criminal_record"]
            height = request.form["height"]
            weight = request.form["weight"]
            eye_color = request.form["eye_color"]

            db.execute('''
                INSERT INTO Suspect
                (SuspectId, Name, DateOfBirth, Address, CriminalRecord, Height, Weight, EyeColor)
                VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)
            ''', (suspect_name, date_of_birth, suspect_address, criminal_record, height, weight, eye_color))
            db.commit()

        elif table_section == "table_4":
            victim_name = request.form["victim_name"]
            contact_information = request.form["victim_contact"]
            victim_statement = request.form["victim_statement"]
            date_of_incident = request.form["date_of_incident"]
            injuries = request.form["injuries"]
            emergency_contact = request.form["emergency_contact"]
            gender = request.form["gender"]
            case_id = request.form["case_id"]

            db.execute('''
                INSERT INTO Victim
                (VictimId, Name, ContactInformation, Statement, DateOfIncident, Injuries, EmergencyContact, Gender, CaseId)
                VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (victim_name, contact_information, victim_statement, date_of_incident, injuries, emergency_contact, gender, case_id))
            db.commit()

        elif table_section == "table_5":
            evidence_description = request.form["evidence_description"]
            date_collected = request.form["date_collected"]
            evidence_type = request.form["evidence_type"]
            chain_of_custody = request.form["chain_of_custody"]
            storage_location = request.form["storage_location"]
            lab_analysis_results = request.form["lab_analysis_results"]
            seized_by_officer_id = request.form["seized_by_officer"]

            db.execute('''
                INSERT INTO Evidence
                (EvidenceId, Description, DateCollected, Type, ChainOfCustody, StorageLocation, LabAnalysisResults, SeizedByOfficerId)
                VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)
            ''', (evidence_description, date_collected, evidence_type, chain_of_custody, storage_location, lab_analysis_results, seized_by_officer_id))
            db.commit()

        elif table_section == "table_6":
            license_plate = request.form["license_plate"]
            owner = request.form["vehicle_owner"]
            make = request.form["vehicle_make"]
            model = request.form["vehicle_model"]
            color = request.form["vehicle_color"]
            registered_address = request.form["registered_address"]
            vehicle_type = request.form["vehicle_type"]
            suspect_id = request.form["suspect_id"]

            db.execute('''
                INSERT INTO Vehicle
                (VehicleId, LicensePlate, Owner, Make, Model, Color, RegisteredAddress, VehicleType, SuspectId)
                VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (license_plate, owner, make, model, color, registered_address, vehicle_type, suspect_id))
            db.commit()

        elif table_section == "table_7":
            department_name = request.form["department_name"]
            department_location = request.form["department_location"]
            department_contact = request.form["department_contact"]
            chief_officer_id = request.form["chief_officer_id"]
            number_of_officers = request.form["number_of_officers"]
            department_budget = request.form["department_budget"]
            special_units = request.form["special_units"]

            db.execute('''
                INSERT INTO PoliceDepartment
                (DepartmentId, Name, Location, ContactInformation, ChiefOfficerId, NumberOfOfficers, Budget, SpecialUnits)
                VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)
            ''', (department_name, department_location, department_contact, chief_officer_id, number_of_officers, department_budget, special_units))
            db.commit()

        elif table_section == "table_8":
            suspect_id_arrest = request.form["suspect_id_arrest"]
            arresting_officer = request.form["arresting_officer"]
            datetime_of_arrest = request.form["datetime_of_arrest"]
            arrest_location = request.form["arrest_location"]
            charges = request.form["charges"]

            db.execute('''
                INSERT INTO ArrestRecord
                (ArrestRecordId, SuspectId, ArrestingOfficerId, DatetimeOfArrest, ArrestLocation, Charges)
                VALUES (NULL, ?, ?, ?, ?, ?)
            ''', (suspect_id_arrest, arresting_officer, datetime_of_arrest, arrest_location, charges))
            db.commit()

        elif table_section == "table_9":
            officer_name = request.form["officer_name"]
            badge_number = request.form["badge_number"]
            rank = request.form["rank"]
            shift = request.form["shift"]
            date_of_joining = request.form["date_of_joining"]
            contact_number = request.form["contact_number"]
            officer_address = request.form["officer_address"]

            db.execute('''
                INSERT INTO PoliceOfficer
                (OfficerId, Name, BadgeNumber, Rank, Shift, DateOfJoining, ContactNumber, Address)
                VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)
            ''', (officer_name, badge_number, rank, shift, date_of_joining, contact_number, officer_address))
            db.commit()

        elif table_section == "table_10":
            officer_id_arrest_record = request.form["officer_id_arrest_record"]
            arrest_record_id = request.form["arrest_record_id"]

            db.execute('''
                INSERT INTO OfficerArrestRecord
                (OfficerArrestRecordId, OfficerId, ArrestRecordId)
                VALUES (NULL, ?, ?)
            ''', (officer_id_arrest_record, arrest_record_id))
            db.commit()

        elif table_section == "table_11":
            suspect_id_case = request.form["suspect_id_case"]
            case_id_case = request.form["case_id_case"]
            role_in_case = request.form["role_in_case"]

            db.execute('''
                INSERT INTO SuspectCase
                (SuspectCaseId, SuspectId, CaseId, RoleInCase)
                VALUES (NULL, ?, ?, ?)
            ''', (suspect_id_case, case_id_case, role_in_case))
            db.commit()

        elif table_section == "table_12":
            case_id_witness = request.form["case_id_witness"]
            witness_id = request.form["witness_id"]
            interview_date_witness = request.form["interview_date_witness"]
            statement_witness = request.form["statement_witness"]

            db.execute('''
                INSERT INTO CaseWitness
                (CaseWitnessId, CaseId, WitnessId, DateOfInterview, Statement)
                VALUES (NULL, ?, ?, ?, ?)
            ''', (case_id_witness, witness_id, interview_date_witness, statement_witness))
            db.commit()

        elif table_section == "table_13":
            location_crime_scene = request.form["location_crime_scene"]
            date_crime_scene = request.form["date_crime_scene"]
            description_crime_scene = request.form["description_crime_scene"]
            investigating_officer_crime_scene = request.form["investigating_officer_crime_scene"]
            weather_conditions = request.form["weather_conditions"]
            photos_taken = request.form["photos_taken"]
            preliminary_findings = request.form["preliminary_findings"]
            case_id_crime_scene = request.form["case_id_crime_scene"]

            db.execute('''
                INSERT INTO CrimeScene
                (SceneId, Location, Date, Description, InvestigatingOfficerId, WeatherConditions, PhotosTaken, PreliminaryFindings, CaseId)
                VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (location_crime_scene, date_crime_scene, description_crime_scene, investigating_officer_crime_scene, weather_conditions, photos_taken, preliminary_findings, case_id_crime_scene))
            db.commit()
        else:
            flash(message="No such table!", category="error")
            return redirect(url_for("main.index"))

        flash(message="Record saved successfully!", category="message")
        return redirect(url_for("main.index"))
    else:
        return render_template("main/add_record.html")


@blue_print.route('/inspect', methods=['GET', 'POST'])
@login_required
def inspect():
    if request.method == 'POST':
        db = get_db()
        table = request.form["table_section"]
        results = db.execute(f'''
            SELECT * FROM `{table}`
        ''').fetchall()
        return render_template('main/inspect.html', query_results=results)
    return render_template('main/inspect.html', query_results=None)