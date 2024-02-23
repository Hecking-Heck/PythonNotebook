# Random Access Program
# Demonstrates String Indexing

import random

word = "index"
print(f'The word is: {word}\n')

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)
    print(f'The word at position[{position}] is {word[position]}')

input(f'\n\nPress the enter key to exit.')