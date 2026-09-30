1. Create three variables in Python: user_name, fav_app, and daily_usage_hours. Assign your own name, your favorite app (like Instagram or Zomato), and how many hours you use it daily.

user_name = "Kashish"
fav_app = "PUBG"
daily_usage = 3

print("Name:", user_name)
print("Favorite App:", fav_app)
print("Daily Usage:", daily_usage, "hours")

2. Write a Python script that declares variables for product_name, price, and is_available to represent an item on Flipkart. Print each variable and its data type using the type() function.

name = "Samsung Galaxy S24"
price = 54999.99
available = True

print(name)
print(type(name))

print(price)
print(type(price))

print(available)
print(type(available))

3. Demonstrate the difference between single-line and multi-line comments in Python by writing a script that explains how a Spotify playlist recommendation system might work. Use # for single-line and triple quotes for multi-line comments.

# This is single line comment


"""
This
is
multi
line
comment
"""

print("Spotify playlist recommendation system")

4. Create variables for order_total, delivery_region, and discount_percent to represent a Zomato order. Follow Python naming conventions and print a sentence using all three variables, like 'Order from [region] totals ₹[order_total] with [discount_percent]% discount.'

total = 850
region = "Ahmedabad"
discount = 20

print(f"Order from {region} totals ₹{total} with {discount}% discount.")

5. Write a Python script that intentionally mixes tabs and spaces for indentation, then fix the script so it runs without errors.<br><br><em><strong>Hint:</strong> Use only spaces for indentation, as per Python's best practices.</em>

-> wrong type

order_total = 1000

if order_total > 500:
    print("Discount is applicable")
	print("Free delivery available")

-> correct way

order_total = 1000

if order_total > 500:
    print("Discount is applicable")
    print("Free delivery available")