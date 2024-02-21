from pywebio.input import *
from pywebio.output import *

employees = [] #<-- Create empty list

file = open('employees.csv', 'r')

# Loop through each line of the file
for line in file:
   employees.append(line)

file.close()

# Sort the list of names before sending them to the user
employees.sort()

# Display popup with options
selected_option = select("Select a member of staff", employees)

# Create a dictionary to track password resets
staff_password_resets = {}

# Set the initial score to zero for each staff member
for employee in employees:
   staff_password_resets[employee] = 0

for employee in employees:
   if employee == selected_option:
       staff_password_resets[employee] += 1

table_data = [(key, value) for key, value in staff_password_resets.items()]
put_table(table_data, header=['Employee', 'Password Resets'])