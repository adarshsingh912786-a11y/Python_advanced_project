from database import (
    creat_table
)

from service import (
    
    update_client_status,
    create_client,
    add_interaction,
    view_records
)

def main():

    
     creat_table()

     while True:

        print("....... CRM SYSTEM.......")
        print("""
    1. Add client Information
    2. Add Interaction
    3. Update Status
    4. View Record
    5. Exit
            
    """)
        
        choice = input("choose from given option: ")

        if choice == "1":
            name = input("Enter the name of client: ")
            phone = input("client phone no: ")
            email = input("client email: ")

            try :
                create_client(name,phone,email)
                print("Client add succesfully")

            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error : {e}")

        elif choice == "2":

            client_id = int(input("Enter the client id: "))
            type = input("Enter the way of Interaction: ")
            note = input("Leave some note: ")

            try:
                add_interaction(client_id,type,note)
            except ValueError as e:
                print(f"Error : {e}")
            except Exception as e:
                print("Error : {e}")        

        elif choice == "3":
            client_id = int(input("Enter the client id: "))
            new_status = input("Enter the Updated Staus: ")

            try:
                update_client_status(client_id,new_status)
            except ValueError as e:
                print(f"Error : {e}")
            except Exception as e:
                print(f"Error : {e}")    

        elif choice == "4":

            status = input("Enter the staust: ")

            try :
                records = view_records(status)
                for view in records:
                    print(f"{view[1]} | {view[2]} | {view[3]} | {view[4]} | {view[5]}")
            except ValueError as e:
                print(f"Error : {e}")

            except Exception as e :
                print(f"Error {e}")            
            
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Chooce from givem option")

if __name__ == "__main__":
    main()            



        
        
        
         
            


