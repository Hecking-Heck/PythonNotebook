# Imports
import random

# Create an empty list to store the facts
facts = []

# Open the file containing all the facts
factFile = open('facts.csv', 'r')

# Loop through the file and add all the lines into the facts list
for line in factFile:
    facts.append(line)

# Close the file once done with it
factFile.close()

# Sort the facts (This is unnessesary as we will randomly fetch facts anyway, I just like to do it)
facts.sort()

# Grab a random fact
factToDisplay = random.randrange(0, len(facts))

# Display the fact to the user
print(f'Fun Fact: {facts[factToDisplay]}')