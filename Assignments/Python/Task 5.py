1. Create a list called playlist_ids with 5 integers representing Spotify playlist IDs, then use append() to add a new playlist ID at the end and print the updated list.

playlist = [101, 102, 103, 104, 105]

playlist.append(106)

print(playlist)

2. Simulate a Flipkart shopping cart: start with a list cart_items containing 't-shirt', 'shoes'. Use extend() to add ['jeans', 'cap'] to the cart, then print the final list of items.

citems = ["t-shirt", "shoes"]

items.extend(["jeans", "cap"])

print(items)

3. Write a function remove_last_item(order_list) that pops the last item from a Zomato order list and returns the removed item. Test it with a sample order_list.


4. Create a tuple called insta_filters with 4 Instagram filter names. Try to update the second filter and observe what error you get. Explain in a comment why this happens.<br><br><em><strong>Hint:</strong> Tuples are immutable, so direct assignment won't work.</em>'

filters = ["A", "B", "C", "D"]

filters[1] = "ABC"

print(filters)

5. Given two scenarios — storing a user's favorite genres (which may change) and storing a fixed set of IRCTC train classes ('Sleeper', 'AC 3 Tier', 'AC 2 Tier') — choose whether to use a list or tuple for each. Write one sentence explaining your choice for both.
