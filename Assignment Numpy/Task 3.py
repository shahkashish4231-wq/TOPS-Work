1. Create a NumPy array representing the number of likes on 7 Instagram posts and print its ndim, shape, size, dtype, itemsize, and nbytes properties.

likes = np.array([120, 250, 180, 500, 320, 450, 600])

print("Array:", likes)
print("ndim:", likes.ndim)
print("shape:", likes.shape)
print("size:", likes.size)
print("dtype:", likes.dtype)
print("itemsize:", likes.itemsize)
print("nbytes:", likes.nbytes)

2. Given a 2D NumPy array of daily step counts for 5 days (each row is a day, columns are morning and evening), use reshape() to convert it into a 1D array, then back to a 2D array with 5 rows and 2 columns.<br><br><em><strong>Hint:</strong> Use the shape attribute to check your array after each reshape.</em>

steps = np.array([
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80],
    [90, 100]
])

print("Original array:")
print(steps)

print("Original shape:", steps.shape)

# Convert 2D array into 1D
steps_1d = steps.reshape(10)

print("\n1D array:")
print(steps_1d)
print("1D shape:", steps_1d.shape)

# Convert back to 2D: 5 rows and 2 columns
steps_2d = steps_1d.reshape(5, 2)

print("\nBack to 2D:")
print(steps_2d)
print("2D shape:", steps_2d.shape)

3. Build a NumPy array representing the prices of 12 food items from a Zomato order, then use ravel(), flatten(), and resize() to create different shaped versions of the data and print each result.<br><br><em><strong>Constraint:</strong> Show the difference between ravel() and flatten() in your code comments.</em>


4. Take a 3x3 NumPy array representing a mini Spotify playlist grid (rows: playlists, columns: song counts in categories like Pop, Rock, Indie). Use both T and np.transpose() to swap rows and columns, then print the transposed array.


playlist = np.array([
    [10, 5, 8],   
    [7, 12, 6],   
    [15, 9, 11]   
])

print("Original playlist:")
print(playlist)

print("\nUsing T:")
print(playlist.T)

print("\nUsing np.transpose():")
print(np.transpose(playlist))


5. Given a 1D NumPy array of 15 Flipkart product ratings, use reshape() to convert it into a 3x5 array, then use flatten() to return it to a 1D array. Explain in a comment when you would use flatten() versus ravel() in real projects.

import numpy as np

ratings = np.array([
    4, 5, 3, 4, 2,
    5, 4, 3, 5, 4,
    3, 4, 5, 2, 4
])

print("Original 1D array:")
print(ratings)
print("Shape:", ratings.shape)


ratings_2d = ratings.reshape(3, 5)

print("\n3x5 array:")
print(ratings_2d)
print("Shape:", ratings_2d.shape)


ratings_1d = ratings_2d.flatten()


print(ratings_1d)
print("Shape:", ratings_1d.shape)