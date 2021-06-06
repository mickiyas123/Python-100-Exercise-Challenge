# Question:  Why is there an error in the code and how would you fix it?

# def foo(a=1, b=2):
#     return a + b

# x = foo - 1
#  This will through an error beacuse we are trying to add a function and int not the function value

def foo(a=1, b=2):
    return a + b

x = foo() - 1
# this is how we fix it
