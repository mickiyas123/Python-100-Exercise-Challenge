# Question: Please create an empty file (manually as you normally create Python files) and name it requests.py . Make sure the file has that name exactly.

# Then just paste the following code in the file:

# import requests

# r = requests.get("http://www.pythonhow.com")
# print(r.text[:100])

# Executing the script will throw an error. Please fix something to make the program print out the expected output. You should not modify the code itself, but something else.

import requests

r = requests.get("http://www.pythonhow.com")
print(r.text[:100])