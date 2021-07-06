# Create a program that asks the user to submit text repeatedly
#the program closes when the user submit ClLOSE


while True:
    user_inputs = input("Write a Value: ")
    if user_inputs == "CLOSE":
        break
    else:
         with open("user_data.txt" ,"a") as file:
            for user_input in user_inputs:
                file.write(user_input + "\n")

    
    
    
   
