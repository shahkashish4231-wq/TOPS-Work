1.
Use re.findall() to extract all valid Indian phone numbers (10 digits, starting with 7, 8, or 9) from a given text string that contains random numbers, prices, and phone numbers like those seen in OLX or WhatsApp chats.
2.
Write a Python function using re.search() that checks if a given string contains a valid date in the format DD/MM/YYYY (e.g., 25/06/2024), and returns True if found, otherwise False.<br><br><em><strong>Hint:</strong> Use the pattern '\b\d{2}/\d{2}/\d{4}\b'.</em>
3.
Given a messy text copied from a Zomato review containing multiple emails, use re.findall() to extract all valid email addresses and print them as a list.
4.
Use re.sub() to mask all but the last 4 digits of any phone number in a string (e.g., replace 9876543210 with ******3210) like Paytm does for privacy.<br><br><em><strong>Constraint:</strong> Do not use loops; achieve this only with re.sub().</em>
5.
Use ChatGPT to generate a regex pattern that matches Flipkart-style order IDs (e.g., OD123456789012345000) and test it in Python using re.search() on sample order strings.