from database import(
    create_table,
    add_product,
    get_product_by_id,
    get_all_products,
    update_product_quantity,
    delete_product
)

from service import (
    create_product,
    change_stock
)

from analytics import (
    calculate_total_inventory_value
)

while True:

    create_table()

    print("--------------------- Stock Manager -----------------------")
    print("""
1️⃣. Add Products
2️⃣. View Products
3️⃣. Change Stock
4️⃣. Inventory Total
5️⃣. Exit
""")
    
    choice  = input("Choose the operation from menu : ")

    if choice == "1":

        name = input("Enter the stock name: ")
        quantity = int(input("Enter the quantity of stock: "))
        price = int(input("Enter the price of stock : "))
        threshold = int(input("Enter the min quantity of stock : "))

        try:
            create_product(name, quantity, price, threshold)
            print("Product created successfully✔️")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"System error : {e}")

    elif choice == "2":
        
        stock_result = get_all_products()

        print("\n------------------ Available Stocks ---------------------")

        for stock in stock_result:
            print(f"{stock[0]}. {stock[1]} | {stock[2]} | {stock[3]} | {stock[4]} | {stock[5]}")
        print("\n")

    elif choice == "3":
        
        id = int(input("Enter the id of the stock: "))
        change_amount = int(input("Enter the quantity for (-ve --> (-)): "))

        update_quantity = change_stock(id, change_amount)

        print(f"\nupdated_quantity: {update_quantity["updated_quantity"]}")
        if  update_quantity["low_stock"]:
            print("Warning! Stock thresolhd trigger")

    elif choice == "4":

        total = calculate_total_inventory_value()

        print(f"\nTotal inventory value : {total["total_value"]}")
        print(f"Total inventory products : {total["total_products"]}")
        print(f"Average inventory value : {total["average_value"]}\n")

    elif choice == "5":
        print("Thank you...")
        break
    else:
        print("Please choose from the menu only❌")