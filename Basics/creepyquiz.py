from pywebio.input import *
from pywebio.output import *
import random

creepy = ['Staring at your co-worker for extended periods all day.',
         'Repeatedly asking for Tea(SEX)',
         'Starting a conversation about sex with your co-worker.( or asking overly personal questions )',
         'Following your co-worker around',
         'Checking up on your co-worker all the time ( in person and via text )',
         'Continuing to check up on your co-worker when they asked you to stop',
         'Touching your co-worker for example hair or shoulder ( without verbal consent )',
         'Feeling that you bought your co-worker coffee or something and then acting like they owe you something',
         'Buying gifts for your co-worker ( except Birthdays etc )',
         'Telling your co worker you are rich and could provide them with anything and you could look after them.',
         'Standing very close to your co-worker.IF they step back filling the space.',
         'You ask your co-worker to go for coffee and co-worker gives you some dumb excuse.Twice and you continued to keep asking',
         "Giving your co-worker a pet name like 'sweetheart' or 'honey'.",
         'Giving your-coworker unrequested advice on appearance like clothes or hair.',
         'You co-worker keep crossing their arms or keeps walking away when you approach and you keep',
         'approaching them for non- work related purpose.',
         'Being entitled and upset if you offered help and they said no.',
         'Going out and having dinner with somone for the first time and not offering to split it with them.',
         'Startiling your coworker when they are concentrating on work then pretending it was a joke.',
         'Your co-worker announces they have changed gender and you deliberatly stick with the previous pronouns.',
         'Insisting your co-worker sit with you in every class , when you have nothing in common',
         'Liking Andrew Tate.']

notcreepy = ['Being normal.', 'Not liking Andrew tate.']

def getQuestion():
   isCreepy = random.randrange(0,2)

   if isCreepy:
       currentQuestion = creepy[random.randrange(0, len(creepy))];
   else:
       currentQuestion = notcreepy[random.randrange(0, len(notcreepy))];

   confirm = actions(currentQuestion, ['Yes', 'No'])

   getQuestion()

   if confirm == 'Yes' and isCreepy:
       put_text(f'bad')
   else:
       put_text(f'good')

if __name__ == '__main__':
   getQuestion()