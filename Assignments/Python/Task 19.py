1. Define a Python class called Song with attributes title, artist, and duration (in seconds), and use the __init__() constructor to initialize these values when creating an object.

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    

song1 = Song("Varoo", "Shreya Ghosal", 200)

print(song1.title)
print(song1.artist)
print(song1.duration)


2. Create an object of the Song class for your favorite track from Spotify, and print out its title and artist using object attributes.

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


song1 = Song("Varoo", "Shreya Ghosal", 200)

print("Title:", song1.title)
print("Artist:", song1.artist)

3. Add a method play_preview(self) to your Song class that prints 'Playing 30-second preview of [title] by [artist]'. Call this method for your Song object.

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play_preview(self):
        print(f"Playing 30-second preview of {self.title} by {self.artist}")


song1 = Song("Varoo", "Shreya Ghosal", 200)

song1.play_preview()

4. Create a class called FoodOrder with attributes restaurant_name, items (a list), and total_price. Add a method add_item(self, item, price) that adds the item to the items list and updates total_price. Demonstrate by creating a FoodOrder object and adding two items like you would on Zomato.

class FoodOrder:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.items = []
        self.total_price = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total_price += price


order1 = FoodOrder("Domino's")

order1.add_item("Pizza", 250)
order1.add_item("Garlic Bread", 120)

print("Restaurant:", order1.restaurant_name)
print("Items:", order1.items)
print("Total Price:", order1.total_price)

5. Refactor your Song class so that it also tracks a play_count attribute (starting at 0), and add a method increment_play_count(self) that increases play_count by 1 each time it's called. Show how you would use this to count how many times a user plays a song.<br><br><em><strong>Hint:</strong> Call increment_play_count() multiple times and print play_count to see the update.</em>