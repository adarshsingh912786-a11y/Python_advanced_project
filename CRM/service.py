import sqlite3

from database import (
    add_client
)

def create_client(name, phone, email):
    
    if name.strip() == "":
        raise ValueError("Name should not be empty")
    
    if phone == "":
        raise ValueError("Phone should not empty")
    
    if email == "":
        raise ValueError("Email should not be empty")
    
    try:
        add_client(name, phone, email)

    except sqlite3.IntegrityError:
        raise ValueError("Client already exists")  

 
        

