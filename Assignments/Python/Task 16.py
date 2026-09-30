1. Use iter() and next() to manually loop through a list of 5 trending movies from BookMyShow and print each movie name one by one.
movies = ["Pushpa 2", "Stree 2", "Jab We Met", "Dhurandhar", "Dhurandhar 2"]

movie = iter(movies)

print(next(movie))
print(next(movie))
print(next(movie))
print(next(movie))
print(next(movie))

2. Create a playlist of 6 songs (as a list of strings) and use enumerate() to print each song with its position like Spotify's tracklist (e.g., '1. Kesariya').

songs = [
    "Song 1",
    "Song 2",
    "Song 3",
    "Song 4",
    "Song 5",
    "Song 6"
]

for position, song in enumerate(songs, start=1):
    print(f"{position}. {song}")


3. Given two lists — one of food items and one of prices — use zip() to print each food item with its price like a Zomato menu (e.g., 'Pizza - ₹250').

food_items = ["Pizza", "Burger", "Pasta", "Biryani", "Sandwich"]
prices = [250, 150, 220, 300, 180]

for food, price in zip(food_items, prices):
    print(f"{food} - ₹{price}")

4. Write a generator function called insta_posts_generator(posts) that takes a list of Instagram post captions and yields one caption at a time. Use next() to get and print the next post caption each time until all captions are printed.<br><br><em><strong>Hint:</strong> Use the yield keyword inside your function and handle StopIteration when all posts are done.</em>

5. Build a generator function called cashback_generator(transactions) that takes a list of Paytm transaction amounts and yields 5% cashback for each transaction. Print out the cashback values for all transactions.