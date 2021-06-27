# Question: Please complete the code so that it prints out the expected output.

# a = [1, 2, 3] 

# Expected output: 

# Item 1 has index 0
# Item 2 has index 1
# Item 3 has index 2

a = [1, 2, 3] 

for index,value in enumerate(a):
    # Enumerate function will go through both the index and the values
    print(f'Item {index} has index {value}')
