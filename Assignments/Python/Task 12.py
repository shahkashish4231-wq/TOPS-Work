1. Write a lambda function that takes a price in rupees and returns the price after adding 18% GST. Test it on the prices 100, 250, and 500.

gst_price = lambda price: price + (price * 0.18)

print(gst_price(100))
print(gst_price(250))
print(gst_price(500))

2. Given a list of song titles from Spotify with extra spaces and inconsistent casing, use map() and a lambda function to clean each title so that it is stripped of spaces and converted to title case (e.g., ' shape OF you ' → 'Shape Of You').

3. Use filter() and a lambda function to extract only those Flipkart product names from a list that start with the letter 'S' (case-insensitive).
products = [
    "Samsung Galaxy",
    "iPhone 15",
    "Sony Headphones",
    "Samsung Earbuds",
    "samsung TV",
    "Realme"
]

s_products = list(filter(lambda product: product.lower().startswith("s"), products))

print(s_products)

4. Given a list of order amounts from a Zomato cart [120, 340, 560, 80], use reduce() from functools to calculate the total bill amount.


5. Use ChatGPT or Copilot to generate a Python code snippet that uses map(), filter(), and reduce() together to process a list of numbers: first double each number, then filter to keep only numbers greater than 100, and finally sum the result. Paste and test the generated code with the list [40, 60, 80, 120].