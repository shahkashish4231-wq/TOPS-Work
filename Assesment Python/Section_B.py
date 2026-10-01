# Task 1

order_value = float(input("Enter order value (Rs): "))
distance = float(input("Enter delivery distance (km): "))

# Check for negative values
if order_value < 0 or distance < 0:
    print("Error: Order value and delivery distance cannot be negative.")

else:
    if order_value >= 500:
        delivery_fee = 0
    elif distance <= 5:
        delivery_fee = 30
    else:
        delivery_fee = 60


    final_amount = order_value + delivery_fee

    
    print("\n----- FOOD DELIVERY BILL -----")
    print(f"Item Total       : Rs", order_value)
    print(f"Delivery Fee     : Rs", delivery_fee)
    print(f"Final Amount     : Rs", final_amount)

# Task 2

menu = {
    "Paneer Tikka": {
        "price": 250,
        "category": "Starter"
    },
    "Veg Biryani": {
        "price": 220,
        "category": "Main Course"
    },
    "Masala Dosa": {
        "price": 150,
        "category": "Breakfast"
    },
    "Manchurian": {
        "price": 180,
        "category": "Starter"
    },
    "Paneer Butter Masala": {
        "price": 280,
        "category": "Main Course"
    },
    "Gulab Jamun": {
        "price": 100,
        "category": "Dessert"
    }
}

def view_menu():
    for i in menu:
        print(i, "-", "Rs", menu[i]["price"], "-", menu[i]["category"])

def filter_category():
    category = input("Enter category: ")

    for i in menu:
        if menu[i]["category"].lower() == category.lower():
            print(i, "-", "Rs", menu[i]["price"])

def search_dish():
    i = input("Enter dish name: ")

    if i in menu:
        print("Price: Rs", menu[i]["price"])
    else:
        print("Dish not found")

while True:

    print("\n1. View all items")
    print("2. Filter by category")
    print("3. Search dish")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_menu()

    elif choice == "2":
        filter_category()

    elif choice == "3":
        search_dish()

    elif choice == "0":
        print("Program ended")
        break

    else:
        print("Invalid choice")


# Task 3

import json


# Function to add a new order
def add_order():

    customer_name = input("Enter customer name: ")

    items = input("Enter items: ")
    items = items.split(",")

    try:
        total_amount = float(input("Enter total amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    status = input("Enter order status: ")

    # Load existing orders
    try:
        with open("orders.json", "r") as file:
            orders = json.load(file)

    except FileNotFoundError:
        orders = []

    # Create new order
    new_order = {
        "customer_name": customer_name,
        "items": items,
        "total_amount": total_amount,
        "status": status
    }

    # Add new order
    orders.append(new_order)

    # Save orders
    with open("orders.json", "w") as file:
        json.dump(orders, file, indent=4)

    print("Order saved successfully!")


# Function to view all orders
def view_orders():

    try:
        with open("orders.json", "r") as file:
            orders = json.load(file)

        if len(orders) == 0:
            print("No orders found.")

        else:
            print("\n----- ORDER HISTORY -----")

            for order in orders:
                print("\nCustomer:", order["customer_name"])
                print("Items:", ", ".join(order["items"]))
                print("Total Amount: Rs", order["total_amount"])
                print("Status:", order["status"])

    except FileNotFoundError:
        print("No order history found.")


# Main program
while True:

    print("\n===== FOOD DELIVERY SYSTEM =====")
    print("1. Add Order")
    print("2. View Orders")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_order()

    elif choice == "2":
        view_orders()

    elif choice == "0":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")