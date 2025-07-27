# patient_db.py

from hospital import Patient
import mysql.connector
from mysql.connector import Error
from dataclasses import dataclass

def add_patient(conn, patient: Patient):
    """
    Adds a new patient to the database.
    WARNING: In production, use parameterized queries to prevent SQL injection!
    """
    try:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO patients (first_name, last_name, dob, gender, contact_number)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                patient.first_name,
                patient.last_name,
                patient.dob,
                patient.gender,
                patient.contact_number
            ))
            conn.commit()
            print(f"New patient added successfully with ID: {cursor.lastrowid}")
    except mysql.connector.MySQLError as e:
        print(f"INSERT failed: {e}")

