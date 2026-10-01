1. Install NumPy using pip and write a Python script list_vs_array.py that creates a list and a NumPy array, each containing the numbers from 1 to 1000.

import numpy as np

# Python list
python_list = list(range(1, 1001))

# NumPy array
numpy_array = np.array(range(1, 1001))

print("Python List:", python_list[:10])
print("NumPy Array:", numpy_array[:10])


2. In your script, measure and print the memory usage (in bytes) of both the Python list and the NumPy array containing 1000 integers.<br><br><em><strong>Hint:</strong> Use the sys.getsizeof() function for the list and the nbytes attribute for the NumPy array.</em>

import sys

python_list = list(range(1, 1001))
numpy_array = np.array(range(1, 1001))

list_memory = sys.getsizeof(python_list)
array_memory = numpy_array.nbytes

print("Python List Memory:", list_memory, "bytes")
print("NumPy Array Memory:", array_memory, "bytes")

3. Write a function compare_addition_speed() that adds 5 to every element in both a Python list and a NumPy array of 10,000 integers, and prints the time taken for each.<br><br><em><strong>Hint:</strong> Use the time module to measure execution time.</em>


4. Explain with code how vectorized operations in NumPy can replace for-loops when multiplying all elements of an array by 2. Show both the loop and the vectorized version using a Zomato-style example: multiplying all restaurant ratings by 2.



ratings = np.array([2.5, 3.0, 4.0, 4.5, 5.0])

result = []

for rating in ratings:
    result.append(rating * 2)

print(result)