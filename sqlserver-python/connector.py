from dotenv import load_dotenv
import pyodbc,os


def connect_to_mssql(server, database, username, password, driver="{ODBC Driver 17 for SQL Server}"):
    """
    Connect to a Microsoft SQL Server database using pyodbc.
    
    :param server: SQL Server hostname or IP (e.g., 'localhost' or '192.168.1.10')
    :param database: Database name
    :param username: SQL Server username
    :param password: SQL Server password
    :param driver: ODBC driver name (default: ODBC Driver 17 for SQL Server)
    :return: Connection object or None if failed
    """
    try:
        # Build connection string
        conn_str = (
            f"DRIVER={driver};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
            "TrustServerCertificate=yes;"
        )

        # Connect to SQL Server
        conn = pyodbc.connect(conn_str)
        print(" Connection successful!")
        return conn

    except pyodbc.Error as e:
        print(" Connection failed.")
        print("Error:", e)
        return None


if __name__ == "__main__":
    
    load_dotenv()
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    username = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    
    conn = connect_to_mssql(server, database, username, password)

    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT @@VERSION;")  
            row = cursor.fetchone()
            print("SQL Server Version:", row[0])
        except pyodbc.Error as e:
            print("Query failed:", e)
        finally:
            conn.close()
