1.
Create two NumPy arrays representing the ratings of 5 restaurants on Zomato and Swiggy, then use np.concatenate() to combine them into a single array of 10 ratings and print the result.
2.
Given three arrays representing the number of likes on three different Instagram posts over 7 days, stack them vertically using np.vstack() so that each row represents one post's weekly likes, and print the stacked array.
3.
You have an array of 12 Flipkart product IDs. Use np.array_split() to divide this array into 5 nearly equal parts, and display each part.<br><br><em><strong>Hint:</strong> Check the shape of each split to confirm the division.</em>
4.
Simulate a WhatsApp group chat: create a 2D NumPy array where each row is a user and each column is the number of messages sent per day for a week. Use np.insert() to add a new user (row) with their message counts, then use np.delete() to remove the user who sent the least messages overall.
5.
Given a NumPy array of YouTube video view counts, use .view() to create a view and .copy() to create a copy. Modify the first element in each and print all arrays to demonstrate the difference between view and copy.<br><br><em><strong>Hint:</strong> Observe which changes affect the original array.</em>