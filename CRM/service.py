import sqlite3

from database import (
    add_client,
    get_client_by_id,
    interaction,
    update_client
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

def add_interaction(client_id,type,note): 

    client_detail = get_client_by_id(client_id)

    if client_detail is None:
        raise ValueError("Client not found")  

    status =  client_detail[4]


    if status != "lead":
        raise ValueError("Status is not aaplicable")


    valid_interaction = {"call","email","meeting"}

    if type not in valid_interaction:
        raise ValueError("Invalid Interaction type")
    
    try :
        interaction(client_id,type,note)

    except sqlite3.IntegrityError:
        raise ValueError("Check Contraints Failed")  

def update_client_status(client_id,new_status):

    client_detail = get_client_by_id(client_id)

    if client_detail is None:
        raise ValueError("Client not Exists")  

    current_status = client_detail[4]     
    
    valid_transaction = {
        "lead":["contacted","converted"],
        "contacted": ["converted","lost"],
        "converted":[],
        "lost":[],

    }
 
    if new_status not in valid_transaction(current_status):
        raise ValueError("Invalid status interaction")

    try :
        update_client(client_id, new_status)

    except sqlite3.IntegrityError:
        raise ValueError("Cllient not Exists")  

    Updated_info = get_client_by_id(client_id)

    update_status = Updated_info[4]

    return{
        "client_id" : client_id,
        "update_status" : update_status
    }  


       

 
        

