def calculate_bill(items, prices, previous_orders):

    # Calculate subtotal
    subtotal = 0

    for price in prices:
        subtotal = subtotal + price

    # Calculate GST
    gst = subtotal * 0.18

    # Delivery fee
    delivery_fee = 30

    # Loyalty discount
    if previous_orders > 5:
        discount = subtotal * 0.10
    else:
        discount = 0

    # Final amount
    final_amount = subtotal + gst + delivery_fee - discount

    return subtotal, gst, delivery_fee, discount, final_amount


# Take food items
items_input = input("Enter food items separated by comma: ")
items = items_input.split(",")

# Take prices
prices = []

for item in items:

    while True:
        try:
            price = float(input("Enter price for " + item.strip() + ": "))

            if price < 0:
                print("Price cannot be negative.")
            else:
                prices.append(price)
                break

        except ValueError:
            print("Invalid price. Enter a number.")


# Take previous order count
while True:
    try:
        previous_orders = int(input("Enter previous order count: "))

        if previous_orders < 0:
            print("Order count cannot be negative.")
        else:
            break

    except ValueError:
        print("Invalid order count. Enter a whole number.")


# Calculate bill
subtotal, gst, delivery_fee, discount, final_amount = calculate_bill(
    items, prices, previous_orders
)


# Print receipt
print("\n========== FOOD RECEIPT ==========")

for i in range(len(items)):
    print(f"{items[i].strip():20} Rs {prices[i]:.2f}")

print("----------------------------------")
print(f"Subtotal             Rs {subtotal:.2f}")
print(f"GST (18%)            Rs {gst:.2f}")
print(f"Delivery Fee         Rs {delivery_fee:.2f}")

if discount > 0:
    print(f"Loyalty Discount     -Rs {discount:.2f}")

print("----------------------------------")
print(f"Final Amount         Rs {final_amount:.2f}")
print("==================================")