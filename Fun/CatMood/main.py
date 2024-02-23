import random

mood = random.randint(1, 3)

faces = [""" /\_/\\\n( o.o )\n > ^ <""", """ /\_/\\\n( o.o )\n > ^ <""", """ /\_/\\\n( o.o )\n > ^ <"""]

if mood == 1:
   print(f'I am happy.\n{faces[0]}')
elif mood == 2:
   print(f'I am angry.\n{faces[1]}')
elif mood == 3:
   print(f"I am sad.\n{faces[2]}")
else:
   print('Error moment.')