import sqlite3

from database import(
    create_table,
    add_product,
    get_product_by_id,
    get_all_products,
    update_product_quantity,
    delete_product
)

def create_product(name, quantity, price, threshold):

    if name or name.strip() == "":
        raise ValueError ("Name cannot be Empty")
    
    if quantity < 0:
        raise ValueError ("Quantity cannot be zero(0)")
    
    if price < 0:
        raise ValueError ("Price cannot be Zero(0)")
    
    if threshold < 0:
        raise ValueError ("Threshold of any stock cannot be Zero(0)")
    
    try:
        add_product(name.strip(), quantity, price, threshold)
    except sqlite3.IntegrityError:
        raise ValueError ("product already Exist")
    
    
def change_stock(product_id, change_quantity):

    product_details = get_product_by_id(product_id)

    if product_details is None:
        raise ValueError ("Product not found")
    
    current_quantity = product_details[2]

    new_quantity = current_quantity + change_quantity

    if new_quantity < 0:
        raise ValueError ("Insufficient stock")
    
    update_product_quantity(product_id, new_quantity)

    return get_product_by_id(product_id)