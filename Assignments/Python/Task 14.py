
1. Use open() in write mode to create a file called my_playlist.txt and write the names of 5 songs you listened to this week, each on a new line.

songs = [
    "Kesariya",
    "Believer",
    "Shape of You",
    "Blinding Lights",
    "Excuses"
]

with open("my_playlist.txt", "w") as file:
    for song in songs:
        file.write(song + "\n")

print("Playlist file created successfully.")

2. Read the my_playlist.txt file you created and print each song name in uppercase using Python file handling.

with open("my_playlist.txt", "r") as file:
    for song in file:
        print(song.strip().upper())

3. Download a sample CSV file of IPL cricket match scores (or create your own with columns: Match, Team1, Team2, Winner), then write Python code to read the CSV and print the name of the winning team for each match.

import csv

with open("ipl_matches.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("Winner:", row["Winner"])
    

4. Given a JSON file named user_profile.json containing details like username, followers, and bio (similar to an Instagram profile), use the json module to load the file and print the username and number of followers.

5. Use pathlib to check if a file called zomato_orders.json exists in your current directory, and print an appropriate message if it is found or not.<br><br><em><strong>Hint:</strong> Use Path('zomato_orders.json').exists() from the pathlib module.</em>

from pathlib import Path

file_path = Path("zomato_orders.json")

if file_path.exists():
    print("zomato_orders.json was found.")
else:
    print("zomato_orders.json was not found.")