1. Write a recursive function in Python called reverse_string(s) that takes a string and returns it reversed (e.g., 'hello' becomes 'olleh').

def reverse_string(s):
    if s == "":
        return s
    else:
        return reverse_string(s[1:]) + s[0]


result = reverse_string("hello")

print(result)

2. Build a recursive function sum_playlist_durations(durations) that takes a list of song durations (in seconds) and returns the total duration, similar to how Spotify totals a playlist.

3. Given the following code, identify whether the variable 'count' is local or global in each function, and explain what will be printed when run:

count = 10
def update_count():
count = 5
print('Inside:', count)

update_count()
print('Outside:', count)

-> count=10 is globally variable as it defines outside a function
-> count=5 is local variable as it defines inside a function

4. Create a recursive function count_likes(posts) that takes a nested dictionary representing Instagram posts and their replies (each with a 'likes' key), and returns the total number of likes across all posts and replies.<br><br><em><strong>Hint:</strong> Each reply can itself have more replies, so use recursion to sum likes at all levels.</em>

5. Write a Python script that demonstrates the lifetime of a local variable inside a function versus a global variable by printing their values before, during, and after a function call. Use variable names similar to 'user_status' and 'app_status', inspired by WhatsApp online/offline status.