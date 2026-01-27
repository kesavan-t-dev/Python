"""
Docstring for db_connection.mysql.mysql_connector
"""
import pymysql

try:
    # Connect to MySQL
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",  # 'passwd' in MySQLdb is 'password' in PyMySQL
        database="test",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor  # Return rows as dictionaries
    )
    print("Connection successful!")

    with connection.cursor() as cursor:
        # Drop table if exists
        cursor.execute("DROP TABLE IF EXISTS products;")

        # Create table
        cursor.execute("""
            CREATE TABLE products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL(10, 2) NOT NULL
            );
        """)
        connection.commit()

        # Insert multiple rows
        products = [
            ("Laptop", 1200.50),
            ("Mouse", 25.75),
            ("Keyboard", 45.00)
        ]
        cursor.executemany(
            "INSERT INTO products (name, price) VALUES (%s, %s)",
            products
        )
        connection.commit()

        # Update a row
        cursor.execute(
            "UPDATE products SET price = %s WHERE name = %s",
            (1300.00, "Laptop")
        )
        connection.commit()

        # Fetch all rows
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

except pymysql.MySQLError as e:
    print(f"MySQL Error: {e}")

finally:
    if 'connection' in locals() and connection.open:
        connection.close()
        print(" MySQL connection closed.")
