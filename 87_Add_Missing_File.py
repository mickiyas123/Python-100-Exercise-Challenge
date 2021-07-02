# Add the missing items to the file

checklist = ["Portugal","Germany","Spain"]

with open("countries_missing.txt" ,"r") as file:
    content = file.readlines()
content = [i.strip("\n") for i in content ]
for item in checklist:
    content.append(item)
print(content)    
