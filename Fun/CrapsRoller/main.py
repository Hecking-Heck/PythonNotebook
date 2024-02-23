# Craps Roller

# Import
import random

# generate random numbers
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

# Calculate the total
total = die1 + die2

# User feedback
print(f'You rolled a {die1} and a {die2} for a total of {total}')

# Wait to exit
input("\n\nPress the enter key to exit.")