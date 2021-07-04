# Add the missing items to the file

checklist = ["Portugal","Germany","Spain"]

with open("countries_missing.txt") as file:
    context = file.readlines()

context = [i.strip() for i in context]

for i in checklist:
    context.append(i)
context = sorted(context)
context = [i + "\n" for i in context]
# print(context)

with open("new_countries.txt", "w") as file1:
    file1.writelines(context)
    
