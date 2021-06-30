#Creaate a program that generates a password of 6 random alphanumeric characters in the range abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?

import random

password_range = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','^','&','*','(',')','?']

password = ""

for i in range (0,6):
    password+=random.choice(password_range)
print(password)  



# characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# chosen = random.sample(characters, 6)
# password = "".join(chosen)
# print(password)

    

