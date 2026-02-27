import sqlite3

from database import (
    create_table,
    add_client,
    get_client_by_id,
    interaction,
    update_client,
    view_records_by_status
)


def create_client(name, phone, email):

    if name.strip() == "":
        raise ValueError("Name should not be empty")
    
    if phone == "":
        raise ValueError("Phone number should not be empty")
    
    if email == "":
        raise ValueError("Email should not be empty")
    
    try:
        add_client(name, phone, email)
    except sqlite3.IntegrityError:
        raise ValueError("Client already exists")

def add_interaction(client_id, interaction_type, note):

    client_details = get_client_by_id(client_id)

    if client_details is None:
        raise ValueError("Client not Exists")
    
    status = client_details[4]

    valid_interaction = {"call", "email", "meeting"}

    if interaction_type not in valid_interaction:
        raise ValueError("Invalid Interaction type")
    
    try:
        interaction(client_id, type, note)

        if status == "lead":
            update_client_status(client_id, interaction_type)
        
    except sqlite3.IntegrityError:
        raise ValueError("Check Constraints Failed")
    
def update_client_status(client_id, new_status):

    client_details = get_client_by_id(client_id)

    if client_details is None:
        raise ValueError("Client not Exists")
    
    current_status = client_details[4]
    new_status = new_status.strip().lower()

    valid_transitions = {
        "lead" : ["contacted", "lost"],
        "contacted" : ["converted", "lost"],
        "converted" : [],
        "lost" : []
    }

    if new_status not in valid_transitions[current_status]:
        raise ValueError("Invalid status transitions")
    
    try:
        update_client(client_id, new_status)
    except sqlite3.IntegrityError:
        raise ValueError ("Check Constraints Fail")
    
    Updated_info = get_client_by_id(client_id)

    update_status = Updated_info[4]

    return {
        "client_id" : client_id,
        "Update_status" : update_status
    }

def view_records(status):

    valid_interaction = {"lead", "contacted", "converted", "lost"}

    status = status.strip().lower()

    if status not in valid_interaction:
        raise ValueError("Invalid Status type")
    
    try:
        records = view_records_by_status(status)
    except sqlite3.IntegrityError:
        raise ValueError ("Check Status Failed")

    return records