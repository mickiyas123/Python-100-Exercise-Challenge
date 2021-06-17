# Question: Please download the file in the attachment and use Python to print out its content.

# Expected output: 

import json


with open('company1.json' , 'r') as file:
    d = json.loads(file.read())
   
print(d)



# {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
#                {'firstName': 'Anna', 'lastName': 'Smith'},
#                {'firstName': 'Peter', 'lastName': 'Jones'}],
#  'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#             {'firstName': 'Jessy', 'lastName': 'Petter'}]}