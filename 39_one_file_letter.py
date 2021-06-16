import string,os

letters = string.ascii_lowercase

if not os.path.exists("letters"):
    os.mkdir("letters")
for letter in letters:
    with open("letters/" + letter + '.txt','w') as file:
        file.write(letter)   



# for letter in letters:
#     with open(f'{letter}.txt','w') as file:
#         file.write(letter)

