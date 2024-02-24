# Imports
import random

states = ['Rock', 'Paper', 'Scissors']

# Playing
input('Ready?\n')
print(f'I choose {states[random.randrange(0, len(states))]}')