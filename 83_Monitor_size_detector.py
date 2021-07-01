# Question: Write a script that detects and prints out your monitor resolution.

# Expected output: 

# Width: 1920,  Height: 1080

import screeninfo


from screeninfo import get_monitors
for m in get_monitors():
    print("Width:",str(m.width),  "Height:",str(m.height))

