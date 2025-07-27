# appointment_db.py

from hospital import Appointment
import mysql.connector
from mysql.connector import Error
from dataclasses import dataclass

def schedule_appointment(conn, appointment: Appointment):
    """
    Schedules a new appointment for a patient.
    Uses a parameterized query to prevent SQL injection.
    """
    try:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO appointments (patient_id, doctor_name, appointment_date, reason)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (
                appointment.patient_id,
                appointment.doctor_name,
                appointment.appointment_date,
                appointment.reason
            ))
            conn.commit()
            print("✅ Appointment scheduled successfully!")
    except mysql.connector.MySQLError as e:
        print(f"Appointment scheduling failed: {e}")

