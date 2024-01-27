# Importing the right libraries.
from pywebio.input import *
from pywebio.output import *

put_markdown('Covid Spotter')

options = ['none', 'coughing', 'headache', 'feeling drained']

data = input_group("Covid Information", [
    input = ('What is your name?'), type=STRING, name="name"),
    select("Symptoms:", options, name="symp")
    ])

# AS OF NOW THIS CODE DOES NOT WORK, I WILL UPDATE IT SOON