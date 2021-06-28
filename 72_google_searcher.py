#Create a script that let the user type in a search term and opens and search on the browser for that term on google


import webbrowser

user_input = input("Enter Your google query: ")

webbrowser.open('https://google.cpm/search?q=%s' % user_input)
