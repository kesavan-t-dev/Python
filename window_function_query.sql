use kesavan_db

CREATE TABLE Sales (
            EmployeeID INT,
            EmployeeName NVARCHAR(50),
            Region NVARCHAR(20),
            SaleAmount DECIMAL(10,2),
            SaleDate DATE
        );

INSERT INTO Sales VALUES
    (1, 'Alice', 'East', 5000, '2024-01-10'),
    (2, 'Bob', 'East', 7000, '2024-01-12'),
    (3, 'Charlie', 'West', 6000, '2024-01-15'),
    (4, 'Alice', 'East', 8000, '2024-02-05'),
    (5, 'Bob', 'East', 4000, '2024-02-07'),
    (6, 'Charlie', 'West', 9000, '2024-02-10');

SELECT 
    EmployeeName,
    SaleDate,
    SaleAmount,
    SUM(SaleAmount) OVER (PARTITION BY EmployeeName ORDER BY SaleDate) AS RunningTotal
FROM Sales;

-- Example 2: Ranking employees by sales within their region
SELECT 
    EmployeeName,
    Region,
    SaleAmount,
    RANK() OVER (PARTITION BY Region ORDER BY SaleAmount DESC) AS SalesRank
FROM Sales;

-- Example 3: Average sales per region without collapsing rows
SELECT 
    EmployeeName,
    Region,
    SaleAmount,
    AVG(SaleAmount) OVER (PARTITION BY Region) AS AvgSaleInRegion
FROM Sales;
