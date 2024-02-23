from pywebio.input import *
from pywebio.output import *
import random

running = True

put_text('Guess my number')
number = random.randrange(0, 10)
tries = 0

while running:
   try:
       answer = int(input("Enter an integer: "))
       print("The entered number is:", answer)

       if int(answer) < number:
           put_text(f'Wrong!\nYou said {answer} but my number is higher')
           tries = tries + 1
       elif int(answer) > number:
           put_text(f'Wrong!\nYou said {answer} but my number is lower')
           tries = tries + 1
       else:
           put_text(f'Well done!\nYou got it in {tries} tries.')

   except ValueError:
       put_text("Invalid input. Please enter an integer.")