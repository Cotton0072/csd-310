import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get credentials securely
user = os.getenv("USER")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
database = os.getenv("DATABASE")

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )

    print("✅ Connection successful!")

    # Create a cursor to run SQL commands
    cursor = conn.cursor()

    # Show tables
    cursor.execute("SHOW TABLES;")
    print("Tables:")
    for (table_name,) in cursor.fetchall():
        print(f"- {table_name}")

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
