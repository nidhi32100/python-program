# Write a Python program to check if a string is a valid email address.


import re

def is_valid_email(email):
    # Regular expression for validating an email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Test the function
email = input("Enter an email address: ")

if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")

