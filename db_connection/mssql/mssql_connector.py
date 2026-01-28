"""
Docstring for db_connection.mssql.mssql_connector
"""
import pyodbc

def main():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};" 
        "SERVER= MS-MDU-073\SQLEXPRESS;"          
        "DATABASE=kesavan_db;"
        "UID=sa2026;"                     
        "PWD=2026;"        
        "TrustServerCertificate=yes;" 
    )

    cursor = conn.cursor()

    cursor.execute("""
        IF OBJECT_ID('dbo.Products', 'U') IS NOT NULL
            DROP TABLE dbo.Products;
        CREATE TABLE dbo.Products (
            id INT IDENTITY(1,1) PRIMARY KEY,
            name NVARCHAR(100) NOT NULL,
            price DECIMAL(10, 2) NOT NULL
        );
    """)

    products = [
        ("Laptop", 1200.50),
        ("Mouse", 25.75),
        ("Keyboard", 45.00)
    ]
    cursor.executemany("INSERT INTO dbo.Products (name, price) VALUES (?, ?)", products)
    conn.commit()

    cursor.execute("UPDATE dbo.Products SET price = ? WHERE name = ?", (1300.00, "Laptop"))
    conn.commit()

    cursor.execute("SELECT * FROM dbo.Products")
    for row in cursor.fetchall():
        print(row) 

    cursor.execute("DELETE FROM dbo.Products WHERE name = ?", ("Mouse",))
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM dbo.Products")
    count = cursor.fetchone()[0]
    print(f"Remaining products: {count}")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
