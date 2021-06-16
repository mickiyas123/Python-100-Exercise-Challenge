# Question: The code produces an error. Please understand the error and try to fix it

# age = input("What's your age? ")
# age_last_year = age - 1
# print("Last year you were %s." % age_last_year)
# This will produce an error beacuse we can't substract str and int


age = int(input("What's your age? "))
age_last_year = age - 1
print("Last year you were %s." % age_last_year)
