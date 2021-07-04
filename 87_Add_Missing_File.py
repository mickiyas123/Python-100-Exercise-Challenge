# Add the missing items to the file

checklist = ["Portugal","Germany","Spain"]
checklist = [i+ "\n" for i in checklist]

with open("countries_missing.txt") as file:
    context = file.readlines()


for i in checklist:
    context.append(i)
context = sorted(context)
# print(context)

with open("new_countries.txt", "w") as file1:
    file1.writelines(context)
    
