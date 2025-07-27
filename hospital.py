# hospital.py

import mysql.connector
from mysql.connector import Error
from dataclasses import dataclass
# --- Data Classes ---
# Matches the 'patients' table schema
@dataclass
class Patient:
    id: int
    first_name: str
    last_name: str
    dob: str  # YYYY-MM-DD
    gender: str
    contact_number: str

# Matches the 'appointments' table schema
@dataclass
class Appointment:
    id: int
    patient_id: int
    doctor_name: str
    appointment_date: str  # YYYY-MM-DD HH:MI:SS
    reason: str

# --- Function Prototypes (Stubs) ---

# From db_utils.py
def db_connect():
    """Establish connection to the MySQL database."""
    pass

# From patient_db.py
def add_patient(conn, patient: Patient):
    """Add a new patient to the database."""
    pass

# From appointment_db.py
def schedule_appointment(conn, appointment: Appointment):
    """Schedule a new appointment for a patient."""
    pass

# From search_db.py
def find_patient_by_id(conn, patient_id: int):
    """Find a patient by ID and return their record."""
    pass

