import sqlite3

file_name = "client databse.db"

def get_connect():
    return sqlite3.connect(file_name)

def creat_table():

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS clients(
                   id INTEGER PRIMARY KEY AUTOMATION,
                   name TEXT NOT NULL,
                   phone_no TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE,
                   status TEXT NOT NULL CHECK(status IN("lead","contacted","converted","lost")),
                   created_at TEXT DEFAULT CURRENT_TIMESTAMP
                   )
""")
    
    cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS interactions(
                   id INTEGER PRIMARY KEY AUTOMATION,
                   client_id INTEGER NOT NULL,
                   note TEXT NOT NULL,
                   note TEXT NOT NULL,
                   interaction_type TEXT NOT NULL CHECK(interaction_type IN("call","email","meeting")),
                   create_at TEXT DEFAULT CURRENT_TEMESTAMP
                   FOREIGN KEY (client_id) REFERENCES clients(id)
                   )
""")
    
    conn.commit()
    conn.close()

def add_client(name, phone, email):
    
    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""
            INSERT INTO clients (name, phone_no, email, status) VALUES (?,?,?,?)
""", (name, phone, email, "lead"))
    
    conn.commit()
    conn.close()
    

    