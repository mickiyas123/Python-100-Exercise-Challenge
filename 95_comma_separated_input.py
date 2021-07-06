#create a program that asks the user to input values separated by commas and those values will be stored in a separate line each in a text file

user_inputs = input("Enter Values: ")
user_input = user_inputs.split(",")





with open("user_data_commas.txt","a") as file:
    for i in user_input:
        file.write(i + "\n")
    
