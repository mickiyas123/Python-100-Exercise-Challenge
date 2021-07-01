#Create a script that lets the user submit a password until they have satisfied three conditions:
#1. Password contains atleast one number
#2. Contains one uppercase letter
#3. It is at least 5 chars long
# Give the exact reason why the user has not created a correct password


while True:
    notes = []
    passwd = input("Enter new password: ")
    if not any(char.isdigit() for char in passwd):
        notes.append("You need at least one number")
    if not any(char.isupper() for char in passwd):
        notes.append("You need at least one uppercase letter")
    if len(passwd) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("password is fine") 
        break   
    else:
        print("Password check the following:")
        for index,vlaue in enumerate(notes):
            print(str(index + 1) , vlaue)
                    