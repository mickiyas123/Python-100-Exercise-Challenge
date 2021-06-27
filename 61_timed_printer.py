# Question: Create a program that prints out Hello  every two seconds.

# Expected output: 

# ...
# Hello
# Hello
# Hello
# Hello
# Hello
# Hello
# ...

import time

while True:
    print("Hello")
    time.sleep(2)
    # Even if it is an infinity loop it will print after 2 sec