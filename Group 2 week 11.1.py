import mysql.connector

# Prompt for credentials at runtime
user = input("Enter MySQL username: ")
password = input("Enter MySQL password: ")

conn = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password,
    database="Willson_Financial"
)
cursor = conn.cursor()

# Example query for Report 1
print("\n--- Report 1: Client Asset Summary ---")
cursor.execute("""
SELECT c.FirstName, c.LastName, c.ContactInfo, a.AssetType, a.AssetValue
FROM Client c
JOIN Asset a ON c.ClientID = a.ClientID
""")
for row in cursor.fetchall():
    print(row)

conn.close()
