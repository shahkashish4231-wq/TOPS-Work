1. Write a Python function safe_divide(a, b) that returns the result of a divided by b, and handles ZeroDivisionError by returning the string 'Cannot divide by zero'.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(safe_divide(10, 2))
print(safe_divide(10, 0))


2. Simulate a Zomato-style rating system: ask the user for number of reviews and total stars, then calculate average rating. Use try-except to handle invalid (non-numeric) input and print an error message if input is not a number.<br><br><em><strong>Hint:</strong> Use input() and int() conversion inside a try block.</em>

try:
    reviews = int(input("Enter number of reviews: "))
    total_stars = int(input("Enter total stars: "))

    average_rating = total_stars / reviews

    print("Average rating:", average_rating)

except ValueError:
    print("Error: Please enter numbers only.")
except ZeroDivisionError:
    print("Error: Number of reviews cannot be zero.")

3. Create a function get_playlist_duration(songs) that takes a list of song durations (in seconds) and returns the total duration in minutes. Raise a custom exception InvalidDurationError if any duration in the list is negative.<br><br><em><strong>Hint:</strong> Define your own exception class by subclassing Exception.</em>

4. Build a Flipkart-style order summary: ask the user for item price and quantity, then calculate and print total price. Use try-except-else-finally blocks to handle ValueError for invalid input, print the total if successful, and always print 'Thank you for shopping!' in the finally block.

try:
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

except ValueError:
    print("Error: Please enter valid numbers.")

else:
    total_price = price * quantity
    print("Total price:", total_price)

finally:
    print("Thank you for shopping!")


5. Use ChatGPT or Copilot to generate a Python code snippet that asks for two numbers and divides them, handling both ZeroDivisionError and ValueError. Paste the generated code, run it, and write one line about what you learned from the AI's approach.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")