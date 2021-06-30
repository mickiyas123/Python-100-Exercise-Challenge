# Question: Create a script that asks the user to enter their age and the script calculates the user's year of birth and prints it out in a string like in the expected output. Please make sure you generate the current year dynamically.

# Expected output: 

# We think you were born back in 1988

from datetime import datetime

year = int(datetime.now().strftime("%Y"))

birth_date = int(input("Enter your age: "))

age = year - birth_date

print("We think you were born back in",str(age))


