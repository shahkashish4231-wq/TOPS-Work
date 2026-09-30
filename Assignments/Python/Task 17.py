1. Use the math module to calculate the square root, factorial, and value of pi for given numbers, and print each result.

import math

number = 100

square_root = math.sqrt(number)
factorial = math.factorial(number)
pi_value = math.pi

print("Square root:", square_root)
print("Factorial:", factorial)
print("Value of pi:", pi_value)

2. Write a script that lists all files in your current directory using the os module, and prints only those files with a .jpg or .png extension.<br><br><em><strong>Hint:</strong> Use os.listdir() and string methods to filter file names.</em>


3. Create a Python program that accepts a date in 'YYYY-MM-DD' format from the user and displays the day of the week using the datetime module.

from datetime import datetime

date_input = input("Enter date : ")

date = datetime.strptime(date_input, "%Y-%m-%d")

day = date.strftime("%A")

print("Day:", day)

4. Build a simple custom module named insta_utils.py with a function format_follower_count(n) that returns '1.5K' for 1500 and '2.3M' for 2300000. Import and use this function in another script to display formatted counts for 3 sample numbers.

5. Create a new virtual environment using venv, activate it, and install the statistics and requests packages via pip. Then, write a script that uses statistics.mean() to calculate the average of a list of numbers.