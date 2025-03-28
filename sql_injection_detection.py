import re
import mysql.connector

# Connect to MySQL
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Exoteric7465@",
        database="secure_db"
    )

# Detect SQL Injection Patterns
def detect_sql_injection(query):
    injection_patterns = [
        r"(\bor\b|\band\b).*(=|like).*('|\")",  # OR/AND with equality check
        r"(union.*select.*)",  # UNION-based attacks
        r"(--|#|;)",  # Comment-based attacks
        r"(drop\s+table|delete\s+from|update\s+.*set)",  # Data-altering queries
        r"('\s*or\s*1\s*=\s*1\s*--)",  # Always-true condition
    ]
    
    for pattern in injection_patterns:
        if re.search(pattern, query, re.IGNORECASE):
            return True  # SQL Injection detected
    return False  # Query is safe

# Secure Query Execution
def execute_query(query, values=None):
    if detect_sql_injection(query):
        print("🚨 SQL Injection detected! Query blocked.")
        return

    connection = connect_to_db()
    cursor = connection.cursor()

    if values:
        cursor.execute(query, values)
    else:
        cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()
    print("✅ Query executed successfully.")

# Test Cases
safe_query = "INSERT INTO data_records (data_value) VALUES (%s)"
malicious_query = "SELECT * FROM users WHERE username = 'admin' OR '1'='1' --'"

execute_query(safe_query, ("safe_data",))  # Allowed
execute_query(malicious_query)  # Blocked
