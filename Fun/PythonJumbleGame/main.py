# World Jumble
#
# The computer will pick a random word and jumble it
# The player will then have to guess the original word

import random

# A list of words for the computer to choose from
words = ('python', 'jumble', 'easy', 'difficult', 'answer', 'xylophone')

word = random.choice(words)

correctWord = word

jumbledWord = ''

while word:
    position = random.randrange(len(word))
    jumbledWord += word[position]
    word = word[:position] + word[(position + 1):]

print('Welcome to Word Jumble!')
print(f'The jumble is: {jumbledWord}')

guess = input('\nEnter your guess: ')
while guess != correctWord and guess != "":
    print('That is not it.')
    guess = input('\nEnter your guess: ')

if guess == correctWord:
    print("That's it! You guessed it!\n")
    
input('\n\nPress the enter key to exit.')