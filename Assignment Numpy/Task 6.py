1. Create a NumPy array called prices with the following values: [199, 299, 399, 499, 599]. Use basic indexing to print the first and last price.

prices = np.array([199, 299, 399, 499, 599])

print("First price:", prices[0])
print("Last price:", prices[-1])


2. Given a 2D NumPy array representing cricket scores for 3 players across 5 matches, use slicing to extract the scores of all players for matches 2 to 4 (index 1 to 3).

scores = np.array([
    [45, 60, 72, 80, 55],
    [30, 50, 65, 70, 40],
    [55, 75, 68, 90, 62]
])

result = scores[:, 1:4]

print(result)

3. You have a NumPy array called ratings = np.array([4.5, 3.8, 4.2, 2.9, 5.0, 3.5]). Use negative indexing to print the last three ratings.

ratings = np.array([4.5, 3.8, 4.2, 2.9, 5.0, 3.5])

print("Last three ratings:", ratings[-3:])


4. Create a NumPy array of the first 20 natural numbers. Use step slicing to print every 3rd number starting from the second element.<br><br><em><strong>Hint:</strong> Use the slice notation with a step value.</em>

numbers = np.arange(1, 21)

result = numbers[1::3]

print("Numbers:", numbers)
print("number starting from second element:", result)


5. Given a NumPy array of Flipkart product prices, use boolean indexing to extract all prices greater than 500. Print the resulting array.

prices = np.array([250, 650, 450, 800, 350, 1200, 500, 750])

result = prices[prices > 500]

print("Prices above 500:", result)


6. You have an array of IPL team scores: np.array([210, 180, 195, 220, 205, 175]). Use np.where() to find the indices of all scores above 200 and print these indices.

scores = np.array([210, 180, 195, 220, 205, 175])

indices = np.where(scores > 200)

print("Indices of scores above 200:", indices)
