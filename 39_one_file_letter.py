import string

letters = string.ascii_lowercase

for letter in letters:
    with open(f'{letter}.txt','w') as file:
        file.write(letter)

