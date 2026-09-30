1. Create a Python script that takes any product name string (e.g., 'Redmi Note 12 Pro') and prints the name in all uppercase and all lowercase using the upper() and lower() methods.

product_name = input("Enter product name: ")

print("Uppercase:", product_name.upper())
print("Lowercase:", product_name.lower())

2. Write a function clean_brand_name(name) that removes leading/trailing spaces and replaces any hyphens '-' with a single space in the input string. Test it with ' oneplus-Nord '.

def clean_brand_name(name):
    name = name.strip()
    name = name.replace("-", " ")
    return name


print(clean_brand_name(" oneplus-Nord "))

3. Given the string 'Apple iPhone 14 Pro Max', use string slicing to extract and print only the brand name and the model (i.e., 'Apple' and 'iPhone 14 Pro Max') separately.<br><br><em><strong>Hint:</strong> Use split() to help find the split point, then use slicing for the substrings.</em>