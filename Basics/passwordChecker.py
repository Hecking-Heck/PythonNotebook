from pywebio.input import *
from pywebio.output import *

# Getting input
passwordInput = input("What is your password?", TYPE=PASSWORD)

put_text(f"The password is {passwordInput}")

# Check loud
loud = passwordInput.upper()
isUpper = (loud == passwordInput)

put_text(f"Your uppercase password is: {loud}")

# is Upper
if isUpper:
    put_text(f"It is {isUpper} that your password is all uppercase, all uppercase is not acceptable.")

# Check name
titleVersion = passwordInput.title()
isName = (titleVersion == passwordInput)

if isName:
    put_text(f"It is {isName} that your password is a proper name, proper names are not acceptable.")

# No spaces
hasSpaces = passwordInput.replace("", "#")
hasNoSpaces = (hasSpaces == passwordInput)

if not hasNoSpaces:
    put_text(f"It is {hasNoSpaces} that your password has no spaces, spaces are not acceptable.")

# Empty password
letterCount = len(passwordInput)
hasZeroLength = letterCount == 0
put_text(f"It is {hasZeroLength} that your password is empty, empty is not acceptable.")

# Has _ or *
hasUnderscore = "_" in passwordInput
hasStar = "*" in passwordInput
has_OrStar = hasUnderscore or hasStar
hasNoStar = not has_OrStar
put_text(f"It is {hasNoStar} that your password does not have _ or * and is NOT acceptable.")

# Check are not
badPasswords = ['password', 'secret', 'manager', 'manchester united']
passIsBad = 0

for badPass in badPasswords:
    if badPass in passwordInput:
        passIsBad = badPass in passwordInput
        break

if passIsBad:
    put_text(f"Your password is bad.")


# Has digit
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
digitCount = 0
for digit in digits:
    if digit in passwordInput:
        digitCount = digitCount + 1

if digitCount > 0:
    if digitCount > 1:
        put_text(f"Password contains {digitCount} digits.")
    else:
        put_text(f"Password contains {digitCount} digit.")