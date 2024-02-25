# Imports
import random

# Possible characters to use in the password
possibleCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!£$%^&*()@#?'

# Ask the user for the required length of their password - a good default is 16
requiredLen = input("Enter password length:\n")

# Declare the empty password first
password = ''

# Loop through the required length and add a random character from the
# Possible chracters list to the new password
for x in range(int(requiredLen)):
    password += random.choice(possibleCharacters)

print(password)