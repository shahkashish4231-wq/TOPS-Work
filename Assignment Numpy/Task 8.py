1. Given a NumPy array of IPL team names with some duplicates, use np.unique() to print a sorted list of all unique team names.

teams = np.array([
    "CSK", "MI", "RCB", "CSK", "KKR",
    "MI", "GT", "RCB", "GT", "PBKS"
])

unique_teams = np.unique(teams)

print("Unique teams:", unique_teams)


2. Create a NumPy array of Zomato order ratings (with some NaN values), then use np.isnan() to count how many ratings are missing.

ratings = np.array([4.5, 4.0, np.nan, 3.8, np.nan, 4.2, 5.0])

missing = np.isnan(ratings)

print("Missing values:", missing)
print("Number of missing ratings:", np.sum(missing))


3. Given an array of Flipkart product prices, use np.clip() to limit all prices between 100 and 1000, and print the resulting array.<br><br><em><strong>Hint:</strong> Use np.clip(array, 100, 1000).</em>

prices = np.array([50, 150, 500, 750, 1200, 2000, 900])

clip_prices = np.clip(prices, 100, 1000)

print("Original prices:", prices)
print("Clipped prices:", clip_prices)


4. You have a NumPy array of YouTube video view counts, some of which are NaN or inf. Replace all NaN values with 0, and all inf values with the maximum finite value in the array.

5. Use ChatGPT to generate a Python code snippet that finds the indices of all even numbers in a NumPy array using np.where(), then test the code with your own example array.

numbers = np.array([11, 24, 37, 42, 55, 68, 73, 80])

even_indices = np.where(numbers % 2 == 0)

print("Array:", numbers)
print("Indices of even numbers:", even_indices)
