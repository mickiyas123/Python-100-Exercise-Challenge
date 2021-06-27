# Question: Please download the json file in the attachment and use Python to add a new employee to the content of the file so that the file looks like in the expected output below.

# from PIL import Image

# img = Image.open("Company1 expected output.png")
# img.show()
# this code is to show the excpected output image

import json

with open('company1.json', 'r+') as file:
    # r+ means read and write mode   
    data = json.loads(file.read())
    # Changes the json file to dict
    data['employees'].append(dict(firstName = "Albert", lastName = "Bert"))
    # added the new employe in the dict
    file.seek(0)
    # puts the cursor top of the file
    json.dump(data, file , indent=4,sort_keys=True)
    # convert it into json file
    file.truncate()
    # deletes everything under the cursor
