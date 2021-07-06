#Cretae a program that asks the user to submit text repeatedly
#The program save the changes when user submits SAVE, but doesn't close
# The program saves the changes and close when the user submits CLOSE


from typing import Coroutine


while True:
    user_inputs = input("Enter Values: ")
    if user_inputs == 'CLOSE':
        break
    elif user_inputs == "SAVE":
        continue
    
    else:
        with open("user_data_save_close.txt", "a") as file:
                file.writelines(user_inputs + "\n")

   
        
        