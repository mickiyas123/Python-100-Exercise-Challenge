#Create a script that lets the user submit a password until they have satisfied three conditions:
#1. Password contains atleast one number
#2. Contains one uppercase letter
#3. It is at least 5 chars long

#print out message "Password is not fine" if the user didn't create a correct password



while True:
    passwd = input("Enter New password: ")
    if any(char.isdigit() for char in passwd) and any(char.isupper for char in passwd) and len(passwd) >=5:
        print("Password is fine")
        break
    
    else:
        print("Passwrd is not fine")    
    





            



   