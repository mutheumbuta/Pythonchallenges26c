#nested dictionary for company departments
company = {"Finance": {"Name": "Ruth", "Role": "Accounts Payable"}, "Production": {"Name": "Mbuvi", "Role": "Production Supervisor"},"IT": {"Name": "Victor", "Role": "Developer"},"HR": {"Name": "Alice", "Role": "Manager"}}
print(f"Company organizational structure: {company}")

# 1. Sum up all items in a dictionary
def sum_dictionary_items(d):
    return sum(d.values())

# Example usage:
prices = {"mangoes": 20, "books": 2450, "cabbages": 80}
print("Sum of dictionary items:", sum_dictionary_items(prices))


#  Inventory management system
inventory = {}

def add_item(name, price, quantity):
    inventory[name] = {"price": price, "quantity": quantity}

def update_item(name, price=None, quantity=None):
    if name in inventory:
        if price is not None:
            inventory[name]["price"] = price
        if quantity is not None:
            inventory[name]["quantity"] = quantity
    else:
        print(f"{name} not found in inventory.")

def remove_item(name):
    if name in inventory:
        del inventory[name]
    else:
        print(f"{name} not found in inventory.")

# Example usage:
add_item("lock nut", 10, 4009)
add_item("Bolt 10mm X 3", 5, 100)
update_item("lock nut", quantity=34)
remove_item("Bolt 10mm X 3")
print("Inventory:", inventory)



# 4. Function to return identical items from two sets
def identical_items(set1, set2):
    return set1.intersection(set2)

# Example usage:
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Identical items:", identical_items(set_a, set_b))

