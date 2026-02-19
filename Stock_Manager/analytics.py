from database import get_all_products

def calculate_total_inventory_value():

    products = get_all_products()

    total_value = 0
    total_products = len(products)

    for product in products:
        quantity = product[2]
        price = product[3]
        total_value += quantity * price
    
    if total_value == 0:
        total_value = 0
        average_value = 0
    else: 
        average_value = total_value / total_products
    
    return {
        "total_value" : total_value,
        "total_products" : total_products,
        "average_value" : average_value
    }