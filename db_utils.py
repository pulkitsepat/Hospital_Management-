# db_utils.py

import mysql.connector
from mysql.connector import Error

# Database credentials
DB_HOST = "localhost"
DB_USER = "hospital_user"
DB_PASS = ""  # Empty string means no password
DB_NAME = "hospital_db_py"

def db_connect():
    """Establishes a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password="",
            database=DB_NAME
        )
        print("Database connection successful!")
        return conn
    except Error as e:
        print(f"Database connection failed: {e}")
        raise SystemExit(1)

