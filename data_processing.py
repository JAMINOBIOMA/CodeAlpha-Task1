import mysql.connector
import pandas as pd

# Connect to MySQL
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Exoteric7465@",
        database="secure_db"
    )

# Function to check for redundant data
def is_duplicate(data_value, connection):
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM data_records WHERE data_value = %s", (data_value,))
    count = cursor.fetchone()[0]
    return count > 0

# Function to insert new data if not redundant
def insert_data(data_value):
    connection = connect_to_db()
    cursor = connection.cursor()

    if is_duplicate(data_value, connection):
        print(f"Duplicate found: {data_value} - Skipping insertion.")
    else:
        cursor.execute("INSERT INTO data_records (data_value) VALUES (%s)", (data_value,))
        connection.commit()
        print(f"Data inserted: {data_value}")

    cursor.close()
    connection.close()

# Example data
test_data = ["user123", "test456", "user123", "data789"]

for data in test_data:
    insert_data(data)
