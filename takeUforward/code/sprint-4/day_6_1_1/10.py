# Q10. Patient Medical Record with Access Audit (Practice - Encapsulation)
#
# Task:
# Design a `MedicalRecord` class to manage sensitive clinical data.
# Clinical notes must only be accessed by authorized roles, and every single view or modification
# must generate an immutable audit log entry.
#
# Attributes:
# - patient_id (str) : Patient identifier (public).
# - patient_name (str) : Patient full name (public).
# - __blood_group (str) : Patient blood group (private, immutable).
# - __diagnoses (list[str]) : Clinical diagnosis list (private).
# - __access_log (list[str]) : System audit trail (private).
#
# Methods:
# - __init__(self, patient_id: str, patient_name: str, blood_group: str):
#     Initializes patient record with immutable blood group.
# - add_diagnosis(self, doctor_id: str, diagnosis_text: str):
#     Appends diagnosis to __diagnoses and appends audit entry: "ADDED: Diagnosis by Dr. {doctor_id}".
# - view_record(self, accessor_id: str, role: str) -> dict | None:
#     If role.upper() in ["DOCTOR", "PATIENT"]:
#         Appends audit "READ: Accessed by {accessor_id} ({role})"
#         Returns dict with "blood_group" and a copy of "diagnoses".
#     Otherwise:
#         Appends audit "UNAUTHORIZED: Attempted by {accessor_id} ({role})"
#         Prints "Access Denied: Unauthorized role."
#         Returns None.
# - get_audit_trail(self, admin_token: str) -> list[str]:
#     If admin_token == "MED_ADMIN_SECURE", returns a copy of __access_log.
#     Otherwise prints "Unauthorized audit access." and returns [].
#
# Example 1:
# Input:
# record = MedicalRecord("PT-901", "Emma Watson", "O+")
# record.add_diagnosis("DR-44", "Type 2 Diabetes")
# record.view_record("INSURANCE-01", "INSURANCE_AGENT")  # Unauthorized role
# data = record.view_record("DR-44", "DOCTOR")           # Authorized role
# print("Patient Data:", data)
# print("Audit Log:", record.get_audit_trail("MED_ADMIN_SECURE"))
# Output:
# Access Denied: Unauthorized role.
# Patient Data: {'blood_group': 'O+', 'diagnoses': ['Type 2 Diabetes']}
# Audit Log: ['ADDED: Diagnosis by Dr. DR-44', 'UNAUTHORIZED: Attempted by INSURANCE-01 (INSURANCE_AGENT)', 'READ: Accessed by DR-44 (DOCTOR)']
#
# Example 2:
# Input:
# record = MedicalRecord("PT-902", "Liam Neeson", "A-")
# print("Audit without token:", record.get_audit_trail("wrong_token"))
# Output:
# Unauthorized audit access.
# Audit without token: []
#
# Example 3 (Edge Case):
# Input:
# record = MedicalRecord("PT-903", "Sophia", "B+")
# patient_view = record.view_record("PT-903", "PATIENT")  # Patient viewing own record
# print("Empty Diagnoses:", patient_view["diagnoses"])
# Output:
# Empty Diagnoses: []
#
# Think About:
# - Direct public attribute access would bypass the audit logger completely.
# - Encapsulation ensures compliance by enforcing that every read/write generates an audit trail.
# - Returning copies of lists prevents caller tampering with internal history.
# - Time Complexity: O(1) per read/write; O(D + L) for exporting records/logs.
# - Space Complexity: O(D + L) where D is diagnoses and L is logs.

# Write your MedicalRecord class below:

class MedicalRecord:
    def __init__(self, patient_id: str, patient_name: str, blood_group: str):
        # Write your code here
        pass

    def add_diagnosis(self, doctor_id: str, diagnosis_text: str):
        # Write your code here
        pass

    def view_record(self, accessor_id: str, role: str) -> dict:
        # Write your code here
        pass

    def get_audit_trail(self, admin_token: str) -> list:
        # Write your code here
        pass
