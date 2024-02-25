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

# This is the input variable
x = ''

# While the input variable is empty, do stuff (This means if they type anything, it will exit the while loop but if they just press enter it will continue.)
while x == '':
    # Tell the user what they can do
    print('Press enter for a Fact, enter stop to quit')
    
    # Store user input
    x = input()
    
    # Grab a random fact
    factToDisplay = random.randrange(0, len(facts))

    # Display the fact to the user
    print(f'Fun Fact: {facts[factToDisplay]}')