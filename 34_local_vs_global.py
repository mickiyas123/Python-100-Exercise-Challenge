# Question: The following script throws a NameError  in the last line saying that c  is not defined. Please fix the function so that there is no error and the last line is able to print out the value of c  (i.e. 1 ).

# def foo(): 
#     c = 1 
#     return c 
# foo() 
# print(c)
# This will print an error beacuse c is a local variable not a global one


# def foo(): 
#     c = 1 
#     return c 
# print(foo()) 


def foo(): 
    global c
    c = 1 
    return c 
foo() 
print(c)
# this is another way of sloving the exercise 