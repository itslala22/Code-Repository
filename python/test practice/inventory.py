inventory = {}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print (f"Added {item} {inventory}.")

def view_inventory():
    for item, quantity in inventory:
        print(f"{item}: {inventory}")

def update_item(item, quantity):
    if item in inventory:
        inventory [item] +- quantity
        print (f"Added {item} in the inventory.")
    else:
        print (f"{item} can not be found in the inventory.")


def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == "1":
            item = input("Enter the item: ")
            quantity = int(input("Enter the quantity: "))
            add_item(item, quantity)
        if choice == "2":
            view_inventory()
        if choice == "3":
            item = input("Enter the item: ")
            quantity = int(input("Enter the quantity: "))
            update_item(item, quantity)
        if choice == "4":
            print("Exit the inventory management system.")
            break
        else:
            print("Invalid number, please try again.\n")


manage_inventory()
