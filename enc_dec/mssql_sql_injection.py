import pyodbc

# --- Connection settings ---
# Adjust SERVER and DRIVER for your environment
conn = pyodbc.connect(
        r"DRIVER={ODBC Driver 17 for SQL Server};" 
        r"SERVER= MS-MDU-073\SQLEXPRESS;"          
        r"DATABASE=TestDB;"
        r"UID=sa2026;"                     
        r"PWD=2026;"        
        r"TrustServerCertificate=yes;" 
    )

cursor = conn.cursor()

# --- Vulnerable login function ---
def vulnerable_login(username, password):
    #  Vulnerable: Direct string concatenation
    query = f"SELECT * FROM Users WHERE username = '{username}' AND password = '{password}'"
    print(f"[DEBUG] Executing query: {query}")
    cursor.execute(query)
    return cursor.fetchall()

# --- Secure login function ---
def secure_login(username, password):
    #  Safe: Parameterized query
    query = "SELECT * FROM Users WHERE username = ? AND password = ?"
    print(f"[DEBUG] Executing secure query with parameters")
    cursor.execute(query, (username, password))
    return cursor.fetchall()

# --- Normal login ---
print("Normal login attempt:")
print(vulnerable_login("alice", "alicepass"))  # Works normally

# --- SQL Injection attack ---
print("\nSQL Injection attack attempt (vulnerable):")
malicious_username = "admin' --"
malicious_password = "anything"
print(vulnerable_login(malicious_username, malicious_password))  # Bypasses password

# --- Secure version blocks it ---
print("\nSQL Injection attempt (secure):")
print(secure_login(malicious_username, malicious_password))  # Returns empty list
