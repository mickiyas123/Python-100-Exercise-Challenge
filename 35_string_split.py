# Question: Create a function that takes any string as input and returns the number of words for that string.
# def now(words):
#     print(len(words))
# now("Hey")    

def count_words(strng): 
    strng_list = strng.split() 
    return len(strng_list) 
 
print(count_words("Hey there it's me!"))