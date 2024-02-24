# Imports
from pywebio.input import *
from pywebio.output import *

# Variable Input
charName = input('Enter a character name:\n')
charAge = input('Enter your characters age:\n')
charBirthplace = input('Enter your characters birthplace:\n')
charClass = select('Select a class', ['Warrior', 'Mage', 'Cleric', 'Templar'])

# Variables
skills = ['Strength', 'Health', 'Wisdom', 'Dexterity']
skillPoints = [0, 0, 0, 0]
startingPoints = 30

while startingPoints:
    put_text(f'You have {startingPoints} points to spend.')
    selectedSkill = select('Select a point to upgrade:', skills)
    skillPoints[skills.index(selectedSkill)] += 1
    startingPoints -= 1
    put_text(skills)
    put_text(skillPoints)
else:
    put_text('All of your skill points have been spent.')
    put_text(f'Good luck on your adventure, {charName} of {charBirthplace}.\nA {charClass} like you will be ruler of the lands in no time!')