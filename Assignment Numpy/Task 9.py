1. Create a NumPy array named prices with these values: [299, 499, 799, 0, 1599, -1, 899]. Print the array and its data type.

prices = np.array([299, 499, 799, 0, 1599, -1, 899])

print("Prices:", prices)
print("Data type:", prices.dtype)


2. Some entries in the prices array are invalid (0 or negative). Replace all values less than or equal to zero with the average of the remaining positive prices.<br><br><em><strong>Hint:</strong> Use boolean indexing and the mean() function.</em>

positive = prices[prices > 0]

average = np.mean(positive)

print("Average:", average)

clean = prices.copy()
clean[clean <= 0] = average
print("Cleaned prices:", clean)


3. Suppose you have a NumPy array quantities = [2, 1, 3, 4, 2, 1, 5]. Calculate the total bill for each item by multiplying the cleaned prices array with quantities, and print the resulting array.

quantities = np.array([2, 1, 3, 4, 2, 1, 5])

item_bills = cleaned_prices * quantities

print("Item bills:", item_bills)


4. Generate and print a summary report: show the minimum, maximum, average, and total of the cleaned prices array, and also the total bill for all items combined.<br><br><em><strong>Hint:</strong> Use NumPy functions like min(), max(), mean(), and sum().</print("Minimum price:", np.min(cleaned_prices))
print("Maximum price:", np.max(clean))
print("Average price:", np.mean(clean))
print("Total price:", np.sum(clean))
print("Total bill:", np.sum(item_bills))
                                                                                                                                          
                                                                                                                                          
5. Use ChatGPT or Copilot to suggest a NumPy function or method that can help you find out how many unique price values are present in your cleaned prices array. Try the suggested method and print the result.

unique_prices = np.unique(cleaned_prices)

print("Unique prices:", unique_prices)
print("Number of unique prices:", len(unique_prices))
