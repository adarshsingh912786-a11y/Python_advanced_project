import sqlite3

db_name = "stock_inventory.db"

def get_connection():
    return sqlite3.connect(db_name)

def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT UNIQUE NOT NULL,
                   quantity INTEGER NOT NULL CHECK(quantity >= 0),
                   price REAL NOT NULL CHECK(price >= 0),
                   low_stock_threshold INTEGER NOT NULL CHECK(low_stock_threshold >= 0),
                   created_at TEXT DEFAULT CURRENT_TIMESTAMP
                   )
""")
    
    conn.commit()
    conn.close()

def add_product(name, quantity, price, low_stock_threshold):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO inventory (name, quantity, price, low_stock_threshold)
                   VALUES (?, ?, ?, ?)
""",(name, quantity, price, low_stock_threshold))
    
    conn.commit()
    conn.close()

def get_product_by_id(product_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM inventory WHERE id = ?",(product_id, ))

    row = cursor.fetchone()
    conn.close()
    return row

def get_all_products():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM inventory")

    row = cursor.fetchall()
    conn.close()
    return row

def update_product_quantity(id, new_quantity):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE inventory SET quantity = ? WHERE id = ?", (new_quantity, id))

    conn.commit()
    conn.close()

def delete_product(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM inventory WHERE id = ?", (id, ))

    conn.commit()
    conn.close()