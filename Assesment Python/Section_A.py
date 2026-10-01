# Scenario 1

order_total = 499.50
distance = 7.3
payment_method = "UPI"
accepting_orders = True

print(type(order_total))
print(type(distance))
print(type(payment_method))
print(type(accepting_orders))

# With wrong data type
# float value store as an integer

order=499

discount = order * 0.90
print(discount)

#with correct data type

order = 499.50
discount = order * 0.90
print(discount)


# Scenario 2

menu1 = [
    ('Burger', 180, 'Snacks'),
    ('Dosa', 90, 'Breakfast')
]

for i in menu1:
    if i[0] == 'Burger':
        print(i[1])



menu2 = {
    'Burger': 180,
    'Dosa': 90
}

print(menu['Burger'])

#dictionary elements can find directly to the key value. while tuples go line by line.


# Scenario 3

def calculate_delivery_fee(order_value, distance):
    if order_value >= 500:
        return 0
    elif distance <= 5:
        return 30
    else:
        return 60

print(calculate_delivery_fee(400, 3))
print(calculate_delivery_fee(400, 8))
print(calculate_delivery_fee(600, 10))

# lambda

orders = [
    ("Order101", 450),
    ("Order102", 800),
    ("Order103", 300)
]

orders.sort(key=lambda order: order[1])

print(orders)


# Scenario 4

import json

order = {
    "order_id": 101,
    "customer": "Kashish",
    "restaurant": "Pizza",
    "amount": 600,
    "payment": "UPI"
}

with open("orders.json", "w") as file:
    json.dump(order, file, indent=4)

print("Order saved successfully.")

# read son file

try:
    with open("orders.json", "r") as file:
        loaded_order = json.load(file)

    print("Loaded order:", loaded_order)

except FileNotFoundError:
    print("No order found.")
    loaded_order = {}


# Scenario 5

rider_name = "Rahul"
gps_location = "Ahmedabad"
order_id = 101
status = "On the way"

def update_location():
    pass

def complete_delivery():
    pass

class Delivery:

    def __init__(self, rider_name, gps_location, order_id):
        self.rider_name = rider_name
        self.gps_location = gps_location
        self.order_id = order_id
        self.status = "On the way"

    def update_location(self, new_location):
        self.gps_location = new_location
        print("Location updated:", self.gps_location)

    def complete_delivery(self):
        self.status = "Completed"
        print("Delivery completed")


delivery1 = Delivery("Rahul", "Ahmedabad", 101)

delivery1.update_location("SG Highway")
delivery1.complete_delivery()

print(delivery1.status)


# Scenario 6

# enter string in stead of float
order_amount = float(input("Enter order amount: "))
# gives value error

# using try except

while True:
    try:
        order_amount = float(input("Enter order amount: "))
        break
    except ValueError:
        print("Invalid amount. Please enter a number.")

print("Order amount:", order_amount)

 # final

 while True:
    try:
        order_amount = float(input("Enter order amount: "))

        if order_amount < 0:
            print("Amount cannot be negative.")
            continue

        break

    except ValueError:
        print("Invalid input. Please enter a number.")

print("Order amount:", order_amount)