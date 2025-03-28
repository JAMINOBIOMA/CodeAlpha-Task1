import pandas as pd
import mysql.connector

# Connect to MySQL
def fetch_data():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Exoteric7465@",
        database="secure_db"
    )
    query = "SELECT * FROM data_records"
    df = pd.read_sql(query, connection)
    connection.close()
    return df

# Load and classify data
df = fetch_data()
df["is_redundant"] = df.duplicated(subset=["data_value"])

print(df)
