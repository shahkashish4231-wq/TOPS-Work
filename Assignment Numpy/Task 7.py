1. Create two NumPy arrays representing the ratings of 5 restaurants on Zomato and Swiggy, then use np.concatenate() to combine them into a single array of 10 ratings and print the result.

zomato_ratings = np.array([4.2, 3.8, 4.5, 4.0, 4.7])
swiggy_ratings = np.array([4.1, 3.9, 4.3, 4.6, 4.4])

combined_ratings = np.concatenate((zomato_ratings, swiggy_ratings))

print("Zomato ratings:", zomato_ratings)
print("Swiggy ratings:", swiggy_ratings)
print("Combined ratings:", combined_ratings)


2. Given three arrays representing the number of likes on three different Instagram posts over 7 days, stack them vertically using np.vstack() so that each row represents one post's weekly likes, and print the stacked array.

post1 = np.array([100, 120, 150, 180, 200, 220, 250])
post2 = np.array([80, 100, 130, 160, 190, 210, 230])
post3 = np.array([150, 170, 190, 210, 240, 260, 300])

weekly_likes = np.vstack((post1, post2, post3))

print(weekly_likes)


3. You have an array of 12 Flipkart product IDs. Use np.array_split() to divide this array into 5 nearly equal parts, and display each part.<br><br><em><strong>Hint:</strong> Check the shape of each split to confirm the division.</em>



4. Simulate a WhatsApp group chat: create a 2D NumPy array where each row is a user and each column is the number of messages sent per day for a week. Use np.insert() to add a new user (row) with their message counts, then use np.delete() to remove the user who sent the least messages overall.

messages = np.array([
    [20, 25, 30, 15, 22, 28, 35],  
    [10, 15, 12, 18, 20, 14, 16],  
    [30, 35, 28, 40, 32, 38, 45],  
    [5, 8, 10, 7, 6, 9, 11] 
])

print("Original group:")
print(messages)


new_user = np.array([[25, 30, 28, 35, 32, 40, 45]])

messages = np.insert(messages, 4, new_user, axis=0)

print("After adding new user:")
print(messages)

messages = np.delete(messages, least_user_index, axis=0)

print("After removing least active user:")
print(messages)


5. Given a NumPy array of YouTube video view counts, use .view() to create a view and .copy() to create a copy. Modify the first element in each and print all arrays to demonstrate the difference between view and copy.<br><br><em><strong>Hint:</strong> Observe which changes affect the original array.</em>
