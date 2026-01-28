"""
Docstring for db_connection.postgres.connector
"""
import pg8000

try:
    connection = pg8000.connect(
        user="postgres",
        password="root",
        host="localhost",
        port=5433,
        database="postgres"
    )
    print("Connection successful!")

    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS products;
        CREATE TABLE products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price NUMERIC(10, 2) NOT NULL
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
    for row in cursor.fetchall():
        print(row)

    cursor.close()


except Exception as e:
    print("An error occurred:", e)
finally:
    connection.close()
    print("Postgres connection closed!")