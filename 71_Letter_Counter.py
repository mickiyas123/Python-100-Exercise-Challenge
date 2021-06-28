# Question: Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt

# Expected output: 

# 47

import requests

t=requests.get('http://www.pythonhow.com/data/')

text = t.text
print(text.count('a'))