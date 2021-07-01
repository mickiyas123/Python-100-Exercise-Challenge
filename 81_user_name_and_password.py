#Create a script that lets the user submit a password until they have satisfied three conditions:
#1. Password contains atleast one number
#2. Contains one uppercase letter
#3. It is at least 5 chars long
# Give the exact reason why the user has not created a correct password
# Before asking for password, ask for username

while True:
    user_names = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
    user_name = input("Enter User Name: ")
    if user_name in user_names:
        print("Username Exists")
    else:
        notes = []
        print("Username is fine")
        passwd = input("Enter password: ")
        if not any(char.isdigit() for char in passwd):
            notes.append("Password must contain atleast one digit")
        if not any(char.isupper() for char in passwd):
            notes.append("password must contain atleast one digit")
        if len(passwd) < 5:
            notes.append("password should be atleast 5 char long")
        if len(notes) == 0:
            print("Password is fine")
            break
        else:
            print("Please check the following:")
            for note in notes:
                print(note)
                



