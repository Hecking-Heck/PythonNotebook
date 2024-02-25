# This is a work in progress

# Import
from pywebio.input import *
from pywebio.output import *

# Make an empty list for the characters
characters = []
characterData = {}

# Open the character data
file = open('hsr_character-data.csv', 'r')

# Add the characters to a list
for line in file:
    fixedLine = line.split(',')[0].capitalize().replace('_', ' ')
    
    if "Trailblazer" not in fixedLine:
        characters.append(fixedLine)

# Close the character data
file.close()

# Manually add the main character
characters.append('Trailblazer')

# Sort the list of characters
characters.sort()

# Add character data to a list
for character in characters:
    characterData[character] = 0  

# Allow a user to select a character
selected_option = select('Select a character', characters)

# Right now this is just a table of all characters, but I want to add only the selected character
table_data = [(key, value) for key, value, in characterData.items()]

# Display character table
put_table(table_data, header=['Character', 'Rarity'])