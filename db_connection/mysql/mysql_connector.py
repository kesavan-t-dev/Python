"""
Docstring for db_connection.mysql.mysql_connector
"""
import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",  
        database="test",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor  
    )
    print("Connection successful!")

    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS products;")
        cursor.execute("""
            CREATE TABLE products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL(10, 2) NOT NULL
            );
        """)

        products = [
            ("Laptop", 1200.50),
            ("Mouse", 25.75),
            ("Keyboard", 45.00)
        ]
        cursor.executemany(
            "INSERT INTO products (name, price) VALUES (%s, %s)",
            products
        )

        cursor.execute(
            "UPDATE products SET price = %s WHERE name = %s",
            (1300.00, "Laptop")
        )

        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

except pymysql.MySQLError as e:
    print(f"MySQL Error: {e}")

finally:
    if connection.open:
        print(" MySQL connection closed.")
