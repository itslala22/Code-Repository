products_database = {
    "Product1": {"pname": "apple", "unitprice": 1.99, "stock": 100},
    "Product2": {"pname": "banana", "unitprice": 2.99, "stock": 50},
    "Product3": {"pname": "orange", "unitprice": 3.99, "stock": 200}
}

customer_database = {
    "Customer1": {"cname": "Customer1", "Contact": 123, "order history": {}},
    "Customer2": {"cname": "Customer2", "Contact": 234, "order history": {}},
    "Customer3": {"cname": "Customer3", "Contact": 345, "order history": {}}
}

def add_item(name, item, quantity):
    if name in customer_database:
        customer_database[name]["order history"]["ordername"]=item
        customer_database[name]["order history"]["orderquantity"]=quantity
    else:
        customer_database["cname"]=name
        customer_database["order history"]["ordername"]=item
        customer_database["order history"]["orderquantity"]=quantity
    print (f"Added {item}.")
    print(customer_database[name])

add_item("Customer1","banana", 2)





# Product Database Example
products = {
    "product_id_1": {"name": "Product 1", "price": 10.99, "stock": 100},
    "product_id_2": {"name": "Product 2", "price": 15.99, "stock": 80},
    # Add more products...
}

# Customer Database Example
customers = {
    "customer_id_1": {"name": "Alice", "contact": "alice@example.com", "orders": {}},
    "customer_id_2": {"name": "Bob", "contact": "bob@example.com", "orders": {}},
    # Add more customers...
}

# Functions for order processing
def add_product_to_order(customer_id, product_id, quantity):
    # Check if the customer_id exists in the customers database
    if customer_id not in customers:
        print(f"Customer {customer_id} not found.")
        return False  # Indicates that the operation was not successful

    # Check if the product_id exists in the products database and if there is enough stock
    if product_id not in products or products[product_id]['stock'] < quantity:
        print(f"Product {product_id} not found or insufficient stock.")
        return False  # Indicates that the operation was not successful

    # If the product is being ordered for the first time, add it to the orders dictionary
    if 'orders' not in customers[customer_id]:
        customers[customer_id]['orders'] = {}

    # If the product already exists in the order, update the quantity; otherwise, add it
    if product_id in customers[customer_id]['orders']:
        customers[customer_id]['orders'][product_id] += quantity
    else:
        customers[customer_id]['orders'][product_id] = quantity

    # Deduct the quantity ordered from the product stock
    products[product_id]['stock'] -= quantity

    print(f"Added {quantity} of {products[product_id]['name']} to customer {customer_id}'s order.")
    return True  # Indicates that the operation was successful



def calculate_order_total(customer_id):
    # Check if the customer_id exists in the customers database
    if customer_id not in customers:
        print(f"Customer {customer_id} not found.")
        return None  # Indicates that the operation was not successful

    # Check if the customer has any orders
    if 'orders' not in customers[customer_id] or not customers[customer_id]['orders']:
        print(f"Customer {customer_id} has no orders.")
        return 0.0  # Returns 0.0 as the total cost if there are no orders

    # Calculate the total cost of all orders for the customer
    total_cost = 0.0
    for product_id, quantity in customers[customer_id]['orders'].items():
        # Ensure the product exists in the product database to avoid KeyError
        if product_id in products:
            product_price = products[product_id]['price']
            total_cost += product_price * quantity
        else:
            print(f"Product {product_id} not found in product database. Skipping.")

    print(f"Total cost for customer {customer_id} is: ${total_cost:.2f}")
    return total_cost  # Returns the total cost of the customer's order


def update_product_stock(product_id, quantity):
    # Check if the product_id exists in the products database
    if product_id not in products:
        print(f"Product {product_id} not found.")
        return False  # Indicates that the operation was not successful

    # Check if there is enough stock to fulfill the order
    if products[product_id]['stock'] < quantity:
        print(f"Insufficient stock for product {product_id}.")
        return False  # Indicates that the operation was not successful

    # Update the product stock
    products[product_id]['stock'] -= quantity
    print(f"Stock updated for product {product_id}: {products[product_id]['stock']} items left.")
    return True  # Indicates that the operation was successful



# Functions for customer management
def add_new_customer(customer_id, name, contact):
    # Check if the customer_id already exists in the customers database to avoid duplicates
    if customer_id in customers:
        print(f"Customer with ID {customer_id} already exists.")
        return False  # Indicates that the operation was not successful

    # Add the new customer to the database
    customers[customer_id] = {
        'name': name,
        'contact': contact,
        'orders': {}
    }
    
    print(f"New customer added: {name} with ID {customer_id}.")
    return True  # Indicates that the operation was successful


def display_customer_details(customer_id):
    # Check if the customer_id exists in the customers database
    if customer_id not in customers:
        print(f"Customer with ID {customer_id} does not exist.")
        return False  # Indicates that the customer was not found

    # Retrieve the customer's details
    customer = customers[customer_id]
    print(f"Details for customer ID {customer_id}:")
    print(f"Name: {customer['name']}")
    print(f"Contact: {customer['contact']}")

    # Check if the customer has any orders and display them
    if customer['orders']:
        print("Order history:")
        for product_id, quantity in customer['orders'].items():
            product_name = products[product_id]['name'] if product_id in products else "Unknown Product"
            print(f" - {product_name} (ID: {product_id}): Quantity {quantity}")
    else:
        print("No order history for this customer.")

    return True  # Indicates that the operation was successful



def remove_customer(customer_id):
    # Check if the customer_id exists in the customers database
    if customer_id in customers:
        # Delete the customer from the database
        del customers[customer_id]
        print(f"Customer {customer_id} has been removed from the database.")
        return True  # Indicates that the operation was successful
    else:
        print(f"Customer {customer_id} not found in the database.")
        return False  # Indicates that the customer was not found and not removed


# Reporting system functions
def generate_sales_report():
    total_revenue = 0
    product_sales = {}

    # Iterate through each customer and their orders
    for customer_id, customer_info in customers.items():
        for product_id, quantity in customer_info['orders'].items():
            # Update total revenue
            if product_id in products:
                total_revenue += products[product_id]['price'] * quantity

                # Update product sales
                if product_id in product_sales:
                    product_sales[product_id] += quantity
                else:
                    product_sales[product_id] = quantity

    # Print the sales report
    print("Sales Report:")
    print("Total Revenue: ${:.2f}".format(total_revenue))
    print("Product Sales:")
    for product_id, quantity in product_sales.items():
        product_name = products[product_id]['name'] if product_id in products else "Unknown Product"
        print(f" - {product_name} (ID: {product_id}): Quantity sold {quantity}")

    return True  # Indicates that the operation was successful


# Implement logic to find most popular products
def most_popular_products():

    product_popularity = {}

    # Aggregate total quantity ordered for each product
    for customer_id in customers:
        for product_id, quantity in customers[customer_id]['orders'].items():
            if product_id in product_popularity:
                product_popularity[product_id] += quantity
            else:
                product_popularity[product_id] = quantity

    # Sort the products by popularity (quantity ordered)
    sorted_products = sorted(product_popularity.items(), key=lambda x: x[1], reverse=True)

    # Display the most popular products
    print("Most Popular Products:")
    for product_id, total_quantity in sorted_products:
        product_name = products[product_id]['name'] if product_id in products else "Unknown Product"
        print(f"{product_name} (ID: {product_id}): Total Quantity Ordered {total_quantity}")

    return True  # Indicates that the operation was successful


# UI Function
def main_menu():
    while True:
        print("\nWelcome to the Customer Order Management System")
        print("1: Add a new customer")
        print("2: Add a product to a customer's order")
        print("3: Calculate the total cost of an order")
        print("4: Update product stock")
        print("5: Remove a customer")
        print("6: Display customer details")
        print("7: Exit")

        choice = input("Please choose an option (1-7): ")

        if choice == '1':
            customer_id = input("Enter customer ID: ")
            name = input("Enter customer name: ")
            contact = input("Enter customer contact details: ")
            add_new_customer(customer_id, name, contact)
        elif choice == '2':
            customer_id = input("Enter customer ID: ")
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity: "))
            add_product_to_order(customer_id, product_id, quantity)
        elif choice == '3':
            customer_id = input("Enter customer ID: ")
            print(f"The total cost for the order is: ${calculate_order_total(customer_id)}")
        elif choice == '4':
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity to restock: "))
            update_product_stock(product_id, quantity)
        elif choice == '5':
            customer_id = input("Enter customer ID to remove: ")
            remove_customer(customer_id)
        elif choice == '6':
            customer_id = input("Enter customer ID to display details: ")
            display_customer_details(customer_id)
        elif choice == '7':
            print("Thank you for using the Customer Order Management System.")
            break
        else:
            print("Invalid option, please try again.")


# Main program execution
if __name__ == "__main__":
    main_menu()