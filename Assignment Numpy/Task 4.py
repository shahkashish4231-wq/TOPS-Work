1. Create two NumPy arrays: one representing the number of likes on your last 7 Instagram posts, and another for the number of comments. Use arithmetic operators to calculate the average engagement (likes + comments) per post and print the result.

likes = np.array([120, 250, 180, 300, 450, 500, 350])
comments = np.array([10, 25, 15, 30, 40, 50, 35])


engagement = likes + comments

average_engagement = np.mean(engagement)

print("Engagement per post:", engagement)
print("Average engagement:", average_engagement)

2. Given two NumPy arrays: one with the prices of 5 food items on Zomato and another with the corresponding discounts in rupees, use element-wise subtraction to get the final price for each item and display the array.

prices = np.array([250, 400, 300, 500, 200])
discounts = np.array([50, 80, 30, 100, 20])


final_prices = prices - discounts

print("Final prices:", final_prices)

3. Suppose you have a NumPy array of IPL team scores for 5 matches. Use comparison operators to create a boolean array indicating which matches had scores greater than 180, then print the boolean array.<br><br><em><strong>Hint:</strong> Use the '>' operator directly on the array.</em>

scores = np.array([175, 210, 165, 195, 180])

result = scores > 180

print("Scores:", scores)
print("Greater than 180:", result)


4. Create two NumPy arrays: one showing whether a user paid via Paytm (1 for paid, 0 for not) and another for PhonePe for 6 transactions. Use np.logical_or() to find out which transactions were paid by either app and print the result.

paytm = np.array([1, 0, 1, 0, 0, 1])
phonepe = np.array([0, 1, 1, 0, 1, 0])

paid_by_either = np.logical_or(paytm, phonepe)

print("Paytm:", paytm)
print("PhonePe:", phonepe)
print("Paid by either app:", paid_by_either)

5. Given a NumPy array of the number of steps you walked each day for a week, use broadcasting to add a bonus of 500 steps to each day's count, then calculate and print the total steps for the week using an aggregate operation.

steps = np.array([5000, 6500, 7000, 4500, 8000, 9000, 6000])


bonus_steps = steps + 500


total_steps = np.sum(bonus_steps)

print("Original steps:", steps)
print("Steps after bonus:", bonus_steps)
print("Total steps for the week:", total_steps)