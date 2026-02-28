import sqlite3

file_name = "client_database.db"

def get_connect():
    conn =  sqlite3.connect(file_name)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def create_table():

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   phone_no TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE,
                   status TEXT NOT NULL CHECK(status IN("lead", "contacted", "converted", "lost")),
                   created_at TEXT DEFAULT CURRENT_TIMESTAMP
                   )
""")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interactions (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   client_id INTEGER NOT NULL,
                   note TEXT NOT NULL,
                   interaction_type TEXT NOT NULL CHECK(interaction_type IN("call", "email", "meeting")),
                   created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                   FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
                   )
""")
    
    conn.commit()
    conn.close()

def add_client(name, phone, email):
    
    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO clients (name, phone_no, email, status) VALUES (?, ?, ?, ?)    
""", (name, phone, email, "lead"))
    
    conn.commit()
    conn.close()

def get_client_by_id(client_id):

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clients WHERE id = ?",(client_id, ))

    row = cursor.fetchone()
    conn.close()

    return row

def interaction(client_id, interaction_type, note):

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO interactions (client_id, note, interaction_type)
                   VALUES (?, ?, ?)
""",(client_id, note, interaction_type))
    
    conn.commit()
    conn.close()

def update_client(client_id, new_status):

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("UPDATE clients SET status = ? WHERE id = ?", (new_status, client_id))

    conn.commit()
    conn.close()

def view_records_by_status(status):

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM clients WHERE status = ? 
""",(status, ))
    
    row = cursor.fetchall()

    conn.close()

    return row

def get_client_status_counts():

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("SELECT status , COUNT(*) FROM clients GROUP BY status")

    result = cursor.fetchall()
    conn.close()

    return result

def get_total_clients_count():

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM clients")

    row = cursor.fetchone()

    result = row[0] if row[0] is not None else 0
    conn.close()

    return result

def get_most_active_client():

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT client_id, COUNT(*) from interactions GROUP BY client_id 
                   ORDER BY COUNT(*) DESC LIMIT 1
""")
    
    result = cursor.fetchone()
    conn.close()

    return result