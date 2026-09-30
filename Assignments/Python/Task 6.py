1. Create a Python dictionary called playlist_prices with at least 5 key-value pairs where the key is a Spotify playlist name (as a string) and the value is the playlist's price (as an integer). Print the dictionary.

playlist = {
    "Songs": 99,
    "Artists": 79,
    "Mashups": 129,
    "Bollywood": 109,
    "English": 149
}

print(playlist)

2. Write a function update_playlist_price(playlist, new_price) that updates the price of a given playlist in the playlist_prices dictionary. Test it by updating the price of any one playlist and printing the updated dictionary.

playlist = {
    "Songs": 99,
    "Artists": 79,
    "Mashups": 129,
    "Bollywood": 109,
    "English": 149
}


def update_playlist(new_playlist, new_price):
    playlist[new_playlist] = new_price


update_playlist("Top Hits", 110)

print(playlist)

3. Remove a playlist from the playlist_prices dictionary using the del statement. Print the dictionary after deletion to confirm the change.

playlist = {
    "Songs": 99,
    "Artists": 79,
    "Mashups": 129,
    "Bollywood": 109,
    "English": 149
}

del playlist["Artists"]

print(playlist)

4. Given two sets: set1 contains the names of restaurants you have ordered from on Zomato, and set2 contains the names of restaurants you have ordered from on Swiggy, find and print the union and intersection of these sets.<br><br><em><strong>Hint:</strong> Use the union() and intersection()

set1 = {"Dominos", "McDonalds", "Subway", "Honest"}
set2 = {"McDonalds", "Subway", "KFC", "Pizza Hut"}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)

print("Union:", union_set)
print("Intersection:", intersection_set)
