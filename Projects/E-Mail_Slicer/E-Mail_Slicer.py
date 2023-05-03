email = input("Enter your e-mail address :- ").strip()  # To strip the entered text of unwanted elements

username = email[:email.index('@')]  # To get the characters before the @ symbol
domain = email[email.index('@')+1:]  # To get the characters after the @ symbol

print(f"Your Username is {username}")
print(f"Your Domain is {domain}")
