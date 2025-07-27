# search_db.py

import mysql.connector
from mysql.connector import Error
from dataclasses import dataclass

def find_patient_by_id(conn, patient_id: int):
    """
    Finds and displays patient information by patient ID.
    """
    try:
        with conn.cursor() as cursor:
            sql = """
                SELECT patient_id, first_name, last_name, dob, gender, contact_number
                FROM patients
                WHERE patient_id = %s
            """
            cursor.execute(sql, (patient_id,))
            row = cursor.fetchone()

            if row:
                print("\n--- Patient Found ---")
                print(f"  ID: {row[0]}")
                print(f"  Name: {row[1]} {row[2]}")
                print(f"  Date of Birth: {row[3]}")
                print(f"  Gender: {row[4]}")
                print(f"  Contact: {row[5]}")
                print("---------------------")
            else:
                print(f"❌ Patient with ID {patient_id} not found.")
    except mysql.MySQLError as e:
        print(f"Search failed: {e}")

