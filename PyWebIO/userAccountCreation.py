# Importing the right libraries.
from pywebio.input import *
from pywebio.output import *

# For this test I will be writing a simple user account creation process.
# This is not a secure way, just a simple way to show how it can be done.

# User account creation input + variables.
firstNameInput = input('What is your First Name?')
lastNameInput = input('What is your Last Name?')
ageInput = input('What is your age?')

usernameInput = input('Enter a username:')
passwordInput = input('Enter a password:') # Note: this is stored in plaintext so it is not secure, this is fine for testing purposes.

# Logged In
put_markdown('Welcome **' + firstNameInput + lastNameInput + '**, you are logged in as **' + usernameInput + '**.') # This will display account information to the user.