import json

class Order:

    def __init__(self, order_id, customer_name, items, total_amount, status="Pending"):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount
        self.status = status

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "items": self.items,
            "total_amount": self.total_amount,
            "status": self.status
        }




def load_orders():

    try:
        with open("orders.json", "r") as file:
            data = json.load(file)

            orders = []

            for order in data:
                obj = Order(
                    order["order_id"],
                    order["customer_name"],
                    order["items"],
                    order["total_amount"],
                    order["status"]
                )

                orders.append(obj)

            return orders

    except FileNotFoundError:
        print("No previous order file found.")
        return []

    except json.JSONDecodeError:
        print("Order file is invalid.")
        return []



def save_orders(orders):

    data = []

    for order in orders:
        data.append(order.to_dict())

    with open("orders.json", "w") as file:
        json.dump(data, file, indent=4)




def place_order(orders):

    # Customer name validation
    while True:
        customer_name = input("Enter customer name: ").strip()

        if customer_name == "":
            print("Customer name cannot be empty.")
        else:
            break

  
    items_input = input("Enter items separated by comma: ")

    items = items_input.split(",")

  

    while True:

        try:
            total_amount = float(input("Enter total amount: "))

            if total_amount < 0:
                print("Amount cannot be negative.")
            else:
                break

        except ValueError:
            print("Invalid amount. Please enter a number.")

    
    if len(orders) == 0:
        order_id = 1
    else:
        order_id = orders[-1].order_id + 1

    
    new_order = Order(order_id, customer_name, items, total_amount)

   
    orders.append(new_order)

    save_orders(orders)

    print("\nOrder placed successfully!")
    print("Order ID:", order_id)


def view_orders(orders):

    if len(orders) == 0:
        print("\nNo orders found.")
        return

    print("\n================ ALL ORDERS ================")
    print(f"{'ID':<8}{'Customer':<20}{'Items':<10}{'Amount':<15}{'Status'}")
    print("-" * 65)

    for order in orders:

       
        if order.status == "Delivered":
            status = ">>> DELIVERED <<<"
        else:
            status = order.status

        print(
            f"{order.order_id:<8}"
            f"{order.customer_name:<20}"
            f"{len(order.items):<10}"
            f"Rs {order.total_amount:<12.2f}"
            f"{status}"
        )




def search_order(orders):

    try:
        order_id = int(input("Enter Order ID: "))
    except ValueError:
        print("Order ID must be a number.")
        return

    for order in orders:

        if order.order_id == order_id:

            print("\n------ ORDER FOUND ------")
            print("Order ID:", order.order_id)
            print("Customer:", order.customer_name)
            print("Items:", ", ".join(order.items))
            print("Total Amount: Rs", order.total_amount)
            print("Status:", order.status)

            return

    print("Order not found.")




orders = load_orders()

while True:

    print("\n========== FOOD DELIVERY SYSTEM ==========")
    print("1. Place New Order")
    print("2. View All Orders")
    print("3. Search Order by ID")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        place_order(orders)

    elif choice == "2":

        view_orders(orders)

    elif choice == "3":

        search_order(orders)

    elif choice == "4":

        print("Thank you! Program ended.")
        break

    else:

        print("Invalid choice. Please select 1, 2, 3 or 4.")