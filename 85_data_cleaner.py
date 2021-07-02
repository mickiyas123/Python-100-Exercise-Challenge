# Question: Please download the attached countries-raw.txt file. The file contains the list of country names, but it also contains some unnecessary text among the countries. 

# Please clean the list with Python by generating a new text file that contains a flawless list of country names without any other text or break lines in it. The new file content should look like in the expected output.

# Expected output: 

# Afghanistan
# Albania
# Algeria
# Andorra
# Angola
# Antigua and Barbuda
# Argentina ....


with open('countries_raw.txt' , 'r') as file:
    content = file.readlines()
content = [i.strip("\n") for i in content if "\n" in i]
content = [i for i in content if i !=""]
content = [i for i in content if i !="Top of page"]
content = [i for i in content if len(i) != 1]

# print(content)

with open("countries.txt" ,'w') as file:
    for i in content:
        file.write(i+"\n")

