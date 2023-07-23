import random
import string
import pyperclip

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the length of the password: "))
password = generate_password(length)

# Copy the password to the clipboard
pyperclip.copy(password)

print("Random password:", password)
print("Password copied to clipboard!")
