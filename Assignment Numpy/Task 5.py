1. Create two NumPy arrays representing the number of likes on your last 7 Instagram posts and your friend's last 7 posts, then use np.add() and np.subtract() to calculate both the combined and difference arrays.

my_likes = np.array([250, 320, 410, 280, 500, 350, 450])
friend_likes = np.array([300, 280, 390, 310, 450, 400, 420])

combined = np.add(my_likes, friend_likes)
difference = np.subtract(my_likes, friend_likes)

print("My likes:", my_likes)
print("Friend likes:", friend_likes)
print("Combined likes:", combined)
print("Difference:", difference)

2. Given a NumPy array of item prices from your last Zomato order, use np.multiply() to apply a 10% discount on each item, then use np.sum() to calculate the final bill amount after discount.<br><br><em><strong>Hint:</strong> To apply a 10% discount, multiply each price by 0.9.</em>

prices = np.array([250, 180, 320, 150, 200])

discounted_prices = np.multiply(prices, 0.9)

final_bill = np.sum(discounted_prices)

print("Original prices:", prices)
print("Prices after 10% discount:", discounted_prices)
print("Final bill:", final_bill)

3. Take a NumPy array of daily step counts for the last 30 days (you can make up the numbers), and use np.mean(), np.median(), np.std(), and np.max() to analyze your fitness stats like a health app would.

steps = np.array([
    6500, 7200, 8100, 5500, 9000,
    7600, 6800, 8200, 9500, 7100,
    6300, 8800, 7400, 7900, 10200,
    6900, 7300, 8500, 9100, 6700,
    7800, 8200, 6000, 9700, 8900,
    7500, 8300, 7200, 9400, 8000
])

print("Average steps:", np.mean(steps))
print("Median steps:", np.median(steps))
print("Standard deviation:", np.std(steps))
print("Maximum steps:", np.max(steps))

4. Create a NumPy array of 10 random float ratings (between 1 and 5) for a new movie on BookMyShow, then use np.round(), np.floor(), and np.ceil() to show how the rating would appear if rounded to the nearest whole number, always rounded down, and always rounded up.

np.random.seed(10)

ratings = np.random.uniform(1, 5, 10)

print("Original ratings:")
print(ratings)

print("Rounded ratings:")
print(np.round(ratings))

print("Floor ratings:")
print(np.floor(ratings))

print("Ceil ratings:")
print(np.ceil(ratings))


5. Use ChatGPT to generate Python code that calculates the percentage of songs you skipped in your last 20 Spotify plays using NumPy arrays and np.percentile(), then run the code and paste your output.<br><br><em><strong>Hint:</strong> Ask ChatGPT for code that finds the 75th percentile of skips in a NumPy array.</em>