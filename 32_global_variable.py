# Question:  What will the following script output? Please try to do this mentally if you can.
c = 1
def foo():
    return c
c = 3
print(foo())


# I am pretty sure it is 3 beacuse both 1 and 3 are global variables but the function is called after c is 3
