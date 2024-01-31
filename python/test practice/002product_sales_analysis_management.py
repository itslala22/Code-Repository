# Product Sales Analysis System

# Product Database
products = {
    'Product1': {'price': 10, 'sales': 0, 'feedback': [], 'average_rating': 0},
    'Product2': {'price': 20, 'sales': 0, 'feedback': [], 'average_rating': 0},
    # Add more products as needed
}

# Function to track sales
def track_sale(product_name, quantity):
    if product_name in products:
        products[product_name]['sales'] += quantity
        print(f"Sale recorded: {quantity} units of {product_name}")
    else:
        print("Product not found.")

# Function to calculate total sales per product
def calculate_total_sales(product_name):
    if product_name in products:
        total_sales = products[product_name]['sales'] * products[product_name]['price']
        return total_sales
    else:
        return "Product not found."

# Function to find the best-selling product
def best_selling_product():
    best_seller = max(products, key=lambda x: products[x]['sales'])
    return best_seller

# Function to record customer feedback
def record_feedback(product_name, rating):
    if product_name in products and 0 <= rating <= 5:
        products[product_name]['feedback'].append(rating)
        update_average_rating(product_name)
        print("Feedback recorded.")
    else:
        print("Invalid input.")

# Function to update product average rating
def update_average_rating(product_name):
    if products[product_name]['feedback']:
        avg_rating = sum(products[product_name]['feedback']) / len(products[product_name]['feedback'])
        products[product_name]['average_rating'] = avg_rating

# Main menu
def main_menu():
    while True:
        print("\nProduct Sales Analysis System")
        print("1. Record a Sale")
        print("2. Display Total Sales for a Product")
        print("3. Show Best-Selling Product")
        print("4. Record Customer Feedback")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            product = input("Enter product name: ")
            quantity = int(input("Enter quantity sold: "))
            track_sale(product, quantity)
        elif choice == '2':
            product = input("Enter product name: ")
            print(f"Total Sales for {product}: {calculate_total_sales(product)}")
        elif choice == '3':
            print(f"Best-Selling Product: {best_selling_product()}")
        elif choice == '4':
            product = input("Enter product name: ")
            rating = float(input("Enter customer rating (0-5): "))
            record_feedback(product, rating)
        elif choice == '5':
            print("Exiting system.")
            break
        else:
            print("Invalid choice, please try again.")

# Start the system
main_menu()
