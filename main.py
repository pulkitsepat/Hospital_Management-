# main.py

from hospital import Patient, Appointment
from db_utils import db_connect
from patient_db import add_patient
from appointment_db import schedule_appointment
from search_db import find_patient_by_id

def show_menu():
    print("\n--- Hospital Management System ---")
    print("1. Add New Patient")
    print("2. Schedule Appointment")
    print("3. Find Patient by ID")
    print("4. Exit")
    return input("Enter your choice: ")

def main():
    conn = db_connect()

    while True:
        choice = show_menu()

        if choice == '1':
            print("Enter Patient Details:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            dob = input("DOB (YYYY-MM-DD): ")
            gender = input("Gender: ")
            contact_number = input("Contact Number: ")
            new_patient = Patient(
                id=0,
                first_name=first_name,
                last_name=last_name,
                dob=dob,
                gender=gender,
                contact_number=contact_number
            )
            add_patient(conn, new_patient)

        elif choice == '2':
            print("Enter Appointment Details:")
            try:
                patient_id = int(input("Patient ID: "))
            except ValueError:
                print("❌ Invalid ID. Must be an integer.")
                continue

            doctor_name = input("Doctor Name: ")
            appointment_date = input("Appointment Date (YYYY-MM-DD HH:MM:SS): ")
            reason = input("Reason for Appointment: ")

            new_appointment = Appointment(
                id=0,
                patient_id=patient_id,
                doctor_name=doctor_name,
                appointment_date=appointment_date,
                reason=reason
            )
            schedule_appointment(conn, new_appointment)

        elif choice == '3':
            try:
                patient_id = int(input("Enter Patient ID: "))
                find_patient_by_id(conn, patient_id)
            except ValueError:
                print("❌ Invalid input. Please enter a valid integer.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()

