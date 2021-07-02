# Question: Please take a look at the following list:

# checklist = ["Portugal", "Germany", "Munster", "Spain"]

# One of the items is not a country. Please use Python and the file containing the list of countries (attached) as data source to filter out the checklist  of non-country items. Once you have filtered out checklist , then print it out.

from typing import Coroutine


checklist = ["Portugal", "Germany", "Munster", "Spain"]
new_checklist = []

with open('countries.txt' ,'r') as file:
    lines = [line.strip() for line in file.readlines() ]  
# print(lines)    

for item in checklist:
    if item not in lines:
        continue
    else:
        new_checklist.append(item)
print(new_checklist)        
           