# Question:  Here's another similar exercise. What will the following script output? Try to do this mentally if you can.

c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())

# c will be 2 beacuase it is assigned inside a function
