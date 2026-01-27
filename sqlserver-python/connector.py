from dotenv import load_dotenv
import pyodbc,os


def connect_to_mssql(server, database, username, password, driver="{ODBC Driver 17 for SQL Server}"):

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

        conn = pyodbc.connect(conn_str)
        print(" Connection successful!")
        return conn

    except pyodbc.Error as e:
        print(" Connection failed.")
        print("Error:", e)
        return None


def fetch_table_data(conn, table_name):
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM {table_name};"  
        cursor.execute(query)

        rows = cursor.fetchall()

        columns = [column[0] for column in cursor.description]

        print(f"\n Data from table '{table_name}':")
        print(columns)  
        for row in rows:
            print(row)  

    except pyodbc.Error as e:
        print(" Failed to fetch data:", e)


if __name__ == "__main__":

    load_dotenv()
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    username = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    
    conn = connect_to_mssql(server, database, username, password)

    # if conn:
    #     try:
    #         cursor = conn.cursor()
    #         cursor.execute("SELECT @@VERSION;")  
    #         row = cursor.fetchone()
    #         print("SQL Server Version:", row[0])
    #         a = conn.execute("SELECT * FROM employee")
    #         print(a)
    #     except pyodbc.Error as e:
    #         print("Query failed:", e)
    #     finally:
    #         conn.close()


    if conn:
        fetch_table_data(conn, "task")  # Change "Employees" to your table name
        conn.close()