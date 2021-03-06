# Question: Please download the attached urls.txt file. The file contains some broken URLs. Here's what the file contains:

# https:/www.google.com
# https:/www.yahoo.com
# https:/www.stackoverflow.com
# https:/www.pythonhow.com

# Please use Python to remove the "s" from "https" and add another forward slash next to the existing slash, so the content looks like in the expected output.

# Expected output: 

# http://www.google.com
# http://www.yahoo.com
# http://www.stackoverflow.com
# http://www.pythonhow.com


with open("urls.txt" ,'r') as file:
    content = file.readlines()

with open("cleanurls.txt","w") as file:
    for line in content:
        lineRemove = line.replace("s","",1)
        lineAddSlash = lineRemove[:6] + "/" + lineRemove[6:]
        file.writelines(lineAddSlash)
