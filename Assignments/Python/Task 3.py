1. Declare four variables in Python: one integer (number of followers), one float (average rating), one string (your favorite app's name), and one boolean (is_premium_user). Print each variable and its type using the type() function.

one_integer = 15000
one_float = 4.5
one_string = "Spotify"
one_boolean = True

print(one_integer)
print(type(one_integer))

print(one_float)
print(type(one_float))

print(one_string)
print(type(one_string))

print(one_boolean)
print(type(one_boolean))

2. Write a Python program that takes a user's input for the price of a Zomato order as a string, converts it to a float using type casting, adds 18% GST, and prints the final bill amount.

food_price = input("Enter Zomato order price: ")

food_price = float(price)

gst = price * 18 / 100
final_bill = food_price + gst

print("Final bill amount:", final_bill)

3. Given a list of strings representing product prices from Flipkart, like ['199.99', '299.50', '150'], convert all to floats and calculate the total cart value.

prices = ['199.99', '299.50', '150']

float_prices = []

for price in prices:
    float_prices.append(float(price))

total = sum(float_prices)

print("Prices:", float_prices)
print("Total cart value:", total)

4. Build a function is_discount_applicable(order_amount) that takes a float and returns True if the amount is greater than 500, otherwise False. Print the result for order amounts 450 and 750.

def dis(amount):
    if amount > 500:
        print("Discount Applicable")
    else:
        print("Discont Not Applicable")


print(dis(450))
print(dis(750))

5. You received a dataset of ratings as strings from Spotify: ['4.5', '3.0', '5', '4.2']. Use type casting to convert these to floats, then find and print the highest rating.<br><br><em><strong>Hint:</strong> Use the float() function inside a loop or list comprehension.</em>

ratings = ['4.5', '3.0', '5', '4.2']

highest_rating = max(ratings)

print("Highest rating:", highest_rating)