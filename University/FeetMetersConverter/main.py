from pywebio.input import *
from pywebio.output import *

put_markdown("# Measurement converter")

running = True

while running:
   user_input = input_group("Input measurement to convert",[input("", name='input_measure'), actions("", ['Convert to meters', 'Convert to feet'], name="action")])
   measurement_to_convert = user_input['input_measure']

   if user_input['action'] == 'Convert to meters':
       meters = float(measurement_to_convert) * 0.3048
       put_text(f"{measurement_to_convert} feet is {meters:.2f} in meters.")

       calculate_again = actions("Convert Another?", ['Yes', 'No'])

       if calculate_again == 'Yes':
           continue
       else:
           running = False

   elif user_input['action'] == 'Convert to feet':
       feet = float(measurement_to_convert) / 0.3048
       put_text(f"{measurement_to_convert} feet is {feet:.2f} in feet.")

       calculate_again = actions("Convert Another?", ['Yes', 'No'])

       if calculate_again == 'Yes':
           continue
       else:
           running = False
