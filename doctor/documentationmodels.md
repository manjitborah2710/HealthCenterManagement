# Database Design
The  tables were created in the Doctor App after a thorough analysis of the NITS Health Centre. The attributes of the tables are discussed too:

## IndividualRecord 
Here the individual records of the students, faculty and other staff is stored.
- **Primary Key** is person_id which scholar id for students and for others it is (to be added) 
- Category of the individuals whether he is student or faculty or staff 
- Name
- Hostel(in case of student)
- Nationality

## HealthCentreStaff
Here the details of the Health Centre Staff is stored. 
- **Primary Key** is staff id.
- staff name
- staff type
- staff address
- availability of the staff time period

## Prescription
Here the prescription is generated. 
- **Primary Key** is prescription_serial_no 
- Patient_id is Foreign Key imported from IndividualRecord
- Date_of_issue i.e. the current date
- Doctor_id is Foreign Key imported from HealthCentreStaff

## Medicine
Here the details of the medicine is added
- **Primary Key** is medicine_id
- Medicine name
- Manufacturing Company
- Quantity of Medicine
- Category of Medicine : a list of category is added

## MedicineIssue
Details of Medicine issued or not is stored here.
- **Primary Key** is auto-increment.
- prescription_serial_no is **Foreign Key** imported from Prescription
- Medicine_id is **Foreign Key** imported from Medicine
- Quantity of Medicine
- Issue_status
- Non_issue_reason

## EmpanelledFirm
Here the details of the firm from which Medicine is bought
- **Primary Key** is firm_id
- Name
- Email id
- Phone No.

## Stock
Here the details of stock purchased in requisition is updated
- **Primary Key** is batch_no
- Bill no of the bill
- Firm id is **Foreign Key** imported from EmpanelledFirm
- Bill date is date of the bill

## StockMedicine
There can be various batch in a requistion can have different expiry date so we have a different table for the stock medicine
- There is no **Primary Key**
- Batch_no is **Foreign Key** imported from Stock
- Medicine id is **Foreign Key** imported from Medicine
- Quantity of the medicine
- Medicine rate
- Expiry date

## Requisition
The requisition which is in process
- Requisition is the **Primark Key**
- Date of order
- Amount
- Date of approval
- Memo

## DoctorRequisitionProposal
The doctor can add the medicine and the quantity to the requisiton
- Requisiton id is the **Foreign Key** imported from Requisiton
- Doctor id is the **Foreign Key** imported from HealthCentreStaff
- Medicine id is the **Foreign Key** imported from Medicine
- Quantity entered by the doctor

## PatientRecord
The record of the patient
- Prescription serial no is **Foreign Key** imported from Prescription
- Doctor id is **Foreign Key** imported from HealthCentreStaff
- Patient id is **Foreign Key** imported from IndividualRecord
- Complaints
- Daignosis
- Test-result
- Follow up date
- isDependant is the patient dependant of the staff
- Test recommended

## FollowUpReport
The follow up report of the pateint 
- Patient id is the **Foreign Key** imported from PatientRecord
- Follow up date
- Present , did the patient come for follow up ?
- Cured , is the patient cured ?
- Further comments

## RecommendedTest
The recommended test
- Patient id is the **Foreign Key** imported from PatientRecord
- Doctor id is the **Foreign Key** imported from HealthCentreStaff
- Test-name

## Composition
The composition of the medicine
- Medicine is the **Foreign Key** imported from Medicine
- Primary ingredient

## Dependant
The dependant of the staff
- Person id is the **Foreign Key** of the IndividualRecord
- Name
- Date of birth
- relation with person

## HealthCentreStaffContact
The details of the Health Centre Staff
- Staff id is the **Foreign Key** imported from the HealthCentreStaff
- Phone no
- Email id

## DisposedMedicine
The medicine which were disposed
- Medicine id is the **Foreign Key** imported from Medicine
- Batch no is the **foreign Key** imported from Requisition
- Reason of dispose
- Quantity
- Date

## Requisition Medicine
In the DoctorRequisitionProposal the doctor may need to add various medicine so we need this table
- Requisition id is **Foreign Key** imported from Requisiton
- Medicine id is **Foreign Key** imported from Medicine
- Quantity_Requested
- Quantity_Recievved
 