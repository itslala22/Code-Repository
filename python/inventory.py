inventory= {}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Added {quantity} {item}(s).")

def view_inventory():
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def update_item(item, quantity):
    if item in inventory:
        inventory[item] = quantity
        print(f"Updated {item} quantity to {quantity}.")
    else:
        print(f"{item} not found in inventory.")