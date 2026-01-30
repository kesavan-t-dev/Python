import pyodbc

def main():
    conn = pyodbc.connect(
        r"DRIVER={ODBC Driver 17 for SQL Server};" 
        r"SERVER= MS-MDU-073\SQLEXPRESS;"          
        r"DATABASE=kesavan_db;"
        r"UID=sa2026;"                     
        r"PWD=2026;"        
        r"TrustServerCertificate=yes;" 
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE Sale (
            EmployeeID INT,
            EmployeeName NVARCHAR(50),
            Region NVARCHAR(20),
            SaleAmount DECIMAL(10,2),
            SaleDate DATE
        );
    """)

    cursor.execute("""
        INSERT INTO Sale VALUES
            (1, 'Alice', 'East', 5000, '2024-01-10'),
            (2, 'Bob', 'East', 7000, '2024-01-12'),
            (3, 'Charlie', 'West', 6000, '2024-01-15'),
            (4, 'Alice', 'East', 8000, '2024-02-05'),
            (5, 'Bob', 'East', 4000, '2024-02-07'),
            (6, 'Charlie', 'West', 9000, '2024-02-10');
    """)


    cursor.execute("""
        SELECT 
            EmployeeName,
            SaleDate,
            SaleAmount,
            SUM(SaleAmount) OVER (PARTITION BY EmployeeName ORDER BY SaleDate) AS RunningTotal
        FROM Sale;
    """)
    
    for row in cursor.fetchall():
        print(row) 


    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()