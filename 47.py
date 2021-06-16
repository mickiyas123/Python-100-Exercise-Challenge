import os

files = os.listdir("letters/")

text = "python"
letters = []

for file in files:
    with open(f'{file}','r') as file:
        file = file.read()
        if file in text:
            letters.append(file)
print(letters)            

