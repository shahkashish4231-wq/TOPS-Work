1. Create a NumPy array called my_scores using np.array() with your last 5 Zomato order ratings (pick any integers between 1 and 5), and print the array.

my_scores = np.array([5, 4, 3, 5, 4])

print(my_scores)

2. Use np.arange() to generate an array of all even numbers between 10 and 30 (inclusive), then print the result.

even_numbers = np.arange(10, 31, 2)

print(even_numbers)


3. Generate an array of 8 equally spaced values between 0 and 1 using np.linspace(), and print the array.<br><br><em><strong>Hint:</strong> This is similar to how Spotify creates smooth volume sliders.</em>

volume = np.linspace(0, 1, 8)

print(volume)

4. Simulate a Flipkart-style 'Add to Cart' button counter by creating a NumPy array of 10 zeros using np.zeros(), then update the 3rd and 7th items to 1 (representing items added to cart), and print the updated array.

5. Use np.random.randint() to create an array of 6 random integers between 1000 and 9999 (representing random OTP codes like Paytm), and print the array.<br><br><em><strong>Constraint:</strong> Set the random seed to 42 using np.random.seed(42) before generating the array so your results are reproducible.</em>

np.random.seed(42)

otp_codes = np.random.randint(1000, 10000, 6)

print(otp_codes)