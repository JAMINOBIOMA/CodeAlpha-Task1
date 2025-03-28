import mysql.connector
from mysql.connector import Error

# Connect to MySQL
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="Exoteric7465@",  
            database="secure_db"
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Run the function to test connection
db_connection = connect_to_db()
