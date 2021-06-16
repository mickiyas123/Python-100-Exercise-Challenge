# import os

# files = os.listdir('letters')

# letters = []
# for file in files:
#     with open(f'{file}','r') as file:
#         letters.append(file.read())
# print(letters)    

import glob

letters = []

fileList = glob.glob("letters/*.txt")

for fileName in fileList:
    with open(fileName, "r") as file:
        letters.append(file.read())
print(letters)        