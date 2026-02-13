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
                   quantity INTEGER NOT NULL,
                   price REAL NOT NULL,
                   low_stock_threshold INTEGER NOT NULL,
                   created_at TEXT 
                   )
""")
    
    conn.commit()
    conn.close()

def add_product(name, quantity, price, low_stock_threshold, created_at):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO inventory (name, quantity, price, low_stock_threshold, created_at)
                   VALUES (?, ?, ?, ?, ?)
""",(name, quantity, price, low_stock_threshold, created_at))
    
    conn.commit()
    conn.close()