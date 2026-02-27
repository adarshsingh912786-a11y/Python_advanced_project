from database import (
    create_table
)

from service import (
    create_client,
    add_interaction,
    update_client_status,
    view_records
)

def main():

    create_table()

    while True:

        print("---------------- CRM System ----------------")
        print("""
    1️⃣. Add client
    2️⃣. Add interaction
    3️⃣. Update Status
    4️⃣. View Records By Status
    5️⃣. Exit
    """)
        
        choice  = input("Choose from menu : ")

        if choice == "1":

            name  = input("Enter the name of client: ")
            phone = input("Clients phone_no : ")
            email = input("Clients email : ")

            try:
                create_client(name, phone, email)
                print("Client added successfully✔️")
            except ValueError as e:
                print(f"Error : {e}")
            except Exception as e:
                print(f"Error : {e}")


        elif choice == "2":
            
            client_id = int(input("Enter the client_id : "))
            interaction_type = input("Enter the way of interaction: ")
            note = input("Leave some note : ")

            try:
                add_interaction(client_id, interaction_type, note)
                print("Interaction Record saved successfully✔️")
            except ValueError as e:
                print(f"Error : {e}")
            except Exception as e:
                print(f"Error : {e}")


        elif choice == "3":
            
            client_id = int(input("Enter the client_id : "))
            new_status = input("Enter the updated status (contacted/ converted/ lost): ")

            try:
                update_status = update_client_status(client_id, new_status)
                print(f"Client_id : {update_status['client_id']}")
                print(f"New status : {update_status['Update_status']}")
            except ValueError as e:
                print(f"Error : {e}")
            except Exception as e:
                print(f"Error : {e}")


        elif choice == "4":
            
            status = input("Enter the Status: ")

            try:
                records = view_records(status)
                for view in records:
                    print(f"{view[0]}. {view[1]} | {view[2]} | {view[3]} | {view[4]} | {view[5]}")
            except ValueError as e:
                print(f"Error : {e}")


        elif choice == "5":
            print("Good-Bye.....")
            break

        else:
            print("Choose from menu only")

if __name__ == "__main__":
    main()